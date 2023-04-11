#!/usr/bin/node
const process = require('node:process');
const size = process.argv[2];
if (parseInt(size)) {
  for (let i = 0; i < parseInt(size); i++) {
    let pattern = '';
    for (let j = 0; j < parseInt(size); j++) {
      pattern += 'x';
    }
    console.log(pattern);
  }
} else {
  console.log('Missing size');
}
