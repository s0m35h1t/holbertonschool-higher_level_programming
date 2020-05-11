#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');
const fpA = process.argv[2];
const fpB = process.argv[3];
const fpC = process.argv[4];
const textA = readFileSync(fpA, 'utf8');
const textB = readFileSync(fpB, 'utf8');
writeFileSync(fpC, textA + textB);
