#!/usr/bin/node
const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/";

request('${url}films', (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    

	console.log(data.title);
  } else {
    console.log(error);
  }
});
