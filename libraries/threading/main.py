import threading


lock = threading.Lock()

shared_resource = 0

def update_resource():
    global shared_resource
    with lock:
        local_copy = shared_resource
        local_copy += 1
        shared_resource = local_copy
        print(f"Updated resource to {shared_resource}")

threads = []
for _ in range(10):
    thread = threading.Thread(target=update_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final value of shared resource: {shared_resource}")
