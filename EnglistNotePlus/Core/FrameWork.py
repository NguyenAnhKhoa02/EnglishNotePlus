import PySide6.QtGui
from Core.Core_QSS import QWidget
from Core.Core_UI import *
from Core.Core_UI import QWidget
from Core.Core_Net import *
from Core.Core_Image import *
from Core.Core_QSS import *

import sys

class FrameBackground(QWidget):
    """FRAME USED TO DISABLE ALL CLICK OUT SIDE CURRENT WIDGET

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent : QWidget) -> None:
        thisParent = parent
        while thisParent.__module__.__ne__("UI.client"):
            thisParent = thisParent.parentWidget()
            if thisParent == None:
                thisParent = parent.parentWidget()
                break
        super().__init__(thisParent)
        
        
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        (width,height) = QGuiApplication.primaryScreen().size().toTuple()
        self.move(0,0)
        self.setFixedSize(width * 90 / 100,
                          height * 90 / 100)
        __l_QW_containerColor = QWidget(self)
        __l_QW_containerColor.setStyleSheet(
            "background-color:rgba(219,215,210,0.5)"
        )
        __l_QW_containerColor.setFixedSize(self.size())
        self.show()

class FrameSearch(QWidget):
    """USED TO SEARCHING INTO THE LIST OF OBJECT

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., dataList : list | None = ...) -> None:
        self.__l_QW_parent = parent
        
        super().__init__(self.__l_QW_parent)
        self.setFixedSize(self.__l_QW_parent.size())
        self.__l_LIST_data = dataList
        
        self.__l_QFL_layout = QHBoxLayout()
        self.__l_QFL_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QFL_layout.setSpacing(0)
        self.setLayout(self.__l_QFL_layout)
        
        self.g_QLE_input = QInput()
        self.g_QLE_input.setFixedWidth(self.width() * 99 / 100)
        self.g_QLE_input.setPlaceholderText("Searching...")
        self.g_QLE_input.textChanged.connect(self.__showResults)
        self.__l_QFL_layout.addWidget(self.g_QLE_input)    

        self.__l_QW_results = QWidget()
        self.g_LW_results = QListWidget()
        self.g_LW_results.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.g_LW_results.setStyleSheet(
            """
                background-color:#c0c0c0;
            """
        )
        self.g_LW_results.itemSelectionChanged.connect(self.__findWord)
        self.__l_LIST_results = list()
        
    def updateListSearch(self, newListSearch : list):
        """Change from to list data to new list data

        Args:
            newListSearch (list): list which use to search
        """
        
        self.__l_LIST_data = newListSearch
    
    def __findWord(self):   
        if len(self.g_LW_results.selectedItems()) == 0:
            self.g_I_pos = -1
            return
          
        self.g_I_pos = self.__l_LIST_data.index(self.g_LW_results.selectedItems()[0].text())
        
        self.__l_QW_results.setFixedHeight(0)
    
    def __showResults(self):
        self.__l_LIST_results.clear()
        
        if self.g_QLE_input.text().__ne__(""):
            self.__l_LIST_results = [data for data in self.__l_LIST_data if data.startswith(self.g_QLE_input.text().lower())]
        else:
            self.g_LW_results.clear()
            self.__l_QW_results.setFixedHeight(0)
            return
        
        self.__l_QW_results.setParent(self.__l_QW_parent.parentWidget())
        self.__l_QW_results.setFixedWidth(self.g_QLE_input.width())

        self.g_LW_results.setParent(self.__l_QW_results)
        self.g_LW_results.setFont(QFont("Arial",11))
        self.g_LW_results.setFixedWidth(self.__l_QW_results.width())
        self.g_LW_results.clear()
        self.g_LW_results.addItems(self.__l_LIST_results)
        
        if len(self.__l_LIST_results) < 5:
            self.__l_QW_results.setFixedHeight(25 * len(self.__l_LIST_results))
        else:
            self.__l_QW_results.setFixedHeight(100)
        self.g_LW_results.setFixedHeight(self.__l_QW_results.height())
        
        self.__l_QW_results.move(self.__l_QW_parent.x(),self.__l_QW_parent.y() + self.g_QLE_input.height())
        self.__l_QW_results.show()
        
