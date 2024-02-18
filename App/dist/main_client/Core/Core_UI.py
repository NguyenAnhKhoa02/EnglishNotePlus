from PySide6.QtWidgets import (
    QMainWindow, QWidget, QPushButton,
    QFrame, QVBoxLayout, QHBoxLayout, 
    QFormLayout, QLabel, QTabWidget,
    QLineEdit, QScrollArea, QFileDialog, 
    QComboBox, QTextEdit, QTableWidget,
    QTableWidgetItem, QListWidget, QCheckBox,
    QGraphicsItem, QGraphicsWidget
)

from PySide6.QtCore import (
    Qt, QEvent, QObject, QCoreApplication,
    QPropertyAnimation  
)

from PySide6.QtGui import(
    QGuiApplication, QDragMoveEvent, QMouseEvent,
    QKeyEvent, QCursor, QFont, QKeySequence, QShortcut
)

from functools import partial

from PIL import ImageFont

import os

class QInput(QLineEdit):
    def __init__(self):
        super().__init__()
    
    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        self.selectAll()
        
# class Table(QTableWidget):
#     def __init__(self, parent : QWidget, listData : list):
#         super().__init__(parent)
#         self.setFixedSize(parent.size())
        
#     def mousePressEvent(self, event: QMouseEvent) -> None:
#         __l_ITW_item = self.itemAt(event.pos())
        
#         if __l_ITW_item.isSelected() == True:
#             __l_ITW_item.setSelected(False)
#         else:
#             __l_ITW_item.setSelected(True)
            
#     def getTextSelectedItems(self) -> list:
#         __l_LIST_text = list()
        
#         for item in self.selectedItems():
#             __l_LIST_text.append(item.text())
            
#         return __l_LIST_text