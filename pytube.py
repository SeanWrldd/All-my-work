from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube("https://www.youtube.com/watch?v=lzQpS1rH3zI&pp=ygUOZmFzdCBqdWljZXdybGQ%3D&ab_channel=JuiceWRLDVEVO")

print("Title: ", yt.title)
print("View: ", yt.views)
yd = yt.streams.get_highest_resolution()

yd.download(input, "D:/python projects/Youtube safe location bot")

