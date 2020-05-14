$(() => {
  $('#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(() => {
    const ul = $('ul.my_list li');
    if (ul.length > 0) {
      ul[ul.length - 1].remove();
    }
  });
  $('#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
