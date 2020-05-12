#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];
request(url + episode, (err, res, body) => {
  if (err) { console.log(err); } else if (res.statusCode === 200) {
    const json = JSON.parse(body);
    console.log(json.title);
  } else { console.log('An error occured. Status code: ' + res.statusCode); }
});
