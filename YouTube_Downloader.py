from pytube import *
import os

error_msg = "An error has occured, please try again"
link = input("video link")

youtube = YouTube(link)
title = youtube.title
filetype=input("Audio or Video? ")

if filetype.lower()=="video":
    try:
        print("Starting download of ",youtube.title)
        youtube.streams.get_highest_resolution().download()
        print("Saved to",os.getcwd())
    except:
        print(error_msg)
        
elif filetype.lower()=="audio":
    try:
        print("Starting download of ",youtube.title)
        audio = youtube.streams.filter(only_audio=True).first()
        audio.download()
        print("Saved to",os.getcwd())
        oldfile=title+".mp4"
        newfile=title+".mp3"
        os.rename(oldfile,newfile)
    except:
        print("an error has occured, make sure you are connected to the internet and try again")
