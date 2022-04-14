function returnHome(){
	window.location.href = "/";
}

function createWarningMessage(warningMessage){
	var warningElement = document.getElementById("warningElement");
	warningElement.innerHTML = warningMessage
}

function redirectToSite(){
	const videoId = document.getElementById('videoidbox').value;
	const videoType = document.getElementById('videotype').value;
	let xhr = new XMLHttpRequest();
	xhr.open('get', '/youtubedl/' + videoId + '/' + videoType);
	xhr.send();

	xhr.onload = function() {
		if (xhr.response[0] == 0){
			document.write('')
			document.write(xhr.response.substring(1))
		} else {
			createWarningMessage(xhr.response.slice(0, -1))
		}
		console.log(xhr.response)
	};

}

async function value(){
	const fpPromise = import('https://openfpcdn.io/fingerprintjs/v3').then(FingerprintJS => FingerprintJS.load())
	const a = await fpPromise.then(fp => fp.get()).then(result => {return result.visitorId})
	console.log(a)
}