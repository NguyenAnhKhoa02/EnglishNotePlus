import os
from playsound import playsound

SOUND_DIR = "\\".join([os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"sound"])

def getPathFileAudio(nameFile : str) -> str:
    return "\\".join([SOUND_DIR,nameFile.lower()])

def play(nameFile : str) -> None:  
    playsound(getPathFileAudio(nameFile),block=False)