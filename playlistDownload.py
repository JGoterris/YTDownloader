import pytube
import videoDownload
import audioDownload
import os

def playlistDownload(link, typeFile):
    playlist = pytube.Playlist(link)
    if typeFile == "video":
        print("--------------------------------------------------------")
        fileExtension = int(input("Extension:\n1. mp4\n2. webm\n\nOption: "))
        match fileExtension:
            case 1:
                try:
                    for url in playlist.video_urls:
                        videoDownload.mp4VideoDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "video")
            case 2:
                try:
                    for url in playlist.video_urls:
                        videoDownload.webmVideoDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "video")

    elif typeFile == "audio":
        print("--------------------------------------------------------")
        fileExtension = int(input("Extension:\n1. mp4\n2. webm\n3. mp3 (always works)\n\nOption: "))
        match fileExtension:
            case 1:
                try:
                    for url in playlist.video_urls:
                        audioDownload.mp4AudioDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "audio")
            case 2:
                try:
                    for url in playlist.video_urls:
                        audioDownload.webmAudioDownload(url,playlist.title)
                except:
                    print("\n////////////////////////////////////////////////////////////////////////")
                    print("Extensión no disponible, pruebe con otra o descargue de forma individual")
                    print("////////////////////////////////////////////////////////////////////////\n")
                    playlistDownload(link, "audio")
            case 3:
                for url in playlist.video_urls:
                        audioDownload.mp3AudioDownload(url,playlist.title)
                os.rmdir("./Temporal")
