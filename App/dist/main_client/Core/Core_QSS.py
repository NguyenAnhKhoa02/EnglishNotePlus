import os
from PySide6.QtWidgets import QWidget

FILE_DIR = "\\".join([os.path.dirname(os.path.dirname(__file__)),"UI","qss"])

def getPathFileQSS(nameFile : str):
    return "\\".join([FILE_DIR,nameFile])

def setQSS(widget : QWidget , nameFile : str):
    with open(getPathFileQSS(nameFile),"r") as f:
        _style = f.read()
        widget.setStyleSheet(_style)