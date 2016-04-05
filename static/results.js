$(document).ready(function() {
    $('.ghostnamelink').click(function() {
        // console.log("Hello");
        $(this).parents('form').submit();
    });
});