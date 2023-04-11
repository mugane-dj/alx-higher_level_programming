#!/usr/bin/node
const args = process.argv;
process.argv.splice(0, 2);
function secondBiggest (array) {
  if (args.length === 0) { return 0; }
  if (args.length === 1) { return 0; }
  const arr = [];
  args.forEach(arg => {
    arr.push(parseInt(arg));
  });
  const max = Math.max(...arr);
  const index = arr.indexOf(max);
  if (index > -1) {
    arr.splice(index, 1);
  }
  const secondMax = Math.max(...arr);
  return secondMax;
}
console.log(secondBiggest(args));
