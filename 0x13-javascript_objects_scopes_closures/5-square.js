#!/usr/bin/node

class Square {
  constructor (size) {
    this.size = size;
  }

  print () {
    for (let a = 0; a < this.size; a++) {
      let row = '';
      for (let b = 0; b < this.size; b++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  double () {
    this.size = this.size * 2;
  }
}

module.exports = Square;
