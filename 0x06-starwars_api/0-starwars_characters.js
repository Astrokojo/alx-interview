#!/usr/bin/node
const request = require('request');

// URL for the film endpoint
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// initial request for the film details
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const film = JSON.parse(body);

    // Extract the characters array
    const characters = film.characters;

    // Function to get character details and print names
    const printCharacterName = (url, callback) => {
      request(url, (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }

        if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
          callback();
        }
      });
    };

    // Helper function to process character urls in sequence
    const processCharacters = (index) => {
      if (index < characters.length) {
        printCharacterName(characters[index], () => {
          processCharacters(index + 1);
        });
      }
    };
    // run the process from the start of the array
    processCharacters(0);
  }
});
