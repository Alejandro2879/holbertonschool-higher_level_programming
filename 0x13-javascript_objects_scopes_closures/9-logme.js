#!/usr/bin/node

let callsCounter = 0;

exports.logMe = function (item) {
  console.log(callsCounter + ': ' + item);
  callsCounter++;
};
