#!/usr/bin/node
const num = process.argv.slice(2).map(x => Number(x));
if (num.length <= 1) {
  console.log(0);
} else {
  console.log(num.sort().reverse()[1]);
}
