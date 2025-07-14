document.querySelector('#add_item').addEventListener('click', function () {
  const thelist = document.createElement('li');
  thelist.textContent = 'Item';
  document.querySelector('.my_list').appendChild(thelist);
});

// lorsque l'utilisateur clique sur add_item il créé une li (liste)
// dans la liste newItem on ajoute l'élément Item
// on ajoute la liste avec la classe my_list.
// La classe my_list correpsond à notre ul on utilise donc appendchild
// pour imbriquer la liste dans l'ul, comme pour imbriquer
// une balise dans une autre en HTML
