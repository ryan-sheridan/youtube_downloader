function returnHome(){
	window.location.href = "/";
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
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
			const downloadLink = document.getElementsByClassName('downloadLink');
			sleep(1000).then(() => {		
				downloadLink[0].style.backgroundColor = '#4CAF50';
				downloadLink[0].innerHTML = 'go to download page';
			})

		}
		console.log(xhr.response)
	};

}

async function value(){
	const fpPromise = import('https://openfpcdn.io/fingerprintjs/v3').then(FingerprintJS => FingerprintJS.load())
	const a = await fpPromise.then(fp => fp.get()).then(result => {return result.visitorId})
	console.log(a)
}

function markInactive(num){
	if(num == 0){
		var downloadLink = document.getElementsByClassName('downloadLink');
		downloadLink[0].style.backgroundColor = '#7a7a7a';
		downloadLink[0].innerHTML = 'loading ...';
		redirectToSite();
	} if (num == 1) {
		var downloadLink = document.getElementsByClassName('downloadLink');
		downloadLink[0].style.backgroundColor = '#7a7a7a';
		downloadLink[0].innerHTML = 'loading ...';
		sleep(1000).then(() => {		
			downloadLink[0].style.backgroundColor = '#4CAF50';
			downloadLink[0].innerHTML = 'download should start now';
		})
	}
}