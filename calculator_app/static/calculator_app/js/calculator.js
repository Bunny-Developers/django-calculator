document.addEventListener('DOMContentLoaded', function() {
    const expressionInput = document.getElementById('expression');
    const resultDisplay = document.getElementById('result');
    const buttons = document.querySelectorAll('.btn');
    
    let currentExpression = '';
    let calculated = false;

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const value = this.value;
            
            if (calculated && !['+', '-', '*', '/', 'C', 'DEL'].includes(value)) {
                currentExpression = '';
                calculated = false;
            }

            if (value === '=') {
                calculateResult();
                calculated = true;
            } else if (value === 'C') {
                currentExpression = '';
                resultDisplay.textContent = '0';
            } else if (value === 'DEL') {
                currentExpression = currentExpression.slice(0, -1);
            } else {
                currentExpression += value;
            }

            if (value !== '=' && value !== 'C') {
                expressionInput.value = currentExpression;
            }
        });
    });

    function calculateResult() {
        if (currentExpression === '') return;
        
        fetch('/calculate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: `expression=${encodeURIComponent(currentExpression)}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDisplay.textContent = 'Error';
            } else {
                resultDisplay.textContent = data.result;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDisplay.textContent = 'Error';
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});