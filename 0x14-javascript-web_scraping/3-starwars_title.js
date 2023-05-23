#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const baseURL = 'https://swapi-api.alx-tools.com/api/films/:id';
const url = baseURL.replace(':id', id);
request(url, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  console.log(JSON.parse(body).title);
});
