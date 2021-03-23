#!/usr/bin/node

let major = parseInt(process.argv[2]);
let secMajor = parseInt(process.argv[2]);

function secondMajor () {
  if (process.argv.length === 2) {
    console.log(0);
  } else if (process.argv.length === 3) {
    console.log(0);
  }
  if (isNaN(major)) {
    console.log(0);
  }
  for (let iter = 0; iter < process.argv.length; iter++) {
    if (process.argv[iter] > major) {
      secMajor = major;
      major = process.argv[iter];
    }
  }
  console.log(secMajor);
}

secondMajor();
