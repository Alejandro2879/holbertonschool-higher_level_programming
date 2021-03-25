#!/usr/bin/node

exports.esrever = function (list) {
  const newArr = [];
  for (let index = list.length - 1; index >= 0; index--) {
    newArr.push(list[index]);
  }
  return newArr;
};
