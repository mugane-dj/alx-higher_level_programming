#!/usr/bin/node
// Get array of arguments.
const args = process.argv;
// Remove execPath and file path from array.
process.argv.splice(0, 2);
function secondBiggest (array) {
  if (args.length === 0) { return 0; }
  if (args.length === 1) { return 0; }
  const arr = [];
  // Parse each arg into an integer and push to a new array.
  args.forEach(arg => {
    arr.push(parseInt(arg));
  });
  // Get max from array and remove using splice method.
  const max = Math.max(...arr);
  const index = arr.indexOf(max);
  if (index > -1) {
    arr.splice(index, 1);
  }
  // Get second max int and return it.
  const secondMax = Math.max(...arr);
  return secondMax;
}
console.log(secondBiggest(args));
