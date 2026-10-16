#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
