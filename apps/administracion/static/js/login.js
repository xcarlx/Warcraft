$("#txtusuario").focus();

 $('.button-collapse').sideNav({
      menuWidth: 300, // Default is 300
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    });
    $('.dropdown-button').dropdown('open');
        
$('#btnLogin').on("click", function(){
	if($("#txtusuario").val().length==0){
		Materialize.toast("No ha digitado el usuario", 4000,  'rounded');
		$("#txtusuario").focus();
	}else if($("#txtpassword").val().length==0){
		Materialize.toast("No ha digitado el password", 4000,  'rounded');
		$("#txtpassword").focus();
	}else{

		$.post( "/login/", $("#formLogin").serialize())
		.done(function( data ) {
			if(data['result']){
				location.reload(true);
			}else{
				$("#txtusuario").focus();
			 	Materialize.toast(data['message'], 4000,  'rounded');
			 	
			}
		});

	}
	
});