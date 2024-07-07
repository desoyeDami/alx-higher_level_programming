#!/usr/bin/node

const i = Number(process.argv[2]);

if (isNaN(i)) {
  console.log('Missing size');
} else if (i > 0) {
  for (let a = 0; a < i; a++) {
    let row = '';
    for (let b = 0; b < i; b++) {
      row += 'X';
    }
    console.log(row);
  }
}