class FrameScroll(QWidget):
    """FRAME USED TO DISPLAY WIDGET THAT THIS HEIGHT CAN LONGER THAN PARENT

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        
        self.g_QSA_container = QScrollArea(self)
        self.g_QSA_container.verticalScrollBar().setStyleSheet(
            "width  :10%"
        )
        self.g_QSA_container.setFixedSize(self.size())
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setFixedWidth(self.width() * 98 / 100)
        self.__l_QW_container.setFixedHeight(self.height())
        
        self.__l_I_height = 0
        
    def grapWithWidget(self, widget : QWidget):
        if widget.height() > self.g_QSA_container.height():
            widget.setFixedWidth(self.width() * 98 / 100)
            
        self.g_QSA_container.setWidget(widget)
            
    def grapRenderWithListWidget(self, listWidgets : list):
        self.__l_QW_container.deleteLater()
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setFixedWidth(self.width() * 99.9 / 100)
        
        __l_I_height = 0
        for widget in listWidgets:
            widget.setParent(self.__l_QW_container)
            widget.setFixedWidth(self.__l_QW_container.width())
            widget.move(0,__l_I_height)
            __l_I_height += widget.height()
        
        self.__l_I_height = __l_I_height
            
        if self.__l_I_height >= self.g_QSA_container.height():
            self.__l_QW_container.setFixedWidth(self.width() * 98.8 / 100)
            for widget in listWidgets:
                widget.setFixedWidth(self.__l_QW_container.width())
        
        self.__l_QW_container.setFixedHeight(__l_I_height)
        self.g_QSA_container.setWidget(self.__l_QW_container)
        self.g_QSA_container.ensureVisible(0,self.__l_QW_container.height())
        
class FrameWindows(QWidget):
    """FRAME WINDOWS USED TO CREATE A WIDGET THAT CAN BE DELETE AFTER CALL

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        setQSS(self,"framework.qss")
        
        self.__l_QVL_container = QVBoxLayout()
        self.__l_QVL_container.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QVL_container.setContentsMargins(0,0,0,0)
        self.__l_QVL_container.setSpacing(0)
        self.setLayout(self.__l_QVL_container)
        
        self.__l_QW_controllBarContainer = QWidget()
        self.__l_QW_controllBarContainer.setObjectName("FrameWindows_container")
        self.__l_QW_controllBarContainer.setFixedSize(self.width(),
                                                     self.height() * 5 / 100)

        self.__l_QHL_controllBarConainer = QHBoxLayout()
        self.__l_QHL_controllBarConainer.setContentsMargins(0,0,6,0)
        self.__l_QHL_controllBarConainer.setSpacing(0)
        self.__l_QHL_controllBarConainer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.__l_QW_controllBarContainer.setLayout(self.__l_QHL_controllBarConainer)
        
        self.g_B_exit = QPushButton()
        self.g_B_exit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.g_B_exit.setToolTip("Close")
        self.g_B_exit.setIcon(QPixmap(getPathFileImage("delete.png")))
        self.g_B_exit.setFixedSize(self.g_B_exit.sizeHint().width(),
                                   self.__l_QW_controllBarContainer.height())
        self.g_B_exit.setObjectName("FrameWindows_exit")
        self.g_B_exit.clicked.connect(self.deleteLater)
        self.__l_QHL_controllBarConainer.addWidget(self.g_B_exit)
        self.__l_QVL_container.addWidget(self.__l_QW_controllBarContainer)
        
        self.g_QW_containerShowing = QWidget()
        self.g_QW_containerShowing.setFixedSize(self.width(),
                                                self.height() * 90 / 100)
        self.__l_QVL_container.addWidget(self.g_QW_containerShowing)
        
    def grapTransparentControllBar(self):
        self.__l_QW_controllBarContainer.setStyleSheet("background-color:transparent;")
        self.g_B_exit.setStyleSheet(
            """
                QPushButton:hover{
                    background-color:rgba(0,0,0,0.3)
                }
            """
        )
        
    def setResizeHeight(self, height : int):
        self.setFixedHeight(height)
        self.g_QW_containerShowing.setFixedHeight(height * 90 / 100)
        
    def setResizeWidth(self, width):
        self.setFixedWidth(width)
        self.g_QW_containerShowing.setFixedWidth(width)
        self.__l_QW_controllBarContainer.setFixedWidth(width)
        
        
