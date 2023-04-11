#!/usr/bin/node
const process = require('node:process');
const arg = process.argv[2];
if (parseInt(arg)) {
  const counter = parseInt(arg);
  for (let i = 0; i < counter; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
