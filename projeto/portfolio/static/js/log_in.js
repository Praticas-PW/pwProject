document.addEventListener('DOMContentLoaded', function() {
    var messageElement = document.querySelector('.warning');
    
    if (messageElement) {
        messageElement.style.display = 'block';
        
        setTimeout(function() {
            messageElement.style.display = 'none';
        }, 5000);
    }
});