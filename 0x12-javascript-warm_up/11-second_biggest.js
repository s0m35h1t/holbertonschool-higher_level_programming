#!/usr/bin/node
'use strict';
let max = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort((a, b) => a - b);
  max = args[args.length - 2];
}
console.log(max);
