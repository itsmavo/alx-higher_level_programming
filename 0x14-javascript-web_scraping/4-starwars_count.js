#!/usr/bin/node
const request = require('request');
const address = process.argv[2];

request(address, function(error, response, body) {
    if (error){
        console.log(error);
    } else {
        let results = JSON.parse(body).results;
        let count = 0;
        for (let i in results) {
            for (let chr of results[i].characters) {
                if (chr.search('/18/') > 0) {
                    count += 1;
                }
            }
        }
<<<<<<< HEAD
	console.log(count);
=======
       console.log(count);
>>>>>>> 7f58b867cdd0191a29b659f0b281fcf728418575
    }
})
