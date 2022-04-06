# YouTube Downloader

This is a barebones YouTube downloader built on Python, HTML, CSS, and Javascript, It is built upon Flask and this can be ran upon any webserver. This is a barebones project of mine to try get my head around front and back-end web development, more support will be added to the backend regarding video to audio conversion with the ffmpeg module. The project will stay open source as I build it up day by day, feel free to clone and rebrand this. Theres a few more things that need to be checked off in regards to mp4 downloading, sending files back to the user, and better mobile support.

## Setup

Clone the Repo and Dive into the sub directory.

`git clone https://github.com/ryan-sheridan/youtube_downloader` **
**
`cd youtube_downloader`**
**

Create and activate a Python Virtual Enviroment.

`python3 -m venv venv`**
**
`. venv/bin/activate`**
**

Setup enviroment variables and run the app.

`export FLASK_APP=main.py`**
**
`flask run`**
**
