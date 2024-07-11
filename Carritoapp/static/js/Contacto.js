document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();

        fetch(contactForm.action, {
            method: 'POST',
            body: new FormData(contactForm),
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert(data.message); // Muestra una alerta con el mensaje de éxito
                contactForm.reset(); // Limpia el formulario después de enviarlo correctamente
            } else {
                alert(data.message); // Muestra una alerta con el mensaje de error, si lo hay
            }
        })
        .catch(error => {
            console.error('Error al enviar el formulario:', error);
            alert('Hubo un problema al enviar el formulario. Por favor, inténtalo de nuevo más tarde.');
        });
    });
});