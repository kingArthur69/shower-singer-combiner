import spleeter.utils.logging
from spleeter.separator import Separator
# from spleeter.utils.logging import enable_logging
import os

if __name__ ==  '__main__':
    spleeter.utils.logging.configure_logger(True)
    file = os.getcwd() + "/download/audio2.mp3"
    print("Calling spleeter " + file)
    separator = Separator("spleeter:2stems")
    separator.separate_to_file(file, os.path.join(os.getcwd(), "separated"))
    print("Called spleeter")
