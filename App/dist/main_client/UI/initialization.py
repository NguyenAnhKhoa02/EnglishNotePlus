from Core.Core_UI import *
from Core.Core_Image import *
from Core.Core_QSS import *
from Dal.Database import init
from Bus.Word import ListWords
from Bus.Grammar import ListGrammar
from Bus.Collection import ListCollection
from Core.FrameWork import *
from Core.Core_Image import *

import sys

class initialization(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Initialization")
        self.setWindowIcon(QPixmap(getPathFileImage("icon.png")))
        
        self.g_BOOL_Connection = True
        
        __l_QL_imageInit = QLabel(self)

        __l_QI_image = QImage(getPathFileImage("initialization.png"))
        __l_QL_imageInit.setFixedSize(__l_QI_image.size())
        __l_QL_imageInit.setPixmap(QPixmap.fromImage(__l_QI_image))

        self.setFixedSize(__l_QL_imageInit.size())
        self.show()
        
        self.g_BOOL_Connection = FrameCheckConnection(self,"https://console.firebase.google.com/project/englishnoteplus/overview",True).g_BOOL_connect
        if not self.g_BOOL_Connection:
            return
        
        init()
        # mixer.init()
        self.g_listWords = ListWords()
        self.g_ListGrammars = ListGrammar()
        self.g_ListCollections = ListCollection()
        
        self.deleteLater()