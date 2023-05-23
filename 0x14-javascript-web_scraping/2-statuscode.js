#!/usr/bin/node
let request = require('request');
let adress = process.argv[2];
request(adress, function (error, response, body) {
    if(error){
        console.log(error);
    } else {
        console.log('code:', response['statusCode']);
    }
});
