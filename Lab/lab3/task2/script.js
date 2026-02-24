
const form = document.getElementById('todoForm');
const input = document.getElementById('taskInput');
const list = document.getElementById('taskList');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const text = input.value.trim();
  if (text === '') return;

  const li = document.createElement('li');
  li.className = 'item';

  const left = document.createElement('div');
  left.className = 'left';

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';

  const span = document.createElement('span');
  span.textContent = text;

  checkbox.addEventListener('change', function () {
    span.classList.toggle('done', checkbox.checked);
  });

  const delBtn = document.createElement('button');
  delBtn.type = 'button';
  delBtn.textContent = 'Delete';
  delBtn.addEventListener('click', function () {
    list.removeChild(li);
  });

  left.appendChild(checkbox);
  left.appendChild(span);

  li.appendChild(left);
  li.appendChild(delBtn);

  list.appendChild(li);
  input.value = '';
});