class FrameChooseData(FrameWindows):
    """FRAME USED TO SHOW ALL DATA OPTIONS BY QCHECKBOX TO CHOOSE

    Args:
        FrameWindows (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., listData : list | None = ...) -> None:
        super().__init__(parent)
        self.setResizeWidth(400)
        self.__l_frameBackground = FrameBackground(parent)
        self.g_B_exit.clicked.connect(self.__l_frameBackground.deleteLater)
        self.g_B_exit.clicked.connect(self.deleteLater)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.__l_LIST_data = listData
        
        self.g_QW_containerShowing.setStyleSheet("background-color:transparent")
        self.__l_LIST_checkBoxs = list()
        self.g_LIST_checkedData = list()
        
        for data in self.__l_LIST_data:
            __l_QCB_data = QCheckBox(data)
            __l_QCB_data.stateChanged.connect(partial(self.__checkedData,__l_QCB_data))
            self.__l_LIST_checkBoxs.append(__l_QCB_data)
        
        self.__l_QVL_layout = QVBoxLayout()
        self.g_QW_containerShowing.setLayout(self.__l_QVL_layout)
        
        index = 0
        while index < len(self.__l_LIST_checkBoxs):
            __l_QHL_layout = QHBoxLayout()
            for count in range(3):
                if index >= len(self.__l_LIST_checkBoxs): break
                
                __l_QHL_layout.addWidget(self.__l_LIST_checkBoxs[index])
                index += 1
                
            self.__l_QVL_layout.addLayout(__l_QHL_layout)
        
        self.setResizeHeight(self.__l_QVL_layout.sizeHint().height() + 50) 
        self.setResizeWidth(self.__l_QVL_layout.sizeHint().width() + 100)
        self.show()
    
    def setCheckData(self, str : str):
        if str.__eq__(""): return
        
        __l_LIST_checked = str.split(",")
        for checkBox in self.__l_LIST_checkBoxs:
            if  checkBox.text() in __l_LIST_checked:
                checkBox.setChecked(True)
    
    def __checkedData(self,checkBox : QCheckBox ,state):
        state = Qt.CheckState(state)
        
        if state == Qt.CheckState.Checked:
            self.g_LIST_checkedData.append(checkBox.text())
        elif state == Qt.CheckState.Unchecked:
            self.g_LIST_checkedData.remove(checkBox.text())
        
        self.g_LIST_checkedData.sort()
    
class FrameDowload(FrameWindows):
    """FRAME USED TO DOWLOAD A FILE FROM URL

    Args:
        FrameWindows (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., word : str | None = ...) -> None:
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.__l_FB_frameBackground = FrameBackground(self)
        self.g_B_exit.clicked.connect(lambda : self.__l_FB_frameBackground.deleteLater())
        self.setResizeHeight(100)
        
        self.__l_QHL_dowloadFile = QHBoxLayout()
        self.g_QW_containerShowing.setLayout(self.__l_QHL_dowloadFile)
        
        self.__l_L_URL = QLabel("URL")
        self.__l_L_URL.setStyleSheet("background-color:transparent;")
        self.__l_QHL_dowloadFile.addWidget(self.__l_L_URL)
        
        self.g_QLE_URL = QLineEdit()
        self.g_QLE_URL.setContentsMargins(0,5,0,5)
        self.g_QLE_URL.setPlaceholderText("Enter url and press \"enter\" to dowload...")
        self.g_QLE_URL.returnPressed.connect(lambda : self.__dowloadFile())
        self.__l_QHL_dowloadFile.addWidget(self.g_QLE_URL)
        
        self.show()
        
    def __dowloadFile(self):
        if not checkConnection(self.g_QLE_URL.text()):
            self.g_QLE_URL.setDisabled(True)
            self.g_B_exit.setDisabled(True)
            __l_FM_connection = FrameMessage(self,"Please check your connection", WARNING)
            __l_FM_connection.g_B_exit.clicked.connect(self.g_B_exit.setEnabled(True))
            __l_FM_connection.g_B_exit.clicked.connect(self.g_QLE_URL.setEnabled(True))
            __l_FM_connection.g_QPB_OK.clicked.connect(self.g_B_exit.setEnabled(True))
            __l_FM_connection.g_QPB_OK.clicked.connect(self.g_QLE_URL.setEnabled(True))
            return
                    
        dowloadFile(self.g_QLE_URL.text())
        self.__l_FB_frameBackground.deleteLater()
        self.g_B_exit.click()
        
    def getNameFile(self):
        return os.path.basename(self.g_QLE_URL.text())


