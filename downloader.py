import requests
import os
import math

def changeReadable(size):
    sizeKB = int(size)/1024
    if int(sizeKB) < 1:
        return str(round(size,2)) , " Bytes"
    elif int(sizeKB) < 1024:
        return str(round(sizeKB,2)) , " KB"
    else:
        sizeMB = sizeKB/1024
        if int(sizeMB) <= 1:
            return str(round(sizeKB,2)) , " KB"
        elif int(sizeMB) < 1024:
            return str(round(sizeMB,2)) , " MB"
        else :
            sizeGB = sizeMB/1024
            return str(round(sizeGB,2)) , " GB"
def download(url,filename):


    url = url
    r = requests.get(url,stream=True)
    filename = "./"+filename
    # finalfile = os.path.join(os.getcwd(),filename)
    totalSize = r.headers['content-length']
    size,ext = changeReadable(totalSize)
    # print(size + ext)
    # print(round(int(totalSize/1024,2) ,"KB"))

    totalDownloaded = 0
    pbar = 0
    with open(filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=2048):
            f.write(chunk)
            totalDownloaded = totalDownloaded + 2048
            percentage = (totalDownloaded/int(totalSize))*100
            
            bars = int(percentage//2)
            if (bars > pbar):
                print("[","#"*bars,"-"*(50-bars),end="]")
                print(int(percentage) ,"% downloaded",end="\r")
                pbar = bars
            
    # print(round(int(percentage),2) ,"% downloaded")



download(url="http://link.testfile.org/150MB",filename="document.zip")
