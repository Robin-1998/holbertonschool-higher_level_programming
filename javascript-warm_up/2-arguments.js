#!/usr/bin/env node
if (process.argv.length === 2) {
  console.log("No argument");
} else if (process.argv.length === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
// process.argv est un tableau contenant les arguments
// process.argv.length renvoie le nombre d'éléments utiliser
// === est l'équivalent de == dans une condition en langage C
