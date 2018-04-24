// Create a clone of the menu, right next to original.
$('.top-menu').addClass('original').clone()
.insertAfter('.top-menu').addClass('cloned')
.css('position','fixed').css('top','0')
.css('margin-top','0').css('z-index','500')
.removeClass('original').hide();

scrollIntervalID = setInterval(stickIt, 10);
cartOnToplID = setInterval(cartOnTop, 10);


function stickIt() {

  var orgElementPos = $('.original').offset();

  if (orgElementPos && $(window).scrollTop() >= (orgElementPos.top)) {
    // scrolled past the original position; now only show the cloned, sticky element.

    // Cloned element should always have same left position and width as original element.     
    orgElement = $('.original');
    coordsOrgElement = orgElement.offset();
    leftOrgElement = coordsOrgElement.left;  
    widthOrgElement = orgElement.css('width');
    $('.cloned').css('left',leftOrgElement+'px').css('top',0).css('width',widthOrgElement).show();
    $('.original').css('visibility','hidden');
    $(".agileits_header").css({ 
      'position' : 'fixed', 
      'top' : $('.cloned').css('height'),
    });
    // console.log($('.cloned').css('height'));
  } else {
    // not scrolled past the menu; only show the original menu.
    $('.cloned').hide();
    $('.original').css('visibility','visible');
    $(".agileits_header").css({ 'position' : 'relative', 'top' : 0 });
  }
}

function cartOnTop() {
  var cart = $('#PPMiniCart');

  var mainRowOffset = $('.main-row').offset();

  if (cart && mainRowOffset) {

    if ($(window).scrollTop() < mainRowOffset.top - 100) {
      cart.css({
        'position' : 'absolute',
        'top' : mainRowOffset.top
      });
    } else {
      cart.css({
        'position' : 'fixed',
        'top' : '100px'
      });
    }
  }
}








