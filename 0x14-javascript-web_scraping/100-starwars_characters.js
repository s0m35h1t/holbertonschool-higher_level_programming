#!/usr/bin/node
const request = require('request');
const film = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${film}`;
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
