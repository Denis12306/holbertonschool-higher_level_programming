#!/usr/bin/node
/* Write a JavaScript script that adds a li element to a list when the user
   clicks on the element with id add_item:
   The new element must be: <li>Item</li> The new element must be added to the
   ul element with class my_list
*/
const addButton = document.querySelector('#add_item');

const list = document.querySelector('.my_list');

addButton.addEventListener('click', function () {
  const newItem = document.createElement('li');

  newItem.textContent = 'Item';

  list.appendChild(newItem);
});
