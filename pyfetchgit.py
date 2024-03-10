from zipfile import ZipFile
import requests
import os


user = ""   # Github Username
repo = ""   # Repository Name
filename = ""   # Zipfile to download


url = f"https://github.com/{user}/{repo}/releases/latest/download/{filename}"   # Latest download link

def downloadlink(url):
    filename = url.split("/")[-1]
    with open(filename, "wb") as file:
        response = requests.get(url)
        file.write(response.content)


print("🚀 Downloading..")

if url.endswith(".zip"):
    downloadlink(url)
else:
    url = url + ".zip"
    downloadlink(url)
    filename += ".zip"


print("| Done.")

with ZipFile(filename, 'r') as zObject:
    print("| Extracting .zip file...")
    zObject.extractall(path="data")

os.remove(filename)
print("🚀 Installation completed.")
