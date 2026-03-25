#!/usr/bin/node
/* Write a JavaScript script that fetches from
   https://hellosalut.stefanbohacek.com/?lang=fr and displays
   the value of hello from that fetch in the HTML element with id hello.
   The translation of “hello” must be displayed in the HTML element with id hello
   Your script must work when it is imported from the <head> tag
*/
document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});
