import sys
from file_scanner import scan_directory
from transcriber import transcribe_file
from file_monitor import start_monitoring

def main(directory):
    # Scan existing files in the directory
    media_files = scan_directory(directory)
    for file_path in media_files:
        transcribe_file(file_path)
    
    # Start real-time monitoring
    start_monitoring(directory)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory>")
    else:
        main(sys.argv[1])