#!/usr/bin/node
let logCount = -1;
exports.logMe = function (item) {
  logCount++;
  console.log(logCount + ': ' + item);
};
