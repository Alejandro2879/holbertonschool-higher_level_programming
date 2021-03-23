#!/usr/bin/node

function secondMajor () {
  if (process.argv.length === 2) {
    return 0;
  } else if (process.argv.length === 3) {
    return 0;
  }
  if (isNaN(parseInt(process.argv[2]))) {
    return 0;
  }
  const sorted = process.argv.sort(function (a, b) { return a - b; });
  const major = sorted[sorted.length - 2];
  return major;
}

console.log(secondMajor());
