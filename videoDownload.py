import pytube

def videoDownload(link):
    print("--------------------------------------------------------")
    fileExtension = int(input("Extension:\n1. mp4\n2. webm\n\nOption: "))
    match fileExtension:
        case 1:
            mp4VideoDownload(link)
        case 2:
            webmVideoDownload(link)

def mp4VideoDownload(link):
    pyt = pytube.YouTube(link)
    try:
        pyt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("./Downloads")
    except:
        print("\n/////////////////////////////////////////")
        print("Extensión no disponible, pruebe con otra")
        print("/////////////////////////////////////////\n")
        videoDownload(link)

def webmVideoDownload(link):
    pyt = pytube.YouTube(link)
    try:
        pyt.streams.filter(progressive=True, file_extension='webm').order_by('resolution').desc().first().download("./Downloads")
    except:
        print("\n/////////////////////////////////////////")
        print("Extensión no disponible, pruebe con otra")
        print("/////////////////////////////////////////\n")
        videoDownload(link)