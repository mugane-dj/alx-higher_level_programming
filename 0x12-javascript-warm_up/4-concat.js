#!/usr/bin/node
const process = require('node:process');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 && arg2) {
  console.log(arg1 + ' is ' + arg2);
} else if (arg1 && !arg2) {
  console.log(arg1 + ' is ' + arg2);
} else {
  console.log(arg1 + ' is ' + arg2);
}
