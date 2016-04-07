function getRandomRow() {
    return 'row' + Math.floor((Math.random() * $('.ghostnamelink').length));
}

function getRandomRow(row1) {
    do { row = getRandomRow(); }
    while (row == row1);
    return row;
}

function getRandomRow(row1, row2) {
    do { row = 'row' + Math.floor((Math.random() * $('.ghostnamelink').length)); }
    while (row == row1 || row == row2);
    return row;
}


$(document).ready(function() {
    $('tr.row_ghostname').hide();
    $('.ghostnamelink').click(function() {
        // console.log("Hello");
        $(this).parents('form').submit();
    });

    $('tr.row_ghostname').each(function(i) {
        $(this).attr('id', 'row' + i);
    });
    shuffle();
});

$(document).on('click', $('#shuffle'), function() {
    shuffle();

});

function shuffle() {
    $('tr.row_ghostname').hide();
    var randomrow1 = getRandomRow();
    var randomrow2 = getRandomRow(randomrow1);
    var randomrow3 = getRandomRow(randomrow1, randomrow2);

    $('tr.row_ghostname').each(function(i) {
        if ($(this).attr('id') == randomrow1 || $(this).attr('id') == randomrow2 || $(this).attr('id') == randomrow3) {
            $(this).show();
        }
    });
}