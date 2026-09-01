# 66. Download files using threading

import threading
import urllib.request

def download_file(url, filename):
    print("Downloading:", filename)
    urllib.request.urlretrieve(url, filename)
    print(filename, "downloaded")

t1 = threading.Thread(
    target=download_file,
    args=("https://example.com/file1.pdf", "file1.pdf")
)

t2 = threading.Thread(
    target=download_file,
    args=("https://example.com/file2.pdf", "file2.pdf")
)

t1.start()
t2.start()

t1.join()
t2.join()

print("All downloads completed")