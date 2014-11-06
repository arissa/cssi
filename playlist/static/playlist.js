console.log('wat')

function HandleKeyPress(e) {
	var titleValue = $('#title').val();
	if (titleValue) {
		$('#submit').prop('disabled',false);
	}
	else {
		$('#submit').prop('disabled',true);

	}
}
function Main() {
	$('#title').keyup(HandleKeyPress);
}

$(document).ready(Main);