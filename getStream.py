import pytube


def getAudio(s,win,title):
    
    win.label.config(text=f"Próbuję uzyskać dźwięk: {title}")
    result = "keyerror"
    while result == "keyerror":
        try:
            sound = s.streams.filter(only_audio=True).first()
            
            result = None
            return sound
        except KeyError:
            result = "keyerror"

def getVideo(s,win,title):
    win.label.config(text=f"Próbuję uzyskać video: {title}")
    result = "keyerror"
    while result == "keyerror":
        try:
            video = s.streams.get_highest_resolution()
            
            result = None
            return video
        except KeyError:
            result = "keyerror"