import pytube
from customDownload import customDownload
import audioDownload

def downloadWithLink(link):
    pyt = pytube.YouTube(link)
    print("Downloading...")
    pyt.streams.first().download("./Downloads")
    showData(pyt)

def downloadWithFile():
    file = str(input("\nFile (def: links.txt): "))
    print()
    if file == "" or file.replace(" ","") == "":
        with open("links.txt") as f:
            for line in f:
                downloadWithLink(line)
    else:
        with open(file) as f:
            for line in f:
                downloadWithLink(line)

def showData(pyt):
    print("\n------------------------------------------------------------")
    print(f"Title: {pyt.title}")
    print("------------------------------------------------------------")
    print(f"Description:\n{pyt.description}")
    print("------------------------------------------------------------")
    print(f"Duration: {str(pyt.length)} seconds")
    print("------------------------------------------------------------\n")

def main():
    print("""
    
 __     _________ _____                      _                 _           
 \ \   / /__   __|  __ \                    | |               | |          
  \ \_/ /   | |  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \   /    | |  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |     | |  | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|     |_|  |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                        
                                                        Made by @JGoterris
    """)

    option = int(input("1. Download with link\n2. Download with playlist\n3. Download with file\n0. Exit\n\nOption: "))

    match option:
        case 1:
            print("--------------------------------------------------------")
            link = str(input("Link: "))
            optionLink = int(input("\nFormat:\n1. Video\n2. Audio\n3. Custom download\n\nOpción: "))
            match optionLink:
                case 1:
                    downloadWithLink(link)
                case 2:
                    audioDownload.audioDownload(link)
                    print("\nCompleted!!")
                case 3:
                    customDownload(link)
                    pyt_data = pytube.YouTube(link)
                    showData(pyt_data)
                    print("Completed!!")
        case 2:
            playlistLink = str(input("Link: "))
        case 3:
            downloadWithFile()
            print("Completed!!")
            
        case 0:
            exit()

main()