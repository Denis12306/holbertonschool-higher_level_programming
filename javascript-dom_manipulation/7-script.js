#!/usr/bin/node
/*  Write a JavaScript script that fetches and lists the title for all movies
    by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
    All movie titles must be list in the HTML ul element with id list_movies
    You must use the Fetch API.
*/
const listElement = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listElement.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
