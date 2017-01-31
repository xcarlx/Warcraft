
$('.modal').modal({

	dismissible: false, // Modal can be dismissed by clicking outside of the modal
	// opacity: .5, // Opacity of modal background
	// inDuration: 300, // Transition in duration
	// outDuration: 200, // Transition out duration
	// startingTop: '40%', // Starting top style attribute
	// endingTop: '10%', // Ending top style attribute
	// ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
	// 	alert("Ready");
	// 	console.log(modal, trigger);
	// },
	// complete: function() { alert('Closed'); } // Callback for Modal close
});

$("#btnEditar").on("click", function(){

	$('#modal1').find('#ModalContenido').load("editar/");

	$('#modal1').find('#ModalTitulo').text("Editando Perfil");

	$('#modal1').modal('open');


});	
$("#btnGuardarPerfil").on("click", function(){
	var img=$('#id_foto').val();
	// $.post( "editar/", $( "#formPersona" ).serialize()+'&foto='+encodeURIComponent(img))
	var formData = new FormData($("#formPersona")[0]);
	// formData.append('foto', img);

	$.ajax({
		url: 'editar/',
		data: formData,
		processData: false,
		contentType: false,
		type: 'POST',
		success: function(data){
			if(data["ok"]){
				Materialize.toast("Datos modificados correctamente", 4000,  'rounded');
				$('#modal1').modal('close');
				location.reload();
        
			}else{
				$('#modal1').find('#ModalContenido').html(data);
			}
		}
	});
	// $.post( "editar/", $( "#formPersona" ).serialize())
	// .done(function( data ) {
		
	// 	$('#modal1').find('#ModalContenido').html(data);
	// });
});	



