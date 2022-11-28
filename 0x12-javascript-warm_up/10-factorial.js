#!/usr/bin/node
const num1 = isNaN(Number(process.argv[2])) ? 1 : Number(process.argv[2]);
function factorial(a) {
  if (a === 0) return 1;
  return a * factorial(a - 1);
}

console.log(factorial(num1));
