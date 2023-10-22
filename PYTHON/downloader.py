# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://youtu.be/wt2WGqJkISk"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

d_video = yt.streams.get_highest_resolution()
print(yt.streams.filter(res="2160p"))
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
else:
    print('Task Completed!')