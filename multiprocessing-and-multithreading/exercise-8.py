# 8. Use `multiprocessing` to process multiple audio files simultaneously. 
# Everyone the thread deals with another file and the results are collected 
# together.

import multiprocessing
from pydub import AudioSegment
import os

def process_audio_file(file_path, results, index):
    """
    Process an audio file to calculate its duration.
    
    Parameters:
    file_path (str): Path to the audio file.
    results (list): List to store the result.
    index (int): Index to store the result in the list.
    """
    try:
        audio = AudioSegment.from_file(file_path)
        duration = len(audio) / 1000.0
        results[index] = (file_path, duration)
        print(f"Processed {file_path}: {duration} seconds")
    except Exception as e:
        results[index] = (file_path, None)
        print(f"Failed to process {file_path}: {e}")

def main():
    audio_files = [
        './files/audio1.mp3', 
        './files/audio2.wav', 
        './files/audio3.ogg', 
        './files/audio4.flac'
    ]

    num_files = len(audio_files)
    manager = multiprocessing.Manager()
    results = manager.list([None] * num_files)

    processes = []
    for i, file_path in enumerate(audio_files):
        process = multiprocessing.Process(
            target=process_audio_file, 
            args=(file_path, results, i)
            )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    for file_path, duration in results:
        if duration is not None:
            print(f"File: {file_path}, Duration: {duration} seconds")
        else:
            print(f"File: {file_path}, Duration: Failed to process")

if __name__ == "__main__":
    main()
