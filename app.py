# app.py

from flask import Flask, request, send_file
from splitter import split
from combiner import combine
import os
import uuid

app = Flask(__name__)
app.config.from_object("config.DevConfig")

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
COMBINED_OUTPUT_FOLDER = app.config['COMBINED_OUTPUT_FOLDER']
DEBUG = app.config['DEBUG']


@app.post("/audio")
def send_audio():
    song_path = save_file('song')
    vocals_path = save_file('vocals')

    file = split(song_path)

    new_song_name = "temp_" + str(uuid.uuid4()) + ".mp3"
    position = request.form["position"]
    new_song_file = combine(vocals_path, file, os.path.join(COMBINED_OUTPUT_FOLDER, new_song_name), position)
    return send_file(new_song_file, download_name=new_song_name)


def save_file(file):
    song = request.files[file]
    save_path = os.path.join(UPLOAD_FOLDER, song.filename)
    song.save(save_path)
    return save_path


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
