#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('No argument');
}
if (process.argv.length === 1) {
  console.log('Argument found')
}
else {
  console.log('Arguments found')
}
// process.argv est un tableau contenant les arguments
// process.argv.length renvoie le nombre d'éléments utiliser
// === est l'équivalent de == dans une condition en langage C
