#!/usr/bin/node

const a = Number(process.argv[2]);

function factorial (a) {
  let result = 1;

  if (isNaN(a)) {
    return 1;
  } else {
    for (let i = 2; i <= a; i++) {
      result *= i;
    }
    return result;
  }
}

const result = factorial(a);
console.log(result);
