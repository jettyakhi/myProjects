from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print('Title :',yt.title)

yd = yt.streams.get_highest_resolution()

yd.download(r'C:\Users\jetty\OneDrive\Desktop\20501a1244\project (video downloader)')