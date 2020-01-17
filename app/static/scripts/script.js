var $data_form = $('#data_form');

function hiddenInputWithValue(value)
{
    return '<input type="hidden" name="action_name" value="' + value + '">';
}

$('#button_1').click(() => {
    let content = '<input name="movie_title" type="text" placeholder="tytuł filmu">';
    content += hiddenInputWithValue('Aktorzy z filmu');
    $data_form.html(content);
});

$('#button_2').click(() => {
    let content = '<input name="runtime" type="number" placeholder="czas trwania">';
    content += hiddenInputWithValue('Czas trwania');
    $data_form.html(content);
});

$('#button_3').click(() => {
    let content = '<input name="director_name" type="text" placeholder="reżyser">';
    content += hiddenInputWithValue('Filmy danego reżysera');
    $data_form.html(content);
});

$('#button_4').click(() => {
    let content = '<input name="actor_name" type="text" placeholder="aktor">';
    content += hiddenInputWithValue('Filmy z aktorem');
    $data_form.html(content);
});

$('#button_5').click(() => {
    let content = '<input name="actor_name" type="text" placeholder="aktor">';
    content += '<input name="genre_name" type="text" placeholder="gatunek">';
    content += hiddenInputWithValue('Filmy z aktorem w gatunku');
    $data_form.html(content);
});

$('#button_6').click(() => {
    let content = '<input name="genre_name" type="text" placeholder="gatunek">';
    content += hiddenInputWithValue('Gatunek');
    $data_form.html(content);
});

$('#button_7').click(() => {
    let content = '<input name="rating" type="number" placeholder="rating">';
    content += hiddenInputWithValue('Rating');
    $data_form.html(content);
});

$('#button_8').click(() => {
    let content = '<input name="year" type="number" placeholder="rok">';
    content += hiddenInputWithValue('Rok produkcji');
    $data_form.html(content);
});

$('#button_9').click(() => {
    $data_form.html(hiddenInputWithValue('Wszyscy aktorzy'));
});

$('#button_10').click(() => {
    $data_form.html(hiddenInputWithValue('Wszyscy reżyserzy'));
});

$('#button_11').click(() => {
    $data_form.html(hiddenInputWithValue('Wszystkie filmy'));
});

$('#button_12').click(() => {
    $data_form.html(hiddenInputWithValue('Wszystkie gatunki'));
});

$('#button_13').click(() => {
    $data_form.html(hiddenInputWithValue('Wszystkie wytwórnie filmowe'));
});