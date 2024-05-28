# 5. Use `multithreading` to monitor different system resources simultaneously,
# such as CPU, memory and disk usage. Update results every second.

import threading
import psutil
import time

def monitor_cpu():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(1)

def monitor_memory():
    while True:
        memory_info = psutil.virtual_memory()
        print(f"Memory Usage: {memory_info.percent}%")
        time.sleep(1)

def monitor_disk():
    while True:
        disk_usage = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_usage.percent}%")
        time.sleep(1)

def main():
    cpu_thread = threading.Thread(target=monitor_cpu)
    memory_thread = threading.Thread(target=monitor_memory)
    disk_thread = threading.Thread(target=monitor_disk)

    cpu_thread.start()
    memory_thread.start()
    disk_thread.start()

    cpu_thread.join()
    memory_thread.join()
    disk_thread.join()

if __name__ == "__main__":
    main()
