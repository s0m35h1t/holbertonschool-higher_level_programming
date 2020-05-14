$(() => {
  function translate () {
    url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, (data, textStatus) => {
      if (textStatus === 'success') {
        $('#hello').text(data.hello);
      }
    });
  }
  $('#btn_translate').click(translate);
  $('#language_code').keypress((event) => {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
