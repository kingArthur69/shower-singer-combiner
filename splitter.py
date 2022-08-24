import os

import spleeter.utils.logging
from spleeter.separator import Separator
from spleeter.separator import Codec
from pathlib import Path

separator = Separator("spleeter:2stems")


def split(file):
    # spleeter.utils.logging.configure_logger(True)
    separator.separate_to_file(file, "separated", codec=Codec.MP3)

    return os.getcwd() + "/separated/" + Path(file).stem + "/accompaniment.mp3"
