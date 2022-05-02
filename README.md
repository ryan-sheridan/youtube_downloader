# YouTube Downloader

A barebones youtube downloader site built on html, css, js, a pytube fork, and flask. This project can be built on top of and freely cloned for any sort of use. This won't be updated regularly, only the odd times when I feel like contributing.

## Future Planning

I would like to add some sort of anti-spam mechanism that uses a js fingerprinting library so my server doesn't get backed up with bullshit, along with that, anti-botting or just being able to auto-ban people if my server detects something negative would be great.

### Setup At Home

Clone the Repo and Dive into the sub directory.

`git clone https://github.com/ryan-sheridan/youtube_downloader` \
`cd youtube_downloader`

Create and activate a Python Virtual Environment and install Requirements.

`python3 -m venv venv`\
`. venv/bin/activate`\
`pip install -r requirements.txt`

Setup environment variables and run the app.

`export FLASK_APP=app.py`\
`flask run`
