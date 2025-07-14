fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    const film = data.results;
    // variable qui contient le tableau de la base de donnée recherché
    const listfilm = document.getElementById('list_movies');
    film.forEach(movie => {
    // forEach fait office de boucle en Javascript
      const thelist = document.createElement('li');
      thelist.textContent = movie.title;
      listfilm.appendChild(thelist);
      // dans cette boucle on créé la liste et on y insert chaque titre de film
    });
  });
