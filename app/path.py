import os
from pathlib import Path

CUR_DIR = Path.cwd()

def check_file_exists(filename):
    return os.path.isfile(filename)

