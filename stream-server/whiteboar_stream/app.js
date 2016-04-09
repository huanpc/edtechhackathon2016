var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');
var users = require('./routes/users');

var app = express();

// require socketIO
// listen on port 3001
var server = require('http').Server(app);
var io = require('socket.io').listen(server);
server.listen(3001);

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);
app.use('/users', users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});

io.sockets.on('connection', function (socket) {

 // A User starts a path
 socket.on( 'startPath', function( data, sessionId ) {

   socket.broadcast.emit( 'startPath', data, sessionId );

 });

 // A User continues a path
 socket.on( 'continuePath', function( data, sessionId ) {

   socket.broadcast.emit( 'continuePath', data, sessionId );

 });

 // A user ends a path
 socket.on( 'endPath', function( data, sessionId ) {

   socket.broadcast.emit( 'endPath', data, sessionId );

 });  

});

// Quiz channel
// teacher ask question channel
var askSocket = io
  .of('/ask')
  .on('connection', function (socket) {
    socket.on('teacher', function(data){
      socket.emit('question', data);  
    });        
  });


// teacher receive answer
var teacherSocket = io
  .of('/teacher')
  .on('connection', function (socket) {    
    // answerSocket.emit('a message', {
    //     everyone: 'in'
    //   , '/ask': 'will get'
    // });
});
// student answer question
var answerSocket = io
  .of('/student_answer')
  .on('connection', function (socket) {    
    socket.on('answer',function(data){
      teacherSocket.emit('answer', data);  
    });    
  });

module.exports = app;
