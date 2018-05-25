$(document).ready(function(){
	var socket = io.connect('/')

	socket.on('connect',function(){
		socket.send("Let's start the game!")
	});
	socket.on('message',function(msg){
		$("#messages").append('<li>'+ msg + '</li>');
		console.log("Yes ! Received !")
	})
	$('#sendbutton').on('click',function(){
		socket.send($('#myMessage').val());
		$(myMessage).val('');
	})
});