import pytube
from flask import Flask, render_template, send_file
import os
import time
import hashlib

app = Flask(__name__)

def download_video(v_id, v_type):
	from pytube import YouTube

	onlyAudio = False # check what file extension the end user wants
	if (v_type == 'mp3'):
		onlyAudio = True
	if (v_type == 'mp4'):
		onlyAudio == False

	# this is the temp filename base, used for searching for the downloaded file later.
	timestamp = str(time.time())
	hash_object = hashlib.md5(timestamp.encode())
	md5timestamp = hash_object.hexdigest()

	# download the file into the destination path (/dl)
	yt = YouTube('https://www.youtube.com/watch?v=' + v_id)
	video = yt.streams.filter(only_audio=onlyAudio).first()
	destination = 'dl'
	ext = '.' + v_type
	out_file = video.download(output_path=destination, filename=md5timestamp + ext)

	filename = md5timestamp + ext
	return yt.title, filename, yt.thumbnail_url


@app.route("/")
def index():
	# return index if no subdir is called
    return render_template('index.html')

@app.route("/youtubedl/<v_id>/<v_type>")
def rd_download(v_id, v_type):
	# if redirect to download page, get video id and type and call download function
	title, filename, thumbnail_url = download_video(v_id, v_type)
	return render_template('youtubedl.html', filename=filename, title=title, v_type=v_type, thumbnail_url=thumbnail_url)

@app.route("/d/<filename>")
def download_file(filename):
	# this is kind of broken right now, mp4s dont work.
	path = 'dl/' + filename
	return send_file(path)

if __name__ == '__main__':
	app.run()
