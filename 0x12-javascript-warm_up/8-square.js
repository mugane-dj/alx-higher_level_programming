#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let pattern = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      pattern += 'X';
    }
    console.log(pattern);
  }
} else {
  console.log('Missing size');
}
