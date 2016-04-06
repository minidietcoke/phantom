$(document).on('click', '#addNewRow', function() {
    $("#ghostnamestable").after(
        "<tr><td><form class='form-inline form' action='/save' method='post'>" +
        "<input type='hidden' name='oldghostname' value=''></input>" +
        "<input type='text' name='newghostname''> <a class='editbutton'>Save</a> </td>" +
        "</form></td><td>" +
        $('#username').val() +
        "</td><td>no</td><td><input type = 'checkbox'> </td></tr>");
});

$(document).on('click', '.editbutton', function() {
    if ($(this).text() === 'Save') {
        $(this).parents('form:first').submit();
    }
    $(this)
        .text(function(i, v) {
            return $(this).text() === 'Edit' ? 'Save' : 'Edit';

        })
        .prev('input')
        .prop('readonly', function(i, r) {
            return !r;
        });
});

$(document).on('click', '.deletebutton', function() {
    $(this).parents('form:first').submit();
});