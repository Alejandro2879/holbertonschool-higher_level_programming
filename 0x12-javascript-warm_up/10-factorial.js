#!/usr/bin/node

const nTimes = parseInt(process.argv[2]);

function recursive (numb) {
  if (numb === 0) {
    return 1;
  } else if (isNaN(numb)) {
    return 1;
  } else {
    return numb * recursive(numb - 1);
  }
}

const res = recursive(nTimes);
console.log(res);
