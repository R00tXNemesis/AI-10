import requests
import threading

URL = "🪓"  # Endpoint upload
FILE_PATH = "large_file.bin"  # File dummy 1GB+

def send_large_file():
    with open(FILE_PATH, "rb") as f:
        requests.post(URL, files={"file": f})

threads = []
for _ in range(10):  # Ubah angka ini untuk meningkatkan beban
    thread = threading.Thread(target=send_large_file)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()