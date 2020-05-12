#!/usr/bin/node
const request = require('request');
const {
  writeFile
} = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    writeFile(filePath, body, 'utf-8', err => {
      console.log(err);
    });
  }
});
