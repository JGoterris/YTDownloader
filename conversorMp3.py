import moviepy.editor as mp
import os

def conversorMp3(carpeta=""):
    if "Downloads" not in os.listdir("./"):
            os.mkdir("./Downloads")
    files = os.listdir("./Temporal")
    for f in files:
        cutExtension = len(f.split(".")[-1]) + 1
        clip = mp.AudioFileClip("./Temporal/"+f)
        clip.write_audiofile("./Downloads/"+f[:-cutExtension]+".mp3")
        os.remove("./Temporal/"+f)
    
    os.rmdir("./Temporal")
