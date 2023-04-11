#!/usr/bin/node
const process = require('node:process');
function factorial (number) {
  const num = parseInt(number);
  if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(process.argv[2]));
