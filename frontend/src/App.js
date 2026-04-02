import { useEffect, useState } from "react";

function App() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then(res => res.json())
      .then(data => setMovies(data));
  }, []);

  return (
    <div>
      {movies.map(m => <h3>{m.title}</h3>)}
    </div>
  );
}

export default App;