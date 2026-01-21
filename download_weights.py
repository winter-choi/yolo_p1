import urllib.request
import os

url = "https://pjreddie.com/media/files/yolov3.weights"
filename = "yolov3.weights"

if os.path.exists(filename):
    print(f"{filename} already exists.")
else:
    print(f"Downloading {filename} from {url}...")
    print("This might take a while depending on your internet connection (approx 237 MB).")
    try:
        urllib.request.urlretrieve(url, filename)
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading file: {e}")
