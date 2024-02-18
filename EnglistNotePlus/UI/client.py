from Core.Core_UI import *
from Core.Core_Audio import *
from Core.Core_QSS import *
from Core.Core_Image import *
from Core.FrameWork import FrameCheckConnection
from UI.controllbar import Controllbar
from UI.initialization import initialization
from UI.chat import Chat
from UI.note import Note
from UI.search import Search
from Bus.Word import ListWords
from Dal.Database import init

import sys

class Client(QMainWindow):
    """UI OF CLIENT

        STRUCTURE OF CLIENT:
        =================== CONTROLLBAR =======================
        | BUTTON  ||             SHOWING CONTENT              |
        | OPTIONS ||                                          |
        |         ||                                          |            
        |         ||                                          |
        |         ||                                          |

    Args:
        QMainWindow (_type_): _description_
    """
    
    def __init__(self, g_listWords, g_listGrammars, g_listCollections) -> None:
        super().__init__()
        
        (width,height) = QGuiApplication.primaryScreen().size().toTuple()
        
        self.setWindowTitle("EnglishNotePlus")
        self.setWindowIcon(QPixmap(getPathFileImage("icon.png")))
        
        # SET SIZE OF CLIENT
        self.setFixedSize(width * 90 / 100,
                          height * 90 / 100)
        self.move(width / 2 - width * 90 / 100 / 2,
                  height / 2 - height * 90 / 100 / 2)
        
        # SET QSS
        setQSS(self,"client.qss")

        # SET FLAGS
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowMinimizeButtonHint)
        
        # CRATE FRAME TO CONTAINER ALL WIDGETS THAT ARE SHOWED INTO CLIENT
        self.__l_F_container = QFrame(self)
        self.__l_F_container.setFixedSize(self.size())

        self.__l_QVL_layoutContainer = QVBoxLayout()
        self.__l_QVL_layoutContainer.setContentsMargins(0,0,0,0)
        self.__l_QVL_layoutContainer.setSpacing(0)
        self.__l_QVL_layoutContainer.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_F_container.setLayout(self.__l_QVL_layoutContainer)
        
        """CONTROLLBAR
        """
        self.__l_QW_containerControllbar = QWidget()
        self.__l_QW_containerControllbar.setFixedSize(self.__l_F_container.width(),
                                                      self.__l_F_container.height() * 4 / 100)
        self.g_CONTROLLBAR_controllbar = Controllbar(self.__l_QW_containerControllbar)
        self.g_CONTROLLBAR_controllbar.setClient(self)
        self.__l_QVL_layoutContainer.addWidget(self.__l_QW_containerControllbar)
        
        """DISPLAY
        """
        self.__l_QHL_layoutDisplay = QHBoxLayout()
        self.__l_QHL_layoutDisplay.setContentsMargins(0,0,0,0)
        self.__l_QHL_layoutDisplay.setSpacing(0)
        self.__l_QHL_layoutDisplay.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.__l_QVL_layoutContainer.addLayout(self.__l_QHL_layoutDisplay)
        
        """BUTTON OPTIONS
        """
        self.__l_QVL_buttonOptions = QVBoxLayout()
        self.__l_QVL_buttonOptions.setContentsMargins(0,0,0,0)
        self.__l_QVL_buttonOptions.setSpacing(0)
        self.__l_QVL_buttonOptions.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QHL_layoutDisplay.addLayout(self.__l_QVL_buttonOptions)
        
        self.g_QPB_chat = QPushButton("Chat")
        self.g_QPB_chat.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_chat.setCursor(QPixmap(getPathFileImage("chat.png")).scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.g_QPB_chat.setObjectName("optionButton")
        self.__l_QVL_buttonOptions.addWidget(self.g_QPB_chat)
        
        self.g_QPB_search = QPushButton("Search")
        self.g_QPB_search.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_search.setObjectName("optionButton")
        self.g_QPB_search.setCursor(QPixmap(getPathFileImage("search.png")).scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.__l_QVL_buttonOptions.addWidget(self.g_QPB_search)
        
        self.g_QPB_note = QPushButton("Note")
        self.g_QPB_note.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_note.setObjectName("optionButton")
        self.g_QPB_note.setCursor(QPixmap(getPathFileImage("note.png")).scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.__l_QVL_buttonOptions.addWidget(self.g_QPB_note)
        
        """SHOWING CONTENTS
        """
        self.g_QW_showingContent = QWidget()
        self.g_QW_showingContent.setFixedSize(self.width() * 93.5 / 100,
                                              self.height() * 96.2 / 100)
        
        """CONTENT SHOWING
        """
        self.g_C_chat = Chat(self.g_QW_showingContent, g_listWords, g_listGrammars, g_listCollections)
        self.g_N_note = Note(self.g_QW_showingContent, g_listWords, g_listGrammars, g_listCollections)
        self.g_N_note.hide()
        self.g_S_search = Search(self.g_QW_showingContent, g_listWords, g_listGrammars, g_listCollections)
        self.g_S_search.hide()
        
        self.__l_QHL_layoutDisplay.addWidget(self.g_QW_showingContent)
        
        self.__l_F_container.setFixedSize(self.size())
        
        CoreClient(self)

class CoreClient:
    """HANDLE AND RESOLVE EVENT IN CLASS "Client"
    """
    
    def __init__(self, client : Client) -> None:
        self.__l_CLIENT_client = client
        self.checkPressedButton()
        
        self.__l_STR_current = self.__l_CLIENT_client.g_C_chat.objectName()
        
        """CONTROLLBAR
        """
        self.__l_CLIENT_client.g_CONTROLLBAR_controllbar.g_QPB_minimize.clicked.connect(self.__l_CLIENT_client.showMinimized)
        self.__l_CLIENT_client.g_CONTROLLBAR_controllbar.g_QPB_exit.clicked.connect(sys.exit)
        
        self.__l_CLIENT_client.g_QPB_chat.clicked.connect(lambda: self.__grapRender(self.__l_CLIENT_client.g_C_chat))
        self.__l_CLIENT_client.g_QPB_search.clicked.connect(lambda: self.__grapRender(self.__l_CLIENT_client.g_S_search))
        self.__l_CLIENT_client.g_QPB_note.clicked.connect(lambda: self.__grapRender(self.__l_CLIENT_client.g_N_note))
    
    def __grapRender(self, showWidget : QWidget):
        """RENDER WIDGETS IN G_QW_SHOWINGCONTENT
            hideWidget : the widget will be hide
            showWidget : the widget will be display

        Args:
            hideWidget (QWidget): _description_
            showWidget (QWidget): _description_
        """
        
        # CHECK CONNECTION
        if not FrameCheckConnection(showWidget,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_STR_current = showWidget.objectName()
        
        match self.__l_STR_current:
            case "Chat":
                self.__l_CLIENT_client.g_N_note.hide()
                self.__l_CLIENT_client.g_S_search.hideSearch()

            case "Search":
                self.__l_CLIENT_client.g_S_search.g_CS_core.updateList()
                self.__l_CLIENT_client.g_N_note.hide()
                self.__l_CLIENT_client.g_C_chat.hide()
                
            case "Note":
                self.__l_CLIENT_client.g_C_chat.hide()
                self.__l_CLIENT_client.g_S_search.hideSearch()
            
        if self.__l_STR_current.__eq__("Search"):
            showWidget.showSearch()
        else:
            showWidget.show()
        self.checkPressedButton()
        
    def checkPressedButton(self):
        """
        CHECK TO CHANGE ALPHA OF BUTTON
        
        IF NOTE IS SHOWING:
            g_QPB_chat will be set "alpha" is 0.5
            g_QPB_note will be set "alpha" is 0
            
        IF CHAT IS SHOWING:
            g_QPB_chat will be set "alpha" is 0
            g_QPB_note will be set "alpha" is 0.5
        """
        
        if not self.__l_CLIENT_client.g_C_chat.isHidden():
            self.__l_CLIENT_client.g_QPB_chat.setStyleSheet("background-color : rgba(0,0,0,0.5)")
            self.__l_CLIENT_client.g_QPB_note.setStyleSheet("background-color : rgba(0,0,0,0)")
            self.__l_CLIENT_client.g_QPB_search.setStyleSheet("background-color : rgba(0,0,0,0)")
        elif not self.__l_CLIENT_client.g_S_search.isHidden():
            self.__l_CLIENT_client.g_QPB_search.setStyleSheet("background-color : rgba(0,0,0,0.5)")
            self.__l_CLIENT_client.g_QPB_chat.setStyleSheet("background-color : rgba(0,0,0,0)")
            self.__l_CLIENT_client.g_QPB_note.setStyleSheet("background-color : rgba(0,0,0,0)")
        elif not self.__l_CLIENT_client.g_N_note.isHidden():
            self.__l_CLIENT_client.g_QPB_note.setStyleSheet("background-color : rgba(0,0,0,0.5)")
            self.__l_CLIENT_client.g_QPB_chat.setStyleSheet("background-color : rgba(0,0,0,0)")
            self.__l_CLIENT_client.g_QPB_search.setStyleSheet("background-color : rgba(0,0,0,0)")