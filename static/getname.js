$(function() {
    $('#entryerror').hide();
});

$(document).on('click', '#submitbutton', function(e) {
    firstname = $('[name="firstname"]').val();
    surname = $('[name="surname"]').val();
    if (firstname.length === 0 || surname.length === 0) {
        e.preventDefault();
        $('#entryerror').text("Names cannot be empty");
        $('#entryerror').show();
    } else {
        e.preventDefault();
        var letters = /^[A-Za-z]+$/;
        console.log(firstname.match(letters));
        if (!firstname.match(letters) || !surname.match(letters)) {
            e.preventDefault();
            $('#entryerror').text("Incorrect name format, please make sure only letters are present");
            $('#entryerror').show();
        }
        else {
            $(this).parents('form:first').submit();
        }
    }

});