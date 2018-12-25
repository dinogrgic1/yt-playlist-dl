import os
import time
import youtube_dl

playlist = # INSERT YOUR PLAYLIST HERE


# klasa za logganje downloada
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Preuzimanje zavrseno, prebacivanje u mp3...')
    if d['status'] == 'downloading':
        # (TODO) : progress bar
        pass
    
# opcije za skidanje pjesama
ydl_opts = {
    'playlist': True,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '/pjesme/%(title)s.%(ext)s',
    'logger': MyLogger(),
    'progress_hooks': [my_hook]
}

if __name__ == '__main__':
    lista = [playlist]
    print('Started downloading : ', lista[0])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(lista)



