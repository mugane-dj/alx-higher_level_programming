#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let pattern = '';
      for (let col = 0; col < this.width; col++) {
        pattern += 'X';
      }
      console.log(pattern);
    }
  }

  rotate () {
    const heigth = this.height;
    const width = this.width;

    this.width = heigth;
    this.height = width;
  }

  double () {
    const height = this.height;
    const width = this.width;

    this.height = height * 2;
    this.width = width * 2;
  }
};
