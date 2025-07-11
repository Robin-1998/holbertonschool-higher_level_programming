#!/usr/bin/node

const count = parseInt(process.argv[2]);

if (!count) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}

// on stock dans une variable count la convertion du deuxième
// argument en entier
// et on utilise une boucle similaire au langage C pour boucler en fonction
// des chiffres utiliser en argument
