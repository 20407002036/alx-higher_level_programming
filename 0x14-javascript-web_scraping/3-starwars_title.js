#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${movieID}';


request(url, (error, response, body) => {
    if (error) {
	console.error(error);
	return;
    }
    // convert the data to json
    try {
    const movieJson = JSON.parse(body);
	console.log(movieJson.title);
    } catch (parseError) {
	console.error(parseError);
    }
});
