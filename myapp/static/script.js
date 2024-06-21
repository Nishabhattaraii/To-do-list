document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('todo-form');
    const input = document.getElementById('todo-input');
    const list = document.getElementById('todo-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const text = input.value.trim();
        if (text !== '') {
            const li = document.createElement('li');
            li.textContent = text;
            list.appendChild(li);
            input.value = '';
        }
    });
});
