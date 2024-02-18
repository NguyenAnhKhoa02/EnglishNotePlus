import PySide6.QtGui
from Core.Core_UI import *
from Core.Core_QSS import *
from Core.Core_Image import *

class Controllbar(QWidget):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        setQSS(self, "controllbar.qss")
        self.__l_QHL_layout = QHBoxLayout()
        self.__l_QHL_layout.setContentsMargins(0,0,0,0)
        self.__l_QHL_layout.setSpacing(0)
        self.__l_QHL_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setLayout(self.__l_QHL_layout)
        
        __l_QL_version = QLabel(self)
        __l_QL_version.setContentsMargins(0,0,5,4)
        __l_QL_version.setToolTip("version")
        __l_QL_version.setObjectName("version")
        __l_QL_version.setText("1.1.6552138")
        __l_QL_version.move(0,0)
        __l_QL_version.setFixedWidth(__l_QL_version.sizeHint().width())
        
        self.g_QPB_minimize = QPushButton()
        self.g_QPB_minimize.setToolTip("minimize")
        self.g_QPB_minimize.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_minimize.setIcon(QPixmap(getPathFileImage("minimize.png")))
        self.g_QPB_minimize.setObjectName("buttonControllbar")
        self.g_QPB_minimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.__l_QHL_layout.addWidget(self.g_QPB_minimize)
        
        self.g_QPB_exit = QPushButton()
        self.g_QPB_exit.setToolTip("exit")
        self.g_QPB_exit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__l_QP_exit = QPixmap(QPixmap(getPathFileImage("exit.png")))
        self.g_QPB_exit.setIcon(self.__l_QP_exit)
        self.g_QPB_exit.setObjectName("buttonControllbar")
        self.g_QPB_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.__l_QHL_layout.addWidget(self.g_QPB_exit)
        
    def setClient(self, client):
        self.__l_CLIENT_client = client    
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.__l_I_currentPos = event.pos()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.__l_I_movePos = event.pos()
        self.__l_CLIENT_client.move(self.__l_CLIENT_client.pos() + (self.__l_I_movePos - self.__l_I_currentPos))