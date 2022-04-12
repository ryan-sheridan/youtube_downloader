import pytube
from flask import Flask, render_template, send_file
import os
import time
import hashlib

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

	if v_type == 'mp4':
		yt = YouTube('http://youtube.com/watch?v={}'.format(v_id))
		video = yt.streams.get_highest_resolution().download('dl/')
	if v_type == 'mp3':
		yt = YouTube('http://youtube.com/watch?v={}'.format(v_id))
		video = yt.streams.filter(only_audio=True).first().download('dl/')

	timestamp = str(time.time())

	hash_object = hashlib.md5(timestamp.encode())
	hashedts = hash_object.hexdigest()[0:7]
	filename = '{}.{}'.format(hashedts, v_type)

	destinationFilePath = 'dl/' + filename
	defaultFilePath = 'dl/' + yt.streams.get_highest_resolution().default_filename
	os.rename(defaultFilePath, destinationFilePath)

	return yt.title, filename, yt.thumbnail_url

@app.route("/")
def index(warningMessage=0):
	# return index if no subdir is called
	if warningMessage == 0:
		warningMessage = ''
	else:
		warningMessage = 'There was an error with the link you entered, please check formatting and try again.'
	return render_template('index.html', warningMessage=warningMessage)

@app.route("/youtubedl//<v_type>")
def throwNoLinkError(v_type):
	return index(warningMessage=1)

@app.route("/youtubedl/<v_id>/<v_type>")
def rd_download(v_id, v_type):
	# if redirect to download page, get video id and type and call download function
	title, filename, thumbnail_url = download_video(v_id, v_type)
	filenames.append(filename)
	print(filenames)
	return render_template('youtubedl.html', filename=filename, title=title, v_type=v_type, thumbnail_url=thumbnail_url)

@app.route("/d/<filename>")
def download_file(filename):
	filenames.remove(filename)
	try:
		path = 'dl/' + filename
		return send_file(path)
	finally:
		clean_dl(filename)

if __name__ == '__main__':
	app.run()
