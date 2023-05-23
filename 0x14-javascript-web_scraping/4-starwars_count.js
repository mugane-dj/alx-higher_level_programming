#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;
    const charURL = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (let j = 0; j < characters.length; j++) {
      if (characters[j] === charURL) {
        count += 1;
      }
    }
  }
  console.log(count);
});
