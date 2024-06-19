#!/usr/bin/node
/**
 * defining a class Square that inherits from Square of
 * 5-square.js
 */

const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    let n = c;
    if (!c) {
      n = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(n.repeat(this.width));
    }
  }
}

module.exports = Square;
