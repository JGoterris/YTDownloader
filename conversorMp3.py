import moviepy.editor as mp
import os

def conversorMp3(fichero=""):
    if "Downloads" not in os.listdir("./"):
        os.mkdir("./Downloads")
    if fichero != "" and fichero not in os.listdir("./Downloads"):
        os.mkdir("./Downloads/"+fichero)
    files = os.listdir("./Temporal")
    for f in files:
        cutExtension = len(f.split(".")[-1]) + 1
        clip = mp.AudioFileClip("./Temporal/"+f)
        clip.write_audiofile("./Downloads/"+fichero+"/"+f[:-cutExtension]+".mp3")
        os.remove("./Temporal/"+f)
