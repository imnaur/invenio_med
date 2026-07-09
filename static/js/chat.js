document.addEventListener('DOMContentLoaded', function() {
    const chatToggle = document.getElementById('chat-toggle');
    const chatBox = document.getElementById('chat-box');
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const messagesContainer = document.getElementById('chat-messages');

    // Логика открытия/закрытия чата
    chatToggle.addEventListener('click', function() {
        chatBox.classList.toggle('is-open'); // Добавляет/удаляет класс .is-open
    });

    // Функция для отрисовки сообщений
    function appendMessage(sender, text) {
        const msgDiv = document.createElement('div');
        msgDiv.style.padding = "5px 0";
        msgDiv.innerHTML = `<b>${sender}:</b> ${text}`;
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    // Слушатель отправки
    sendBtn.addEventListener('click', function() {
        const message = userInput.value;
        if (!message.trim()) return;

        appendMessage('Вы', message);
        userInput.value = '';

        fetch('/chatbot/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: 'message=' + encodeURIComponent(message)
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('InvenioBot', data.reply);
        })
        .catch(err => {
            appendMessage('InvenioBot', 'Ошибка соединения.');
        });
    });
});