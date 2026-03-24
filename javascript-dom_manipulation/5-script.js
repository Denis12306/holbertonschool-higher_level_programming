#!/usr/bin/node
/* Write a JavaScript script that updates the text of the header element to
   New Header!!! when the user clicks on the element with id update_header
*/
const updateButton = document.querySelector("#update_header");

const header = document.querySelector("header");

updateButton.addEventListener("click", function () {
  header.textContent = "New Header!!!";
});
