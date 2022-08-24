from pydub import AudioSegment


def combine(user_vocals, accompaniment, new_song_name, position):
    vocals = AudioSegment.from_file(user_vocals)
    accompaniment = AudioSegment.from_file(accompaniment)

    vocals = vocals + 5
    overlay = vocals.overlay(accompaniment, position=int(position))

    return overlay.export(new_song_name, format="mp3")
