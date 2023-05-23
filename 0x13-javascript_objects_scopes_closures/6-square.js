#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    for (let row = 0; row < this.height; row++) {
      let pattern = '';
      for (let col = 0; col < this.width; col++) {
        if (!c) {
          pattern += 'X';
        } else {
          pattern += c;
        }
      }
      console.log(pattern);
    }
  }
};
