$('#btnLogin').on("click", function(){
	var usuario = $("#txtusuario").val();
	var password = $("#txtpassword").val();

	$.post( "/login/", $("#formLogin").serialize())
	.done(function( data ) {
		alert(data);
	});
});