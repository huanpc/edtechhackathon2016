var askSocket = io.connect('http://localhost:3001/ask')
    , teacherSocket = io.connect('http://localhost:3001/teacher')
    , answerSocket = io.connect('http://localhost:3001/student_answer');

// Quiz channel
// receive question from teacher
var askSocket = io
  .of('/ask')
  .on('connection', function (socket) {
    socket.on('question', function(data){
      // receive question
    });        
});


// teacher receive answer
var teacherSocket = io
  .of('/teacher')
  .on('connection', function (socket) {    
  	socket.on('answer',function(data){
  		// student receive answer
  	});
});

// student answer question
var answerSocket = io
  .of('/student_answer')
  .on('connection', function (socket) {    
  	socket.emit('answer', {data: 'data'}});    
  });

window.onload = function() {
	alert(document.getElementById('answer').val());	
}