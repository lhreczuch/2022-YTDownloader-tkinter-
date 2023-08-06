import bs4
import requests
import pytube
import getStream
import saveStream 
import os.path


def downloadingSound(video,win):
    # Pobieram tytuł filmu przed pobraniem, by potem sprawdzić czy już go nie ma w folderze
    response = requests.get(video.watch_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
          
    title = title.split(' - YouTube')[0]

    # eliminuję znaki któe mogę spowodować WinError 123:
    title = title.replace('<', '').replace('>', '').replace('*', '').replace('?', '').replace(':', '').replace('"', '').replace('|', '').replace('.', '').replace(',','').replace('/','')

    
    filePath = str(os.path.join(os.getcwd(), title)+".mp3")
            
    # sprawdzam czy plik o wyżej pobranym tytule istnieje:
    if os.path.exists(filePath):
        win.label.config(text=f"Ten plik już istnieje: {title}")

    # jeśli pliku nie ma - pobieram mp3
    elif not os.path.exists(filePath):   
        try:
            sound = getStream.getAudio(video,win,title)
            saveStream.saveAudio(sound,title,win)
                            
        except pytube.exceptions.AgeRestrictedError:
            win.label.config(text=f"Nie mogę pobrać: {title} AGE RESTRICTED")

        except Exception as e:
            win.label.config(text=f"Nie mogę pobrać: {title} Nieokreślony błąd: {e}")

def downloadingVideo(video,win):
    # Pobieram tytuł filmu przed pobraniem, by potem sprawdzić czy już go nie ma w folderze
    response = requests.get(video.watch_url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    title = title.split(' - YouTube')[0]
    
    # eliminuję znaki któe mogę spowodować WinError 123:
    title = title.replace('<', '').replace('>', '').replace('*', '').replace('?', '').replace(':', '').replace('"', '').replace('|', '').replace('.', '').replace(',','')


    filePath = str(os.path.join(os.getcwd(), title)+".mp4")
            
    # sprawdzam czy plik o wyżej pobranym tytule istnieje:
    if os.path.exists(filePath):
        win.label.config(text=f"Ten plik już istnieje: {title}")

    # jeśli pliku nie ma - pobieram mp4 z najwyższą rozdzielczością
    elif not os.path.exists(filePath):   
        try:
                   
            videoToGet = getStream.getVideo(video,win,title)
            saveStream.saveVideo(videoToGet,title,win)
                            
        except pytube.exceptions.AgeRestrictedError:
            win.label.config(text=f"Nie mogę pobrać: {title} \nAGE RESTRICTED")

        except:
            win.label.config(text=f"Nie mogę pobrać: {title} \nNieokreślony błąd")

# główne funkcje:

def youtubeDownload(link,win):
    win.label3.config(text="") # Every time function starts running clear label3

    if "playlist" in link or "index" in link: # Checking if link is a playlist
        chosenPlaylist = pytube.Playlist(link)
        for video in chosenPlaylist.videos:
            downloadingSound(video,win)
        win.label3.config(text="Możesz wprowadzić kolejny link")
                       
    else:
        # Pobieram tytuły filmów za pomocą funkcji get w bibliotece requests przed pobraniem filmu
        video = pytube.YouTube(link)
        downloadingSound(video,win)
        win.label3.config(text="Możesz wprowadzić kolejny link")

def youtubeVideoDownload(link,win):
    win.label3.config(text="") # Every time function starts running clear label3
    if "playlist" in link or "index" in link:
        chosenPlaylist = pytube.Playlist(link)
          
        for video in chosenPlaylist.videos:
            downloadingVideo(video,win)
        win.label3.config(text="Możesz wprowadzić kolejny link")
                    
    else: 

        video = pytube.YouTube(link)
        downloadingVideo(video,win)      
        win.label3.config(text="Możesz wprowadzić kolejny link") # after every finished function call - edit label3


        