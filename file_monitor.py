from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from transcriber import transcribe_file
from utils import load_processed_files

SUPPORTED_FORMATS = ["*.mp3", "*.wav", "*.mp4", "*.mkv", "*.mov", "*.flv", "*.aac", "*.m4a"]

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory
        self.processed_files = load_processed_files()

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path not in self.processed_files and any(file_path.endswith(ext) for ext in SUPPORTED_FORMATS):
                print(f"New file detected: {file_path}")
                transcribe_file(file_path)
                self.processed_files.add(file_path)

def start_monitoring(directory):
    event_handler = NewFileHandler(directory)
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=True)
    observer.start()
    print(f"Monitoring started for directory: {directory}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()