WARNING = 1
SUCCESSFUL = 2
class FrameMessage(FrameWindows):
    """FRAME USED TO DISPLAY MESSAGE

    Args:
        FrameWindows (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., message : str | None = ..., type : int | None = ...) -> None:
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.__l_FB_background = FrameBackground(self)
        self.g_B_exit.clicked.connect(self.__l_FB_background.deleteLater)
        self.g_B_exit.clicked.connect(self.deleteLater)
        # self.setResizeHeight(120)
        self.setResizeWidth(400)
        
        self.__l_QFL_layout = QFormLayout()
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QFL_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.g_QW_containerShowing.setLayout(self.__l_QFL_layout)
        
        self.__l_QHL_message = QHBoxLayout()
        self.__l_QHL_message.setContentsMargins(0,0,0,0)
        self.__l_QHL_message.setSpacing(0)
        
        self.__l_QL_icon = QLabel()
        self.__l_QL_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__l_QL_icon.setStyleSheet("background-color: #f0f0f0;")
        self.__l_QL_icon.setFixedSize(self.width() * 20 / 100,
                                      self.height() * 15 / 100)
        if type == 1:
            self.__l_QL_icon.setPixmap(QPixmap(getPathFileImage("warning.png")).scaled(self.__l_QL_icon.width(),self.__l_QL_icon.height(),Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
        elif type == 2:
            self.__l_QL_icon.setPixmap(QPixmap(getPathFileImage("successful.png")).scaled(self.__l_QL_icon.width(),self.__l_QL_icon.height(),Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
        
        self.__l_QHL_message.addWidget(self.__l_QL_icon)
        
        self.__l_QL_message = QLabel(message)
        self.__l_QL_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__l_QL_message.setWordWrap(True)
        self.__l_QL_message.setStyleSheet(
            "font-family: \"Arial Rounded MT Bold\";"
            "background-color: #f0f0f0;"
            "font-size: 15px;"
        )
        self.__l_QHL_message.addWidget(self.__l_QL_message)
        
        self.__l_QFL_layout.addRow(self.__l_QHL_message)
        
        self.__l_QHL_buttonOptions = QHBoxLayout()
        self.__l_QHL_buttonOptions.setContentsMargins(0,0,0,0)
        self.__l_QHL_buttonOptions.setSpacing(0)
        self.__l_QHL_buttonOptions.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        self.g_QPB_OK = QPushButton("OK")
        self.g_QPB_OK.setFixedHeight(20)
        self.g_QPB_OK.clicked.connect(self.__l_FB_background.deleteLater)
        self.g_QPB_OK.clicked.connect(self.deleteLater)
        self.g_QPB_OK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.g_QPB_CANCEL = QPushButton("Cancel")
        self.g_QPB_CANCEL.setFixedHeight(20)
        self.g_QPB_CANCEL.clicked.connect(self.__l_FB_background.deleteLater)
        self.g_QPB_CANCEL.clicked.connect(self.deleteLater)
        self.g_QPB_CANCEL.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        if type == 1:
            self.__l_QHL_buttonOptions.addWidget(self.g_QPB_OK)
        elif type == 2:
            self.__l_QHL_buttonOptions.setContentsMargins(0,0,5,0)
            self.__l_QHL_buttonOptions.addWidget(self.g_QPB_OK)
            self.__l_QHL_buttonOptions.addWidget(self.g_QPB_CANCEL)
        
        self.__l_QFL_layout.addRow(self.__l_QHL_buttonOptions)
        
        self.setResizeHeight(self.__l_QFL_layout.sizeHint().height() + self.__l_QHL_buttonOptions.sizeHint().height()  + 10)
        self.show()
        
class FrameCheckConnection(QWidget):
    """FRAME CHECK CONNECTION

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., url : str | None = ..., exitProg : bool | None = False) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        self.g_BOOL_connect = True
        
        if not checkConnection(url):
            __l_FM_message = FrameMessage(parent,"Please checking your connection", WARNING)
            # __l_FM_message.setFixedHeight(130)
            __l_FM_message.g_B_exit.clicked.connect(self.deleteLater)
            __l_FM_message.g_QPB_OK.clicked.connect(self.deleteLater)
            
            if exitProg:
                __l_FM_message.g_B_exit.clicked.connect(sys.exit)
                __l_FM_message.g_QPB_OK.clicked.connect(sys.exit)
            
            self.g_BOOL_connect = False
            return
        
        self.deleteLater()
        
