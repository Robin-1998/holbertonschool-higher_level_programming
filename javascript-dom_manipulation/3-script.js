const header = document.querySelector('#header');

document.querySelector('#toggle_header').addEventListener('click', function () {
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else if (header.classList.contains('green')) {
    header.classList.replace('green', 'red');
  } else {
    header.classList.add('red');
  }
});

// on ajoute la condition que si au clic, on regarde si le header à la class red
// si oui, on le remplace par geen
// si le header contient green alors on le remplace par red
// et pour finir si on ajoute red de base pour éviter qu'elle soit vide
