#!/usr/bin/node

const i = Number(process.argv[2]);
let a = 0;

if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  while (a < i) {
    console.log('C is fun');
    a++;
  }
}
