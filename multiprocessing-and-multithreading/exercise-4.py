# 4. Create a multi-threaded job queue in which several threads process jobs in 
# parallel. The tasks can be anything, such as image processing.

import threading
import queue
import time
import random

def process_image(image_id):
    """
    Simulates image processing by sleeping for a random time.
    
    Parameters:
    image_id (int): ID of the image to process.
    
    Returns:
    str: Result of processing.
    """
    process_time = random.uniform(0.5, 2.0)
    time.sleep(process_time)
    result = f"Image {image_id} processed in {process_time:.2f} seconds"
    return result

def worker(job_queue, result_queue):
    """
    Worker thread function to process jobs from the job queue.
    
    Parameters:
    job_queue (queue.Queue): Queue containing jobs to process.
    result_queue (queue.Queue): Queue to store the results.
    """
    while True:
        try:
            image_id = job_queue.get(timeout=1)
            result = process_image(image_id)
            result_queue.put(result)
            job_queue.task_done()
        except queue.Empty:
            break

def main():
    job_queue = queue.Queue()
    result_queue = queue.Queue()

    num_threads = 4
    image_ids = list(range(10))

    for image_id in image_ids:
        job_queue.put(image_id)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(job_queue, result_queue))
        thread.start()
        threads.append(thread)

    job_queue.join()

    for thread in threads:
        thread.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
