
//JS16AK11HI2022L
openerp.Key_shortcuts = function (jQuery) {
//    $(document).bind('keydown', 'f2', function assets() {
////        window.location.href = window.location.protocol + '//' + window.location.host + '/' + 'web?debug=1#view_type=form&model=account.invoice&menu_id=441&action=395';
//        window.location.href = window.location.protocol + '//' + window.location.host + '/' + 'web?debug=1#view_type=form&model=account.invoice&action=395';
//    setTimeout(function(){
//    $('button.oe_button.oe_form_button_create').click();
//}, 4000)
//    });

//    HARSHA'S CODE
$.shortcut = function(key, callback, args) {
    $(document).keydown(function(e) {
        if(!args) args=[]; // IE barks when args is null
        if(e.keyCode != 49 && (e.keyCode == key.charCodeAt(0) || e.keyCode == key)) {
            callback.apply(this, args);
            return false;
        }
    });
};

$.shortcut('113', function() {
    window.location.assign("/web#view_type=form&model=account.invoice&action=399");
        $('.oe_list_add').trigger('click');
        $('.oe_form_button_create').trigger('click');

//    $('.oe_form_button_create').each(function() {
//        if($(this).parents('div:hidden').length == 0){
//            $(this).trigger('click');
//        }
//    });
//
//	$('.oe_list_add').each(function() {
//            if($(this).parents('div:hidden').length == 0){
//                $(this).trigger('click');
//            }
//        });
});

$.shortcut('114', function() {
	$('.css_hiworth').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});

$.shortcut('115', function() {
	$('.btn_txt').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});



$.shortcut('121', function() {
	$('.oe_form_button_save').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
	$('.css_print').each(function() {
		if($(this).parents('div:hidden').length == 0){
			$(this).trigger('click');
		}
	});
});

//console.log('f3');

//    ROBIN'S CODE
    $( document ).ready(function() {
    //For adding class to html tag
    var newClass = window.location.href;
    newClass = newClass.substring(newClass.indexOf('&action=') + 1).replace('=', '-num');
    $('html').addClass(newClass);
    // For adding tr to supplier table

    });
    $("button.oe_button.oe_list_add").on('click', function() {
        $('.oe_notebook_page.ui-tabs-panel.ui-widget-content .abhi_custom .oe_form_field .oe_view_manager_wrapper .oe_view_manager_body .oe_view_manager_view_list table.oe_list_content > tbody:last-child').append('<tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr>');
    });

//    $( "oe_button oe_form_button_create" ).click(function() {
    $("button.oe_button.oe_form_button_create").on('click', function() {
//    alert( "Handler for .click() called." );
      $('.oe_notebook_page.ui-tabs-panel.ui-widget-content .abhi_custom .oe_form_field .oe_view_manager_wrapper .oe_view_manager_body .oe_view_manager_view_list table.oe_list_content > tbody:last-child').append('<tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr><tr>...</tr>');

    });

//END

};

//jQuery(function($) {
//
//  $(window).load(function() {
//
//    var $gal = $(".oe_notebook_page"),
//      galW = $gal.outerWidth(true),
//      galSW = $gal[0].scrollWidth,
//      wDiff = (galSW / galW) - 1, // widths difference ratio
//      mPadd = 60, // Mousemove Padding
//      damp = 20, // Mousemove response softness
//      mX = 0, // Real mouse position
//      mX2 = 0, // Modified mouse position
//      posX = 0,
//      mmAA = galW - (mPadd * 2), // The mousemove available area
//      mmAAr = (galW / mmAA); // get available mousemove fidderence ratio
//
//    $gal.mousemove(function(e) {
//      mX = e.pageX - $(this).offset().left;
//      mX2 = Math.min(Math.max(0, mX - mPadd), mmAA) * mmAAr;
//    });
//
//    setInterval(function() {
//      posX += (mX2 - posX) / damp; // zeno's paradox equation "catching delay"
//      $gal.scrollLeft(posX * wDiff);
//    }, 10);
//
//  });
//
//});