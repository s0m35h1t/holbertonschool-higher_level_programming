$(() => {
  $('#btn_translate').click(() => {
    url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, (data, textStatus) => {
      if (textStatus === 'success') {
        $('div#hello').text(data.hello);
      }
    });
  });
});
