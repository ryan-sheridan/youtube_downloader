function redirectToSite(){
	const videoId = document.getElementById('videoidbox').value;
	const videoType = document.getElementById('videotype').value;
	window.location.href = "/youtubedl/" + videoId + "/" + videoType;
}