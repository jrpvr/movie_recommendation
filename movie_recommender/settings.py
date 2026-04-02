"""
Django settings for movie_recommender project.
"""

from pathlib import Path

# 📁 Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# 🔐 SECURITY
SECRET_KEY = 'django-insecure-0bjza&)v%#0auta48e*j5uwebjj5u8fe_jbj5_k-==93puzy!7'

DEBUG = True

ALLOWED_HOSTS = []


# 📦 INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'movies',  # ✅ your app
]


# ⚙️ MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🌐 URL CONFIG
ROOT_URLCONF = 'movie_recommender.urls'


# 🎨 TEMPLATES (FIXED)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ global templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🚀 WSGI
WSGI_APPLICATION = 'movie_recommender.wsgi.application'


# 🗄️ DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# 🎨 STATIC FILES
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",   # ✅ for custom CSS/JS
]


# 🔑 DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 🔐 LOGIN SYSTEM (FIXED ✅)
LOGIN_URL = '/login/'              # 🔥 IMPORTANT FIX
LOGIN_REDIRECT_URL = '/'          # after login → home
LOGOUT_REDIRECT_URL = '/login/'   # after logout → login
LOGOUT_REDIRECT_URL = 'home'