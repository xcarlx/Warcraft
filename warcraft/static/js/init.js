(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$("#btnCambioPassword").on("click",function(){
	$('#modalPassword').find('p').load("/personal/cambiopassword/");
	$('#modalPassword').find('h4').text("Cambiar contraseña");
 	$('#modalPassword').modal('open');
});

$("#btnGuardarPassword").on("click",function(){
	var formData = new FormData($("#formPersonaPassword")[0]);
	// formData.append('foto', img);

	$.ajax({
		url: '/personal/cambiopassword/',
		data: formData,
		processData: false,
		contentType: false,
		type: 'POST',
		success: function(data){
			if(data["ok"]){
				Materialize.toast("Datos modificados correctamente", 4000,  'rounded');
				$('#modalPassword').modal('close');
				// $("html").waitMe({text: 'Cerrando Sesión'});
				location.href = "/logout/";
        
			}else{
				$('#modalPassword').find('p').html(data);
			}
		}
	});
});
	