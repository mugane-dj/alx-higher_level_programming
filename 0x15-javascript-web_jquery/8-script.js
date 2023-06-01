$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  $(document).ready(function () {
    const items = response.results;
    const ul = $('UL#list_movies');
    for (let i = 0; i < items.length; i++) {
      ul.append('<li>' + items[i].title + '</li>');
    }
  });
}).fail(function (xhr, status, error) {
  console.log(error);
});
