$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

/*$('.existing-customer-email-btn').click(function(){
    $('.existing-customer-email').addClass("show");
    $('.existing-customer-email-btn').click(function(){
      $('.existing-customer-email').removeClass("show");
    })
});*/

$('.existing-customer-email-btn').on('click',function(){
    $('.existing-customer-email').show();
    $('.new-customer-form').hide();
});

$('.new-customer-email-btn').on('click',function(){
    $('.new-customer-form').show();
    $('.existing-customer-email').hide();
});


