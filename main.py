import pytube
from customDownload import customDownload
from audioDownload import audioDownload
from videoDownload import videoDownload
from playlistDownload import playlistDownload

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

    option = int(input("1. Download with link\n2. Download with playlist\n0. Exit\n\nOption: "))

    match option:
        case 1:
            print("--------------------------------------------------------")
            link = str(input("Link: "))
            optionLink = int(input("\nFormat:\n1. Video (video and audio in the same file)\n2. Audio\n3. Custom download\n\nOpción: "))
            match optionLink:
                case 1:
                    videoDownload(link)
                    print("\nCompleted!!")
                case 2:
                    audioDownload(link)
                    print("\nCompleted!!")
                case 3:
                    customDownload(link)
                    pyt_data = pytube.YouTube(link)
                    showData(pyt_data)
                    print("Completed!!")
        case 2:
            print("--------------------------------------------------------")
            link = str(input("Link: "))
            optionLink = int(input("\nFormat:\n1. Video (video and audio in the same file)\n2. Audio\n\nOpción: "))
            match optionLink:
                case 1:
                    playlistDownload(link, "video")
                    print("\nCompleted!!")
                case 2:
                    playlistDownload(link, "audio")
                    print("\nCompleted!!")        
        case 0:
            exit()

main()