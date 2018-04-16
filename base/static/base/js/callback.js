$('#get-callback').on('click', function() {
	$('.callback-form').css({ display : 'block' });
});
$('#callback-close').on('click', function() {
	$('.callback-form').css({ display : 'none' });
});

$('#callback-form').on('submit', function(e) {

	e.preventDefault();

	$.post( "/callback", { 
		'data' : JSON.stringify({
        		'form' : $('#callback-form').serialize(),
        	})
	} , function(response) {
		console.log(response);
		if (response.message == 'Success')
			window.location = '/success-callback';
		else if (response.message == 'redirect') {
			window.LiqPayCheckoutCallback(response.hash_data, response.signature);
		}
	});
});