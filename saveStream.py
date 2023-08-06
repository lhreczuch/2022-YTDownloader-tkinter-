import os
import pydub
import time
import re

def saveAudio(sound,title,win):

    try:
        
        win.label.config(text=f"Próbuję pobrać audio dla: {sound.title}")
        outFile = sound.download()
        
        base, ext = os.path.splitext(outFile)
        mp3File = title + ".mp3"
        os.rename(outFile, mp3File)
        print(mp3File)
        
        pydub.AudioSegment.from_file(mp3File).export(mp3File, format="mp3", bitrate = "128k")
        win.label.config(text=f"pobrałem audio dla: {sound.title}")
        
    
    except FileExistsError:
        win.label.config(text=f"Już wcześniej pobrano audio dla: {sound.title}")
        os.remove(outFile)
        
    # gdyby pojawiły się inne znaki niedozwolone przez system w tytule filmu, oprócz tych które zostały wyeliminowane w youtubeDownload.py:
    except WindowsError as e:
        if e.winerror == 123:
            mp3File = "nieobsługiwany_tytuł" + ".mp3"
            os.rename(outFile, mp3File)

            pydub.AudioSegment.from_file(mp3File).export(mp3File, format="mp3", bitrate = "128k")
            win.label.config(text=f"pobrałem audio dla: {sound.title}")
        else:
            win.label.config(text=f"pobrałem audio dla: {sound.title}")

def saveVideo(video,title,win):

    try:
        win.label.config(text=f"Próbuję pobrać mp4 dla: {video.title}")
        outFile = video.download()
        base, ext = os.path.splitext(outFile)
        videoFile = title + ".mp4"
        os.rename(outFile,videoFile)

        print(videoFile)
        win.label.config(text=f"pobrałem mp4 dla: {video.title}")
            

    except FileExistsError:
        win.label.config(text=f"Już wcześniej pobrano mp4 dla: {video.title}")
        os.remove(outFile)
    except WindowsError as e:
        if e.winerror == 123:
            videoFile = title + ".mp4"
            os.rename(outFile,videoFile)

            print(videoFile)
            win.label.config(text=f"pobrałem mp4 dla: {video.title}")
