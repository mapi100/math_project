document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#prime-form');
  const numberInput = document.querySelector('#number');
  const resultMessage = document.querySelector('.result-message');

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const number = numberInput.value;
    fetch('/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ number: number })
    })
      .then(response => response.json())
      .then(data => {
        resultMessage.textContent = `The closest prime number to ${number} is ${data.closest_prime}.`;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  });
});
