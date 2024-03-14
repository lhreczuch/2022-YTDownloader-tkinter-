"""
YOUTUBE DOWNLOADER
Korzysta głównie z biblioteki pytube.

Pozwala na pobieranie dźwięku lub mp4 z filmów z youtube. 
Oparty na prostocie i minimalizmie jednocześnie szybko spełnia swoje funkcje.
Stworzony z graficznym interfejsem. Pobiera pliki do folderu w którym akurat znajduje się program.

Sprawdza przed rozpoczęciem procesu pobierania czy plik był wcześniej pobierany korzystając z bibliotek requests oraz bs4.

Filmy pobierane w najwyższej dostępnej rozdzielczości - ustawione na sztywno
Audio pobierane jako pierwszy stream ONLY_AUDIO.


Kod z tego pliku zawiera interfejs graficzny aplikacji.

"""


import threading
from tkinter import *
from tkinter import ttk
import youtubeDownload
import youtubeDownload
from moviepy.editor import *

def show_menu(event):
    try:
        text.tk.call("tk_popup", menu, event.x_root, event.y_root)
    finally:
        menu.grab_release()

def get_input(outputType):
    link = text.get(1.0, "end-1c")
    if outputType == "music":
        threading.Thread(target=youtubeDownload.youtubeDownload, args=(link,win)).start()
    elif outputType == "video":
        threading.Thread(target=youtubeDownload.youtubeVideoDownload, args=(link,win)).start()
    
# defining window 'win'
win = Tk()
win.wm_attributes('-toolwindow', 'True')
win.geometry("800x220")
win.title("Youtube audio downloader")
win.protocol("WM_DELETE_WINDOW", win.quit)

label2 = Label(win, text="Wklej tu link playlisty lub filmu z youtube", font=('Calibri 15 bold'))
label2.pack()


text = Text(win, width=100, height=2)
text.tag_configure("tag_name", justify='center')
text.insert(END, "")
text.pack()


firstButton = ttk.Button(win, text="Pobierz audio", command=lambda: get_input("music"))
firstButton.pack()

secondButton = ttk.Button(win, text="Pobierz video", command=lambda: get_input("video"))
secondButton.pack()

menu = Menu(win, tearoff=0)
menu.add_command(label="Wklej", command=lambda: text.event_generate("<Control-v>"))
text.bind("<Button-3>", show_menu)

label = Label(win, text="", font=('Calibri 15'))
label.pack()

label3 = Label(win, text="", font=('Calibri 15'))
label3.pack()

win.label = label
win.label3 = label3

win.mainloop()


#test
#test2

#test3