class FrameLockScreen(FrameWindows):
    def __init__(self, parent: QWidget | None = ..., message : str | None = ...) -> None:
        __l_FB_background = FrameBackground(parent)
        super().__init__(__l_FB_background)
        self.grapTransparentControllBar()
        self.g_B_exit.clicked.connect(__l_FB_background.deleteLater)
        self.setResizeWidth(__l_FB_background.width() * 30 / 100)
        self.setResizeHeight(__l_FB_background.height() * 40 / 100)
        
        self.move(__l_FB_background.width() / 2 - self.width() / 2,
                  __l_FB_background.height() / 2 - self.height() / 2)
        
        __l_QHL_lockScreen = QHBoxLayout()
        __l_QHL_lockScreen.setContentsMargins(0,0,0,0)
        __l_QHL_lockScreen.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.g_QW_containerShowing.setLayout(__l_QHL_lockScreen)
        
        __l_QL_message = QLabel(text=message)
        __l_QL_message.setFont(QFont("Arial Rounded MT Bold",30))
        __l_QL_message.setStyleSheet("background-color:transparent;")
        __l_QL_message.setFixedHeight(__l_QL_message.sizeHint().height())
        __l_QHL_lockScreen.addWidget(__l_QL_message)
        
        self.show()
        
class FrameChat:
    def __init__(self) -> None:
        self.__l_STR_topic = ""
        pass
    
    def setToppic(self, topic : str):
        self.__l_STR_topic = topic
    
    def showHint(self, key : str ,listShowHint : list, labelReceive : QLabel) -> None:
        """Show hint

        Args:
            key (str): text that use to search
            listShowHint (list): list that was returned from listRelative
            labelReceive (QLabel): labelReceive
        """
        
        __l_QVL_labelReceive = QVBoxLayout()
        __l_QVL_labelReceive.setContentsMargins(0,0,0,0)
        __l_QVL_labelReceive.setSpacing(10)
        labelReceive.setLayout(__l_QVL_labelReceive)
        __l_QL_messageHint = QLabel()
        __l_QL_messageHint.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        __l_QL_messageHint.setObjectName("showingReceive")
        __l_STR_hint = f"I have some {self.__l_STR_topic}s list the name {key} \n"
        __l_STR_hint += "\n".join(listShowHint)
        __l_QL_messageHint.setText(__l_STR_hint)
        __l_QL_messageHint.setFixedHeight(__l_QL_messageHint.sizeHint().height())
        __l_QVL_labelReceive.addWidget(__l_QL_messageHint)
        __l_QHL_openBrowser = QHBoxLayout()
        __l_QHL_openBrowser.setAlignment(Qt.AlignmentFlag.AlignLeft)
        __l_QL_openBrowser = QLabel(text="Or you can search the word on the internet")
        __l_QL_openBrowser.setObjectName("showingReceive")
        __l_QHL_openBrowser.addWidget(__l_QL_openBrowser)
        __l_QPB_openBrowser = QPushButton(icon=QPixmap(getPathFileImage("openBrowser.png")))
        __l_QPB_openBrowser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        __l_QPB_openBrowser.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        __l_QHL_openBrowser.addWidget(__l_QPB_openBrowser)
        __l_QVL_labelReceive.addLayout(__l_QHL_openBrowser)
        labelReceive.setFixedHeight(__l_QVL_labelReceive.sizeHint().height())
        
        if self.__l_STR_topic.lower().__eq__("word"):
            __l_QPB_openBrowser.clicked.connect(lambda : openBrowserWord(key))
            __l_QPB_openBrowser.setToolTip(f"Open page dictionay cambridge for word \"{key}\"")
        elif self.__l_STR_topic.lower().__eq__("grammar"):
            __l_QPB_openBrowser.clicked.connect(lambda : openBrowserFindInGoogle(f"Cấu trúc {key} trong tiếng anh"))
            __l_QPB_openBrowser.setToolTip(f"Open browser and search the grammar \"{key}\"")
        elif self.__l_STR_topic.lower().__eq__("collection"):
            __l_QPB_openBrowser.deleteLater()
            
        
    def showDontKnow(self, key : str, labelReceive : QLabel, textMessage : str, query : str | None = None) -> None:
        """Show dont't know this key

        Args:
            key (str): key don't know   
            labelReceive (QLabel): labelReceive
        """
        __l_QHL_layout = QHBoxLayout()
        __l_QHL_layout.setContentsMargins(0,0,0,0)
        __l_QHL_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        labelReceive.setLayout(__l_QHL_layout)
        __l_QL_message = QLabel()
        __l_QL_message.setObjectName("showingReceive")
        __l_QL_message.setText(textMessage)
        __l_QHL_layout.addWidget(__l_QL_message)
        __l_QPB_openBrowser = QPushButton()
        __l_QPB_openBrowser.setCursor(Qt.CursorShape.PointingHandCursor)
        __l_QPB_openBrowser.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        __l_QPB_openBrowser.setIcon(QPixmap(getPathFileImage("openBrowser.png")))
        __l_QPB_openBrowser.setFixedSize(__l_QPB_openBrowser.sizeHint().width(),
                                         __l_QL_message.sizeHint().height())
        __l_QHL_layout.addWidget(__l_QPB_openBrowser)
        
        if not query == None:
            __l_QPB_openBrowser.clicked.connect(lambda: openBrowserFindInGoogle(query))
            __l_QPB_openBrowser.setToolTip(f"Open browser to search the text \"{key}\"")
            
            return
    
        if self.__l_STR_topic.lower().__eq__("word"):
            __l_QPB_openBrowser.clicked.connect(lambda : openBrowserWord(key))
            __l_QPB_openBrowser.setToolTip(f"Open browser to search the word \"{key}\"")
        elif self.__l_STR_topic.lower().__eq__("grammar"):
            __l_QPB_openBrowser.clicked.connect(lambda: openBrowserFindInGoogle(f"Cấu trúc {key} trong tiếng anh"))
            __l_QPB_openBrowser.setToolTip(f"Open browser to search the grammar \"{key}\"")