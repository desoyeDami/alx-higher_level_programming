#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = body.characters;

  characters.forEach(url => {
    request(url, { json: true }, (err, res, character) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(character.name);
    });
  });
});
