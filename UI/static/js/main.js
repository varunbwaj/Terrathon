// main.js
document.getElementById('message-input').addEventListener('submit', function(event) {
    event.preventDefault();  // prevent form submission

    var message = document.getElementById('message').value;
    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<p><strong>You:</strong> ' + message + '</p>';
    document.getElementById('message').value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send message to server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/send-message", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function() {
        if (this.status == 200) {
            var response = JSON.parse(this.response);
            chatBox.innerHTML += '<p><strong>Server:</strong> ' + response.message + '</p>';
            chatBox.scrollTop = chatBox.scrollHeight;
        } else {
            console.error(xhr);
        }
    };
    xhr.send(JSON.stringify({message: message}));
});

document.getElementById('play-button').addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/play-response", true);
    xhr.onload = function() {
        if (this.status == 200) {
            console.log(this.response);
        } else {
            console.error(xhr);
        }
    };
    xhr.send();
});

// Trigger photo take
document.getElementById("send").addEventListener("click", function() {
    context.drawImage(video, 0, 0, 640, 480); // copy frame from <video>
    canvas.toBlob(upload, "image/jpeg");  // convert to file and execute function upload
});
// Elements for taking the snapshot
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var stream = null;

// Add event listener to open dashboard button
document.getElementById('open-dashboard').addEventListener('click', function() {
    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Not adding { audio: true } since we only want video now
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(mediaStream) {
            //video.src = window.URL.createObjectURL(stream);
            video.srcObject = mediaStream;
            video.play();
            stream = mediaStream;  // store the stream
        });
    }

    // Show the modal
    $('#dashboard').modal('show');
});

// Add event listener to modal close event
$('#dashboard').on('hide.bs.modal', function (e) {
    if (stream) {
        let tracks = stream.getTracks();  // get all tracks from the stream
        tracks.forEach(function(track) {
            track.stop();  // stop each track
        });
        video.srcObject = null;  // remove the stream from the video
    }
});

document.getElementById('upload-button').addEventListener('click', function() {
    var fileInput = document.getElementById('file-input');
    var file = fileInput.files[0];
    if (file) {
        upload(file);
    } else {
        console.log('No file selected');
    }
});

function upload(file) {
    // create form and append file
    var formdata =  new FormData();
    formdata.append("snap", file);
    
    // create AJAX requests POST with file
    var xhr = new XMLHttpRequest();
    // xhr.open("POST", "{{ url_for('upload') }}", true);
    xhr.open("POST", "/upload", true);
    xhr.onload = function() {
        if(this.status = 200) {
            console.log(this.response);
        } else {
            console.error(xhr);
        }
        alert(this.response);
    };
    xhr.send(formdata);
}

document.getElementById('open-dashboard').addEventListener('click', function() {
    document.getElementById('dashboard').style.display = 'block';
});

(function ($) {
    "use strict";

    // Navbar on scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.navbar').fadeIn('slow').css('display', 'flex');
        } else {
            $('.navbar').fadeOut('slow').css('display', 'none');
        }
    });


    // Smooth scrolling on the navbar links
    $(".navbar-nav a, .btn-scroll").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 1500, 'easeInOutExpo');
            
            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });


    // Scroll to Bottom
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.scroll-to-bottom').fadeOut('slow');
        } else {
            $('.scroll-to-bottom').fadeIn('slow');
        }
    });


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Gallery carousel
    $(".gallery-carousel").owlCarousel({
        autoplay: false,
        smartSpeed: 1500,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            },
            1200:{
                items:5
            }
        }
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
    });
    
})(jQuery);

