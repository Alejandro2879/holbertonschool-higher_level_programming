#!/usr/bin/node

const nTimes = parseInt(process.argv[2]);
let iter;

if (isNaN(nTimes)) {
  console.log('Missing size');
} else {
  for (iter = 0; iter < nTimes; iter++) {
    console.log('x'.repeat(nTimes));
  }
}
