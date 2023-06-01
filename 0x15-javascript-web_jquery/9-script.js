$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    success: function (response) {
      $('DIV#hello').html(response.hello);
    }
  });
});
