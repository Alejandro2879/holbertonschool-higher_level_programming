#!/usr/bin/node

const nTimes = parseInt(process.argv[2]);

if (isNaN(nTimes)) {
  console.log('Missing size');
} else {
  for (let fIter = 0; fIter < nTimes; fIter++) {
    console.log('X'.repeat(nTimes));
  }
}
