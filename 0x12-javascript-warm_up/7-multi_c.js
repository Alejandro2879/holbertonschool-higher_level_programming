#!/usr/bin/node

const nTimes = parseInt(process.argv[2]);
let iter;

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (iter = 0; iter < nTimes; iter++) {
    console.log('C is fun');
  }
}
