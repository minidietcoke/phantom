$(document).on('click', '#addNewRow', function() {
    $("#ghostnamestable").after(
        "<tr><td><form class='form-inline form' action='/save' method='post'>" +
        "<input type='hidden' name='oldghostname' value=''></input>" +
        "<input type='text' name='newghostname''></input> <a class='editbutton'>Save</a> </td>" +
        "</form></td><td>" +
        $('#username').val() +
        "</td><td>no</td><td></td><td><span class='glyphicon glyphicon-remove deletebutton'></span></td></tr>");
});
var oldghostname;

$(document).on('click', '.editbutton', function(e) {
    if ($(this).text() === 'Edit') {
        oldghostname = $(this).parent().find("input[type=text]").val();
        console.log(oldghostname);
    } else if ($(this).text() === 'Save') {
        if ($(this).parent().find("input[type=text]").val().length === 0) {
            e.preventDefault();
            $(this).parent().find("input[type=text]").val(oldghostname);
            console.log(oldghostname);
            alert("Ghostname cannot be empty");
        } else {
            $(this).parents('form:first').submit();
        }
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