import pytube
import videoDownload
import audioDownload

def playlistDownload(link, typeFile):
    playlist = pytube.Playlist(link)
    if typeFile == "video":
        print("--------------------------------------------------------")
        fileExtension = int(input("Extension:\n1. mp4\n2. webm\n\nOption: "))
        match fileExtension:
            case 1:
                try:
                    for url in playlist.video_urls:
                        print(f"Downloading {pytube.YouTube(url).title}...")
                        videoDownload.mp4VideoDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "video")
            case 2:
                try:
                    for url in playlist.video_urls:
                        print(f"Downloading {pytube.YouTube(url).title}...")
                        videoDownload.webmVideoDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "video")

    elif typeFile == "audio":
        print("--------------------------------------------------------")
        fileExtension = int(input("Extension:\n1. mp4\n2. webm\n\nOption: "))
        match fileExtension:
            case 1:
                try:
                    for url in playlist.video_urls:
                        print(f"Downloading {pytube.YouTube(url).title}...")
                        audioDownload.mp4AudioDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "audio")
            case 2:
                try:
                    for url in playlist.video_urls:
                        print(f"Downloading {pytube.YouTube(url).title}...")
                        audioDownload.webmAudioDownload(link,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "audio")
