#!/usr/bin/node
const process = require('node:process');
const arg1 = process.argv[2];
if (parseInt(arg1)) {
  console.log('My number: ' + parseInt(arg1));
} else {
  console.log('Not a number');
}
