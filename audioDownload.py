import pytube

def mp4AudioDownload(link):
    pyt = pytube.YouTube(link)
    pyt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download("./Downloads")

def webmAudioDownload(link):
    pyt = pytube.YouTube(link)
    pyt.streams.filter(only_audio=True, file_extension='webm').order_by('abr').desc().first().download("./Downloads")

def audioDownload(link):
    print("--------------------------------------------------------")
    fileExtension = int(input("Extension:\n1. mp4\n2. webm\nOption: "))
    match fileExtension:
        case 1:
            mp4AudioDownload(link)
        case 2:
            webmAudioDownload(link)