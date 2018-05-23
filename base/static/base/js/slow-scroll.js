document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        console.log(this.getAttribute('href'));

        href = this.getAttribute('href')

        $('.banner').addClass('invisible');

        setTimeout(function() {
        	location.href = href;
        }, 300);

        setTimeout(function() {
        	$('.banner').removeClass('invisible');
        }, 300);

        

        // document.querySelector(this.getAttribute('href')).scrollIntoView({
        //     behavior: 'smooth',
        //     block: 'start'
        // });
    });
});