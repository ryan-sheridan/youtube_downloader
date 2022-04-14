# YouTube Downloader

barebones web-based youtube downloader built on python, html, css and js. this project was mainly built around pytube and flask and there is a clone and setup tutorial below. this website is also hosted on youtubeddd.com for testing purposes. more stuff will be added such as a way to get from youtube to my site and automatically download a video. this should be pretty easy in theory if the user just wanted to put ddd infront of the youtube link. the download folder also needs to be fixed as users can download an unlimited amount of videos to my server. banning is another thing that i need to include as i have imported a working fingerprinting library so that will be used to ban users.

## Setup

Clone the Repo and Dive into the sub directory.

`git clone https://github.com/ryan-sheridan/youtube_downloader` \
`cd youtube_downloader`

Create and activate a Python Virtual Enviroment.

`python3 -m venv venv`\
`. venv/bin/activate`

Setup enviroment variables and run the app.

`export FLASK_APP=app.py`\
`flask run`
