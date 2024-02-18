import os
from PySide6.QtWidgets import (
    QLabel
)

from PySide6.QtGui import (
    QImage, QPixmap
)

IMAGE_DIR = "\\".join([os.path.dirname(os.path.dirname(__file__)),"img"])

def getPathFileImage(nameFile : str) -> str:
    return "\\".join([IMAGE_DIR,nameFile.lower()])