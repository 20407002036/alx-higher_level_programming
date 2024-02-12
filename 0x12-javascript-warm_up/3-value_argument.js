#!/usr/bin/node

const arg = process.argv - 2;

if (arg !== 0) {
  console.log(process.argv[3]);
} else {
  console.log('No arguement');
}
