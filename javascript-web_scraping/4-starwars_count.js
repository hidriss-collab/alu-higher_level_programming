#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

    console.log(films.filter((film) => film.characters.includes(characterUrl)).length);
  }
});
