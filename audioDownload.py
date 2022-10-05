import pytube
from conversorMp3 import conversorMp3

def mp4AudioDownload(link, fichero=""):
    pyt = pytube.YouTube(link)
    try:
        pyt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download("./Downloads"+"/"+fichero)
    except:
        print("\n/////////////////////////////////////////")
        print("Extensión no disponible, pruebe con otra")
        print("/////////////////////////////////////////\n")
        audioDownload(link)

def webmAudioDownload(link, fichero=""):
    pyt = pytube.YouTube(link)
    try:
        pyt.streams.filter(only_audio=True, file_extension='webm').order_by('abr').desc().first().download("./Downloads"+"/"+fichero)
    except:
        print("\n/////////////////////////////////////////")
        print("Extensión no disponible, pruebe con otra")
        print("/////////////////////////////////////////\n")
        audioDownload(link)

def mp3AudioDownload(link, fichero=""):
    pyt = pytube.YouTube(link)
    pyt.streams.filter(only_audio=True).order_by('abr').desc().first().download("./Temporal")
    conversorMp3(fichero)
    

def audioDownload(link):
    print("--------------------------------------------------------")
    fileExtension = int(input("Extension:\n1. mp4\n2. webm\n3. mp3 (always works)\n\nOption: "))
    match fileExtension:
        case 1:
            mp4AudioDownload(link)
        case 2:
            webmAudioDownload(link)
        case 3:
            mp3AudioDownload(link)