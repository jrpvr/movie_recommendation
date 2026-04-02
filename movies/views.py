from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
import requests
import re
import random
from collections import Counter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

API_KEY = "6aed4a4e"

# =========================
# 🔥 RANDOM QUERY
# =========================
def generate_query():
    queries = [
        "batman", "spiderman", "joker",
        "action", "comedy", "horror",
        "romance", "avengers", "thriller", "hindi"
    ]
    return random.choice(queries)


# =========================
# 🔍 SEARCH SUGGESTIONS
# =========================
def suggest(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(title__icontains=query)[:5]
    return JsonResponse([m.title for m in movies], safe=False)


# =========================
# 🎬 HOME
# =========================
@login_required
def home(request):
    query = request.GET.get('q') or generate_query()
    url = f"http://www.omdbapi.com/?s={query}&apikey={API_KEY}"

    try:
        data = requests.get(url, timeout=5).json()
        api_movies = data.get('Search', [])
    except:
        api_movies = []

    if not api_movies:
        api_movies = requests.get(
            f"http://www.omdbapi.com/?s=spiderman&apikey={API_KEY}"
        ).json().get('Search', [])

    final_movies = []

    for m in api_movies:
        title = m.get('Title')
        imdb_id = m.get('imdbID')

        movie = Movie.objects.filter(title=title).first()

        if not movie:
            try:
                details = requests.get(
                    f"http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
                ).json()

                year_match = re.search(r'\d{4}', details.get('Year', ''))
                year = int(year_match.group()) if year_match else 0

                poster = details.get('Poster')
                if poster == "N/A" or not poster:
                    poster = "https://via.placeholder.com/300x450?text=No+Image"

                rating = details.get('imdbRating')
                rating = float(rating) if rating and rating != "N/A" else 0

                movie = Movie.objects.create(
                    title=details.get('Title', 'Unknown'),
                    year=year,
                    genre=details.get('Genre', ''),
                    description=details.get('Plot', ''),
                    poster=poster,
                    rating=rating
                )
            except:
                continue

        final_movies.append(movie)

    random.shuffle(final_movies)

    paginator = Paginator(final_movies, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    liked_ids = Movie.objects.filter(
        liked_by=request.user
    ).values_list('id', flat=True)

    return render(request, 'movies/home.html', {
        'movies': page_obj,
        'liked_movies': liked_ids
    })


# =========================
# ❤️ LIKE
# =========================
@login_required
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.user in movie.liked_by.all():
        movie.liked_by.remove(request.user)
    else:
        movie.liked_by.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'home'))


# =========================
# 📌 WATCHLIST
# =========================
@login_required
def toggle_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.user in movie.watchlisted_by.all():
        movie.watchlisted_by.remove(request.user)
    else:
        movie.watchlisted_by.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'home'))


# =========================
# 📌 WATCHLIST PAGE
# =========================
@login_required
def watchlist_page(request):
    movies = Movie.objects.filter(watchlisted_by=request.user)
    return render(request, 'movies/watchlist.html', {'movies': movies})


# =========================
# 🎬 DETAIL
# =========================
@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


# =========================
# 🔥 RECOMMENDATIONS
# =========================
@login_required
def recommendations(request):
    liked_movies = Movie.objects.filter(liked_by=request.user)

    genres = []
    for m in liked_movies:
        genres.extend(m.genre.split(','))

    genre_count = Counter(genres)

    if genre_count:
        top_genre = genre_count.most_common(1)[0][0].strip()
        recommended = Movie.objects.filter(genre__icontains=top_genre)
    else:
        recommended = Movie.objects.all()

    recommended = list(recommended.exclude(liked_by=request.user))
    random.shuffle(recommended)

    paginator = Paginator(recommended, 8)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'movies/recommendations.html', {
        'movies': page_obj
    })