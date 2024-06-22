#!/usr/bin/node

class Square {
  constructor (size) {
    this.size = size;
  }

  charPrint (c) {
    for (let a = 0; a < this.size; a++) {
      let row = '';
      for (let b = 0; b < this.size; b++) {
        if (!c) {
          row += 'X';
        } else {
          row += 'c';
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
