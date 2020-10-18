console.log('Hello in contact')
function submithandler(){
    alert('Message sent successfully... Thank you!')
}
$(document).ready(function(){
// Check Radio-box
$(".rating input:radio").attr("checked", false);

$('.rating input').click(function () {
    $(".rating span").removeClass('checked');
    $(this).parent().addClass('checked');
});

$('input:radio').change(
function(){
    var userRating = this.value;
    document.getElementById('crate').value = userRating;
}); 
});

