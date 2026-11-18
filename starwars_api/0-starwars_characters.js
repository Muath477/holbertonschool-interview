#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

function getJson (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// the requests run at the same time, but Promise.all keeps the results
// in the order of the characters list, so the names print in that order
getJson(filmUrl)
  .then((film) => Promise.all(film.characters.map(getJson)))
  .then((characters) => {
    characters.forEach((character) => console.log(character.name));
  })
  .catch((error) => console.log(error));
