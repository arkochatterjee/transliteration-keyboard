$('textarea').on('input', function() {
    text = $('textarea').val();
    $('div').html(text);
  });