import os
import whisper
from utils import load_processed_files, save_processed_file

def transcribe_file(file_path):
    """
    Transcribes an audio/video file using OpenAI's Whisper model and saves the transcription as a text file.
    The transcription is generated in English by default.
    """
    # Load the list of already processed files
    processed_files = load_processed_files()
    
    # Skip if the file has already been processed
    if file_path in processed_files:
        print(f"Skipping already processed file: {file_path}")
        return
    
    # Load the Whisper model (use "base" for faster processing, "large" for higher accuracy)
    model = whisper.load_model("base")
    
    # Transcribe the file in English
    print(f"Transcribing file: {file_path}")
    result = model.transcribe(file_path, language="en")  # Set language to English
    transcription = result["text"]
    
    # Save the transcription as a text file with UTF-8 encoding
    output_path = os.path.splitext(file_path)[0] + ".txt"
    with open(output_path, "w", encoding="utf-8") as f:  # Use UTF-8 encoding
        f.write(transcription)
    
    # Mark the file as processed
    save_processed_file(file_path)
    print(f"Transcription saved: {output_path}")

def transcribe_chunk(chunk_path):
    """
    Helper function to transcribe a single chunk of an audio/video file in English.
    """
    model = whisper.load_model("base")
    result = model.transcribe(chunk_path, language="en")  # Set language to English
    transcription = result["text"]
    
    # Save the transcription as a text file with UTF-8 encoding
    output_path = os.path.splitext(chunk_path)[0] + ".txt"
    with open(output_path, "w", encoding="utf-8") as f:  # Use UTF-8 encoding
        f.write(transcription)
    
    print(f"Transcription saved: {output_path}")