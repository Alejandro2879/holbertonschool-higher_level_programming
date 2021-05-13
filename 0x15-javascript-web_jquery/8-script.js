$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let counter = 0; counter < data.results.length; counter++) {
    $('list_movies').append('<li>' + data.results[counter].title + '</li>');
  }
});
