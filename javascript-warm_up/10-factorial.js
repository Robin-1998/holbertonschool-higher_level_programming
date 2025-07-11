#!/usr/bin/node

function fact (n) {
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}
console.log(fact(process.argv[2]));

// https://www.geeksforgeeks.org/javascript/factorial-of-a-number-using-javascript/
