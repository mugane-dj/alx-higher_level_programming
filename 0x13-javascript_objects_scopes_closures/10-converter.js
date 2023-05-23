#!/usr/bin/node
exports.converter = function (base) {
  function stringRep (num) {
    return num.toString(base);
  }
  return stringRep;
};
