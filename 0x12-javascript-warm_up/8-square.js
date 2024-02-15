#!/usr/bin/node

const size = process.argv[2];
const intSize = parseInt(size);
let i = 0; let j = 0;

if (isNaN(size) || isNaN(intSize)) {
  console.log('Missing size');
} else {
  // The console.log function will print in the next line

  // for (i = 0; i < intSize; i++) {
  //     for (j = 0; j < intSize; j++) {
  //         console.log('X');
  //     }
  // }

  // To solve construct  each row with the chars.
  // print the row using console.log

  for (i = 0; i < intSize; i++) {
    // craete an empty string
    let row = '';
    for (j = 0; j < intSize; j++) {
      // Append to the empty string.
      row += 'X';
    }

    console.log(row);
  }
}
