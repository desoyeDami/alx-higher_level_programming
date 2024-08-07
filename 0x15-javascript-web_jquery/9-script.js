
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .done(function (data) {
    $('#hello').text(data.hello);
  });
