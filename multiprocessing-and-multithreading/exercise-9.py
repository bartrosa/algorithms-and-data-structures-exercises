# 9. Implement an image processing application using multiple threads. Every 
# threadprocesses another part of the image.

import threading
from PIL import Image

def process_image_region(file_path, region, results, index):
    """
    Processes a region of the image.
    
    Parameters:
    file_path (str): Path to the image file.
    region (tuple): The region to process (left, upper, right, lower).
    results (list): The list to store the processed region.
    index (int): The index to store the result in the list.
    """
    try:
        with Image.open(file_path) as image:
            cropped_image = image.crop(region)
            processed_image = cropped_image.convert("L")
            results[index] = (region, processed_image)
            print(f"Processed region {region}")
    except Exception as e:
        results[index] = None
        print(f"Failed to process region {region}: {e}")

def main():
    input_image_path = './files/images.jpeg'
    output_image_path = 'output_image.jpg'
    num_threads = 4 

    image = Image.open(input_image_path)
    width, height = image.size
    region_height = height // num_threads

    results = [None] * num_threads
    threads = []

    for i in range(num_threads):
        left = 0
        upper = i * region_height
        right = width
        lower = (i + 1) * region_height if i != num_threads - 1 else height
        region = (left, upper, right, lower)
        
        thread = threading.Thread(
            target=process_image_region, 
            args=(input_image_path, region, results, i)
            )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    output_image = Image.new("L", (width, height))
    for result in results:
        if result is not None:
            region, processed_image = result
            output_image.paste(processed_image, region)

    output_image.save(output_image_path)
    print(f"Processed image saved as {output_image_path}")

if __name__ == "__main__":
    main()
