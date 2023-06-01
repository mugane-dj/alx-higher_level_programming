$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (response) {
  $(document).ready(function () {
    $('DIV#character').html(response.name);
  });
}).fail(function (xhr, status, error) {
  console.log(error);
});
