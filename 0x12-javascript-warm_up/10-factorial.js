#!/usr/bin/node

// For a recursive function get the brealpoint
// When counter variable is 1.
// Have a

function factorial (value) {
  if (isNaN(value)) {
    return 1;
  } else if (value <= 1) {
    return 1;
  } else {
    return (value * factorial(value - 1));
  }
}

const number = parseInt(process.argv[2]);

console.log(factorial(number));
