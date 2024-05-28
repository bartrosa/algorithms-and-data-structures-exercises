# 6. Use `multithreading` to asynchronously make multiple HTTP requests to 
# different ones servers. Use the `requests` module.

import threading
import requests

def fetch_url(url, results, index):
    """
    Fetch the content from the given URL and store the result.
    
    Parameters:
    url (str): The URL to fetch.
    results (list): List to store the result.
    index (int): Index to store the result in the list.
    """
    try:
        response = requests.get(url)
        results[index] = response.text
        print(f"Successfully fetched {url}")
    except requests.RequestException as e:
        results[index] = None
        print(f"Failed to fetch {url}: {e}")

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
        "https://jsonplaceholder.typicode.com/posts/5"
    ]

    results = [None] * len(urls)

    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch_url, args=(url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for i, result in enumerate(results):
        if result:
            print(f"Result from {urls[i]}: {result[:100]}...")
        else:
            print(f"Failed to retrieve result from {urls[i]}")

if __name__ == "__main__":
    main()
