#!/usr/bin/node
const request = require('request');
const film = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${film}`;
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    json.caracters.forEach(elm => {
      request(elm, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});