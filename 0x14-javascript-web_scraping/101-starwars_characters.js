#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/films/' + process.argv[2];

function printCharacters (characters, idx) {
  request(characters[idx], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

request(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
