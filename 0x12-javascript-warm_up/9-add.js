#!/usr/bin/node

function add (a, b) {
  return (a +b);
}
// The function receive the args as strings
// Remember to parse them to int
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || (isNaN(arg2))) {
    console.log('NaN');
} else {
    console.log(add(arg1, arg2));
}