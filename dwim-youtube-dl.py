import os
import sys
import argparse
import subprocess
import logging

logger = logging.getLogger(__name__)


def main(*args, **kwargs):
    """Main program entrypoint
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t', help="music or video?", type=str)
    parser.add_argument('--url', '-u', help="link?", type=str)
    parser.add_argument("--debug", "-d", action="store_true")
    parser.add_argument("--logfile", "-l", type=str)  # should this be File?
    parsed = parser.parse_args()
    loglevel = logging.INFO

    if parsed.debug:
        loglevel = logging.DEBUG
    logger.setLevel(loglevel)

    if parsed.logfile:
        fh = logging.FileHandler(parsed.logfile)
        fh.setLevel(loglevel)
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(fh)
    logger.debug("Configured logging, nice")

    temp_path = os.getcwd() + '/temp'
    if os.path.exists(temp_path):
        os.chdir(temp_path)
    else:
        os.mkdir(temp_path)
        os.chdir(temp_path)

    if parsed.type == 'music':
        # this will download a video an convert to just mp3
        url = parsed.url
        subprocess.call(["youtube-dl", "-i", "--extract-audio",
                         "--audio-format", "mp3", "--yes-playlist",
                         "-o", "%(playlist_title)s/%(title)s.%(ext)s",
                         url])
    if parsed.type == 'video':
        # this actually downloads the videos in a playlist to seperate files.
        url = parsed.url
        subprocess.call(["youtube-dl", "-i", "-f"
                         "mp4", "-o", "%(playlist_title)s/%(title)s.%(ext)s",
                         url])


if __name__ == '__main__':
    sys.exit(main(*sys.argv))
