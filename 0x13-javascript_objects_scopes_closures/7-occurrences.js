#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      occur++;
    }
  }
  return occur;
};
