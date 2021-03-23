#!/usr/bin/node

let major = parseInt(process.argv[2]);
let secMajor = parseInt(process.argv[2]);

function secondMajor () {
  for (let iter = 0; iter < process.argv.length; iter++) {
    if (process.argv[iter] > major) {
      secMajor = major;
      major = process.argv[iter];
    }
  }
  console.log(secMajor);
}

secondMajor();
