import pytube
from flask import Flask, render_template, send_file
import os
import time
import hashlib
import re

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def clean_dl(filename):
	os.remove('dl/{}'.format(filename))
	dir_name = "dl/"
	t = os.listdir(dir_name)
	for item in t:
	    if item.endswith(".js"):
	        os.remove(os.path.join(dir_name, item))

def download_video(v_id, v_type):
	from pytube import YouTube

	try:
		yt = YouTube('http://youtube.com/watch?v={}'.format(v_id))
		error_code = 0
	except pytube.exceptions.RegexMatchError:
		error_code = 1
		return 0, 0, 0, error_code

	if v_type == 'mp4':
		try:
			video = yt.streams.get_highest_resolution().download('dl/')
		except pytube.exceptions.VideoUnavailable:
			error_code = 3
			return 0, 0, 0, error_code
	if v_type == 'mp3':
		try:
			video = yt.streams.filter(only_audio=True).first().download('dl/')
		except pytube.exceptions.VideoUnavailable:
			error_code = 3
			return 0, 0, 0, error_code

	timestamp = str(time.time())

	hash_object = hashlib.md5(timestamp.encode())
	hashedts = hash_object.hexdigest()[0:7]
	filename = '{}.{}'.format(hashedts, v_type)

	destinationFilePath = 'dl/' + filename
	defaultFilePath = 'dl/' + yt.streams.get_highest_resolution().default_filename
	os.rename(defaultFilePath, destinationFilePath)

	return yt.title, filename, yt.thumbnail_url, error_code

@app.route("/")
def index(errorCode=0):
	if errorCode == 0:
		warningStr = ''
		return render_template('index.html')
	if errorCode == 1:
		warningStr = 'there has been a problem trying to process the video url/id, please check if the input is correct and try again.'
		return warningStr + str(errorCode)
	if errorCode == 2:
		warningStr = 'please enter a video id or video url into the input box.'
		return warningStr + str(errorCode)
	if errorCode == 3:
		warningStr = 'this video does not exist, please try again with a valid link.'
		return warningStr + str(errorCode)
	if errorCode == 4:
		warningStr = 'please stop.'
		return warningStr + str(errorCode)


@app.route("/youtubedl/<v_type>")
def throwNoLinkError(v_type):
	return index(errorCode=2)

@app.route("/youtubedl/<v_id>/<v_type>")
def rd_download(v_id, v_type):
	# if redirect to download page, get video id and type and call download function
	title, filename, thumbnail_url, error_code = download_video(v_id, v_type)

	if error_code == 1:
		return index(errorCode=error_code)
	if error_code == 2:
		return index(errorCode=error_code)
	if error_code == 3:
		return index(errorCode=error_code)
	else:
		return render_template('youtubedl.html', filename=filename,
												 title=title,
												 v_type=v_type,
												 thumbnail_url=thumbnail_url,
												 error_code=error_code)

@app.route("/d/<filename>")
def download_file(filename):
	try:
		path = 'dl/' + filename
		return send_file(path)
	finally:
		clean_dl(filename)

if __name__ == '__main__':
	app.run()
