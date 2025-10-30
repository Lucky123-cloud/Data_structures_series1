import threading
import time

def download_file(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=download_file, args=(f"File {i+1}", i+1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # Wait for all threads
