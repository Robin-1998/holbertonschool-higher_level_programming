fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(res => res.json())
  .then(data => {
    console.log(data.name);
    document.getElementById('character').textContent = data.name;
  });

// res.json est une méthode qui convertit la réponse brute en texte
// then data récupère le nom en base de donnée
// et on fini par remplacer le contenu du texte dans l'id character
// par le nom du personnage appellé par data
