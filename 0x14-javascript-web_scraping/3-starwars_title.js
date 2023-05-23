#!/usr/bin/node
let request = require('request');
let n = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/:id' + n, function(error, response, body) {
    if (error){
        console.log(error);
    } else {
        console.log(JSON.parse(body)['title']);
    }
});