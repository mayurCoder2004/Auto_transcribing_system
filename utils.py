import os

def load_processed_files():
    if os.path.exists("processed_files.txt"):
        with open("processed_files.txt", "r") as f:
            return set(f.read().splitlines())
    return set()

def save_processed_file(file_path):
    with open("processed_files.txt", "a") as f:
        f.write(file_path + "\n")