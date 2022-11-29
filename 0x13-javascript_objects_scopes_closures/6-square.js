#!/usr/bin/node

const Sq5 = require('./5-square');

class Square extends Sq5 {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
       console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
