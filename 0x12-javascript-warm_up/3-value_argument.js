#!/usr/bin/node
const process = require('node:process');
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
