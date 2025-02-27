import os
import glob

# Supported file formats
SUPPORTED_FORMATS = ["*.mp3", "*.wav", "*.mp4", "*.mkv", "*.mov", "*.flv", "*.aac", "*.m4a"]

def scan_directory(directory):
    """
    Scans a directory and its subdirectories for supported audio and video files.
    """
    media_files = []
    for format in SUPPORTED_FORMATS:
        media_files.extend(glob.glob(os.path.join(directory, "**", format), recursive=True))
    return media_files