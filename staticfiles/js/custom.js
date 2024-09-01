document.addEventListener('DOMContentLoaded', function() {
    const popup = document.getElementById('popup');
    const form = document.querySelector('.contact-form');
    const submitButton = document.getElementById('submit-button');
    const spinner = document.getElementById('spinner');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        submitButton.disabled = true;  // Disable the button
        spinner.style.display = 'inline-block';  // Show the spinner

        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                popup.classList.add('show');
                form.reset();
            } else {
                alert('There was an error sending your message. Please try again.');
            }
        })
        .finally(() => {
            submitButton.disabled = false;  // Re-enable the button
            spinner.style.display = 'none';  // Hide the spinner
        });
    });

    function closePopup() {
        popup.classList.remove('show');
    }

    window.closePopup = closePopup;  // Make closePopup function globally accessible



});


document.addEventListener('DOMContentLoaded', function() {
    var navLinks = document.querySelectorAll('.nav-link');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        // Check if the navbar is currently expanded
        if (navbarCollapse.classList.contains('show')) {
          // If it's expanded, trigger the collapse
          navbarCollapse.classList.remove('show');
          navbarCollapse.classList.add('collapsing');
          setTimeout(function() {
            navbarCollapse.classList.remove('collapsing');
            navbarCollapse.classList.add('collapse');
          }, 300); // Match the duration with your CSS transition
        }
      });
    });
  });