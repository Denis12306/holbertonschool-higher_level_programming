#!/usr/bin/node
/* Write a JavaScript script that adds the class red to the header element
   when the user clicks on the tag with id red_header
*/
const trigger = document.querySelector('#red_header');

const header = document.querySelector('header');

trigger.addEventListener('click', function () {
  header.classList.add('red');
});
