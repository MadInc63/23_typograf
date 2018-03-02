$(function(){
  $('#send_button').click(function(){
    var ugly_text = $("#text").val();
    event.preventDefault();
    $.ajax({
      url: '/action',
      data: {
        'text': ugly_text
      },
      type: 'POST',
      success: function(response){
        $('#beautiful_text').html(response);
      },
      error: function(error){
      alert('Что-то пошло не так...');
      }
    });
  });
});