import os
import argparse
import subprocess
import shutil
from pathlib import Path

if __name__ == '__main__':
    MUSIC_DEST = 
    VIDEO_DEST = 

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-t', '--type', help="aud or vid?", type=str)
    PARSER.add_argument('-u', '--url', help="link?", type=str)

    ARGS = PARSER.parse_args()

    TEMP_PATH = os.getcwd() + '/temp'
    os.mkdir(TEMP_PATH)
    os.chdir(TEMP_PATH)

    if ARGS.type == 'music':
        # this will download a video an convert to just mp3
        URL = ARGS.url
        DEST_ROOT = MUSIC_DEST
        subprocess.call(["youtube-dl", "-i", "--extract-audio",
                         "--audio-format", "mp3", "--yes-playlist",
                         "-o", "%(playlist_title)s/%(title)s.%(ext)s",
                         URL])
    if ARGS.type == 'video':
        # this actually downloads the videos in a playlist to seperate files.
        URL = ARGS.url
        DEST_ROOT = VIDEO_DEST
        subprocess.call(["youtube-dl", "-i", "-f"
                         "mp4", "-o", "%(playlist_title)s/%(title)s.%(ext)s",
                         URL])

    PLAYLIST = os.listdir(".")
    DEST = DEST_ROOT + "/" + PLAYLIST[0]
    shutil.move(PLAYLIST[0], DEST)
    os.rmdir(TEMP_PATH)
