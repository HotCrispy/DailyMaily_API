const express = require('express'); // express 모듈 추가하기
console.log("server running");
const app = express();
const port = 8080;
const path = require('path');

app.use(express.static(__dirname +'/'));

app.get('/', function(request, response) {
    response.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(port, function(err) {
    console.log('Connected port - ' + port);
    if (err) {
        return console.log('Found error - ', err);
    }
});
