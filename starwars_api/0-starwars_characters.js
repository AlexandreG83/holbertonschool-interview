#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film:', error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  // Fetch characters in order
  let completed = 0;

  characterUrls.forEach((url, index) => {
    request(url, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        return;
      }

      const character = JSON.parse(charBody);
      // Store the result with its index
      characterUrls[index] = character.name;
      completed++;

      // When all characters have been fetched, print them in order
      if (completed === characterUrls.length) {
        characterUrls.forEach(name => console.log(name));
      }
    });
  });
});