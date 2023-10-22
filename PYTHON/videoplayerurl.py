# importing vlc module
import vlc,time
from pytube import YouTube
from pynput.keyboard import Key, Listener
from voicerecog_module import *
speed=2.25
def pause(key):
    global speed
    if key== Key.space:
        if player.is_playing()==True:
            player.pause()
        else :
            player.play()
    if format(key)[1]=='>'or format(key)[1]=='<':
        if format(key)[1]=='>':
            speed+=0.25
        else :
            speed-=0.25
        player.pause()
        player.set_rate(speed)
        print ("speed is ",speed)
        player.play()
    if key==Key.right or key==Key.left:
        if key==Key.right:
            speed+=0.5
        else:
            speed-=0.5
        player.pause()
        player.set_rate(speed)
        print ("speed is ",speed)
        player.play()
    if key == Key.delete:
        exit()
def pausecheck():
    with Listener(on_press = pause) as l2: 
        l2.join()
                
def play(url):
    # url of the video
# creating pafy object of the video
    global speed
    try:
	# object creation using YouTube
	# which was imported in the beginning
        video = YouTube(url)
    except:
        print("Connection Error") #to handle exception
        exit()
    audio=video.streams.get_audio_only()
# getting best stream
    best = video.streams.get_by_resolution("720p")
#print(best.resolution)
# creating vlc media player object
    media = vlc.MediaPlayer(best.url)
    global player
#media = vlc.MediaPlayer("temp_video.avi")
    media_audio=vlc.MediaPlayer(audio.url)
# start playing video
    #Speech("hello sir how are you")
    Speech("what shall i play audio or video :- ")
    a=voice()
    Speech("playing the track with title "+video.title)
    
    if a=="audio":
        player=media_audio
        Speech("got it playing audio")
    else:
        player=media 
        Speech("playing Video for you. tell playback speed")
        try:
            s=float(voice()) 
            player.set_rate(s)
            speed=s
        except:
            player.set_rate(speed)
    
    player.play()  
    player.set_fullscreen(1)
    pausecheck()
if __name__ == '__main__':
    play(input('enter the url :- '))