from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from Core.Core_QSS import QWidget
from Core.Core_UI import *
from Core.Core_Audio import *
from Core.Core_QSS import *
from Core.Core_Image import *
from Core.Core_Docx import *
from Core.Core_Language import *
from Bus.Word import ListWords, Word
from Bus.Grammar import ListGrammar, Grammar
from Bus.Collection import ListCollection, Collection
from Core.Core_UI import QWidget
from Core.FrameWork import *
from Core.FrameWork import QWidget

"""STRUCTURE OF CLASS:

                              BaseManage
                                  ||
                                  ||
                                  ||
                                  ||
            ===================================================================================
            ||                                             ||                                 ||
            ||                                             ||                                 ||
            ||                                             ||                                 ||
            ||                                             ||                                 ||
        ManageWord                                      ManageGrammar                       ManageCollection
        #                                               #                                   #
        #### CoreManageWord                             #####CoreManageGrammar              ######CoreManageCollection
            #                                                #                                    #
            ###### UIWord                                    ##### UIGrammar                      # UICollection
                        
                        

Returns:
    _type_: _description_
"""


g_LIST_level = ["A1",
                "A2",
                "B1 (4.0 - 5.0)",
                "B2 (5.5 - 6.5)",
                "C1 (7.0 - 8.0)",
                "C2 (8.5+)"]
g_LIST_level.sort()

g_LIST_PartOfSpeech = ["Article",
                       "Adjective",
                       "Adverb",
                       "Noun",
                       "Pronoun",
                       "Verb",
                       "Preposition",
                       "Conjuction",
                       "Interjection",
                       "Phrasal verb",
                       "Idiom",
                       "Phrase",
                       "Collocation",
                       "Prefix",
                       "Suffix"]
g_LIST_PartOfSpeech.sort()

class Note(QWidget):
    """UI NOTE

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., listWords : ListWords | None = Ellipsis, listGrammars : ListGrammar | None = Ellipsis, listCollections : ListCollection | None = Ellipsis) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        self.setObjectName("Note")
        setQSS(self, "note.qss")
        
        self.__l_QTW_tabManage = QTabWidget(self)
        self.__l_QTW_tabManage.setFixedSize(self.size())
        self.__l_QTW_tabManage.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__l_QTW_tabManage.setObjectName("tabManage")
        
        self.__l_MW_manageWord = ManageWord(self.__l_QTW_tabManage, listWords)
        self.__l_QTW_tabManage.addTab(self.__l_MW_manageWord,"Word")
        
        self.__l_MG_manageGrammar = ManageGrammar(self.__l_QTW_tabManage, listGrammars)
        self.__l_QTW_tabManage.addTab(self.__l_MG_manageGrammar, "Grammar")
        
        self.__l_MC_manageCollection = ManageCollection(self.__l_QTW_tabManage, listCollections)
        self.__l_QTW_tabManage.addTab(self.__l_MC_manageCollection, "Collection")

class BaseManage(QWidget):
    def __init__(self, parent: QWidget | None = ..., listData : list | None = ...) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        self.__l_LIST_data = listData
        
        self.g_QW_container = QWidget(self)
        self.g_QW_container.setObjectName("container")
        self.g_QW_container.setFixedSize(self.size())
        
        self.__l_QFL_layoutContainer = QFormLayout()
        self.__l_QFL_layoutContainer.setContentsMargins(0,0,0,0)
        self.__l_QFL_layoutContainer.setSpacing(0)
        self.g_QW_container.setLayout(self.__l_QFL_layoutContainer)
        
        """SEARCH
        """
        self.__l_QW_searchContainer = QWidget()
        self.__l_QW_searchContainer.setFixedSize(self.g_QW_container.width(),
                                                 self.g_QW_container.height() * 5 / 100)
        
        self.__l_QHL_searchContainer = QHBoxLayout()
        self.__l_QHL_searchContainer.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QHL_searchContainer.setContentsMargins(0,0,0,0)
        self.__l_QHL_searchContainer.setSpacing(0)
        self.__l_QW_searchContainer.setLayout(self.__l_QHL_searchContainer)

        
        self.g_FS_searching = FrameSearch(self.__l_QW_searchContainer,self.__l_LIST_data)
        self.__l_QHL_searchContainer.addWidget(self.g_FS_searching)
        
        self.__l_QFL_layoutContainer.addRow(self.__l_QW_searchContainer)
        
        """ADDNEW
        """        
        self.__l_QHL_addNewAndChooseDataContainer = QHBoxLayout()
        self.__l_QHL_addNewAndChooseDataContainer.setContentsMargins(0,0,0,0)
        self.__l_QHL_addNewAndChooseDataContainer.setSpacing(0)
        # self.__l_QHL_addNewAndChooseDataContainer.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.g_QCBB_showData = QComboBox()
        self.g_QCBB_showData.setFixedWidth(self.g_QW_container.width() * 30 / 100)
        self.g_QCBB_showData.setContentsMargins(0,0,0,0)
        self.g_QCBB_showData.addItems(self.__l_LIST_data)
        self.g_QCBB_showData.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QHL_addNewAndChooseDataContainer.addWidget(self.g_QCBB_showData)
        
        # self.__l_QPB_openComboboxAll = QPushButton(text="slide")
        # self.__l_QPB_openComboboxAll.setFixedSize(self.__l_QPB_openComboboxAll.sizeHint())
        # self.__l_QPB_openComboboxAll.setCursor(Qt.CursorShape.PointingHandCursor)
        # self.__l_QPB_openComboboxAll.clicked.connect(self.__slideOpenAllData)
        # self.__l_QHL_addNewAndChooseDataContainer.addWidget(self.__l_QPB_openComboboxAll, alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.g_QPB_addNew = QPushButton()
        self.g_QPB_addNew.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_addNew.setFixedSize(self.g_QPB_addNew.sizeHint())
        self.g_QPB_addNew.setToolTip("Add New")
        self.g_QPB_addNew.setObjectName("addNew")
        self.g_QPB_addNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.__l_QP_addNew = QPixmap(getPathFileImage("add-new.png"))
        self.__l_QP_addNew = self.__l_QP_addNew.scaled(100,100,Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.g_QPB_addNew.setIcon(self.__l_QP_addNew)
        self.__l_QHL_addNewAndChooseDataContainer.addWidget(self.g_QPB_addNew, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.__l_QFL_layoutContainer.addRow(self.__l_QHL_addNewAndChooseDataContainer)
        
        """DISPLAY
        """
        self.__l_QHL_display = QHBoxLayout()
        self.__l_QHL_display.setSpacing(80)
        self.__l_QHL_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # BUTTON PREVIOUS
        self.g_QPB_prev = QPushButton()
        self.g_QPB_prev.setToolTip("previous")
        self.g_QPB_prev.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_prev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.g_QPB_prev.setIcon(QPixmap(getPathFileImage("prev.png")))
        self.g_QPB_prev.setFixedWidth(self.g_QW_container.width() * 5 / 100)
        self.g_QPB_prev.setFixedHeight(self.g_QW_container.height() * 40 / 100)
        self.g_QPB_prev.setDisabled(True)
        self.__l_QHL_display.addWidget(self.g_QPB_prev) 

        # WIDGET SHOWING
        self.__l_QW_containerShowing = QWidget()
        self.__l_QW_containerShowing.setFixedSize(self.width() * 70 / 100,
                                                  self.height() * 80 / 100)
        self.__l_QVL_containerShowing = QVBoxLayout()
        self.__l_QVL_containerShowing.setContentsMargins(0,0,0,0)
        self.__l_QVL_containerShowing.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QVL_containerShowing.setSpacing(0)
        self.__l_QW_containerShowing.setLayout(self.__l_QVL_containerShowing)
        
        # BUTTON EDIT
        self.__l_QW_containerEdit = QWidget()
        self.__l_QW_containerEdit.setFixedSize(self.__l_QW_containerShowing.width(),
                                               self.__l_QW_containerShowing.height() * 5 / 100)
        self.__l_QHL_containerEdit = QHBoxLayout()
        self.__l_QHL_containerEdit.setContentsMargins(0,0,0,0)
        self.__l_QHL_containerEdit.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.__l_QW_containerEdit.setLayout(self.__l_QHL_containerEdit)
        self.g_QPB_edit = QPushButton()
        self.g_QPB_edit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_edit.setObjectName("edit")
        self.g_QPB_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.g_QPB_edit.setToolTip("Edit")
        self.g_QPB_edit.setIcon(QPixmap(getPathFileImage("edit.png")))
        self.__l_QHL_containerEdit.addWidget(self.g_QPB_edit)
        self.__l_QVL_containerShowing.addWidget(self.__l_QW_containerEdit)
        
        # FRAMECROLL SHOWING
        self.__l_QW_containerFrameScroll = QWidget()
        self.__l_QW_containerFrameScroll.setFixedSize(self.__l_QW_containerShowing.width(),
                                                      self.__l_QW_containerShowing.height() * 95 / 100)
        
        self.g_FS_showing = FrameScroll(self.__l_QW_containerFrameScroll)
        self.g_FS_showing.g_QSA_container.setWidgetResizable(True)
        self.__l_QVL_containerShowing.addWidget(self.__l_QW_containerFrameScroll)
        self.__l_QHL_display.addWidget(self.__l_QW_containerShowing)
        
        # BUTTON NEXT
        self.g_QPB_next = QPushButton()
        self.g_QPB_next.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.g_QPB_next.setIcon(QPixmap(getPathFileImage("next.png")))
        self.g_QPB_next.setToolTip("next")
        self.g_QPB_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if len(listData) == 1: self.g_QPB_next.setDisabled(True)
        self.g_QPB_next.setFixedWidth(self.g_QW_container.width() * 5 / 100)
        self.g_QPB_next.setFixedHeight(self.g_QW_container.height() * 40 / 100)
        self.__l_QHL_display.addWidget(self.g_QPB_next)
        
        self.__l_QFL_layoutContainer.addRow(self.__l_QHL_display)   
        
    def updateDataShow(self):
        self.g_QCBB_showData.clear()
        self.g_QCBB_showData.addItems(self.__l_LIST_data)
    
    def checkDisablePrevAndNext(self, pos : int):
        """pos : posion
           If pos at the first of list, g_QPB_prev  will be disabled and g_QPB_next will be enabled \n
           If pos at the end of list, g_QPB_prev will be enabled and g_QPB_next will be disabled \n
           If pos is not at the end or the first of list, g_QPB_prev and g_QPB_next will be enabled \n

        Args:
            pos (int): current position in the list
        """
        
        
        if pos == 0:
            self.g_QPB_prev.setDisabled(True)
        else:
            self.g_QPB_prev.setDisabled(False)
        
        if pos == len(self.__l_LIST_data) - 1:
            self.g_QPB_next.setDisabled(True)
        else:
            self.g_QPB_next.setDisabled(False)        

# WORD
class ManageWord(BaseManage):
    def __init__(self, parent: QWidget | None = ..., listWords : ListWords | None = ...) -> None:
        super().__init__(parent, listWords.g_LIST_wordTexts)
        self.g_listWords = listWords
        self.g_CMW_core = CoreManageWord(self)

class CoreManageWord:
    def __init__(self, manageWord : ManageWord) -> None:
        self.__l_MW_manageWord = manageWord
        self.__l_I_index = 0
        
        self.__l_WORD_word = UIWord(self.__l_MW_manageWord.g_FS_showing)
        
        self.__l_MW_manageWord.g_FS_showing.grapWithWidget(self.__l_WORD_word.grapDisplay(self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[0])))

        self.__l_MW_manageWord.g_QPB_next.clicked.connect(lambda :self.__grapNext())
        self.__l_MW_manageWord.g_QPB_prev.clicked.connect(lambda : self.__grapPrev())
        self.__l_MW_manageWord.g_QPB_edit.clicked.connect(lambda : self.__edit())
        self.__l_MW_manageWord.g_QPB_addNew.clicked.connect(lambda : self.__addNew())
        self.__l_MW_manageWord.g_FS_searching.g_LW_results.itemSelectionChanged.connect(self.__grapShowBySearch)
        self.__l_MW_manageWord.g_QCBB_showData.currentIndexChanged.connect(self.__grapShowByChooseData)
        
    def reload(self):
        """Reload ManageWord
        """
        if self.__l_I_index > len(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts):
            self.__l_I_index = len(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts) - 1
        
        self.__l_MW_manageWord.g_QW_container.show()
        self.__l_MW_manageWord.g_FS_showing.grapWithWidget(self.__l_WORD_word.grapDisplay(self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[self.__l_I_index])))
        self.__l_MW_manageWord.checkDisablePrevAndNext(self.__l_I_index)
        self.__l_MW_manageWord.updateDataShow()
        
    
    def __addNew(self):
        """DISPLAY THE WIDGET THAT ONLY SHOW ALL QLINEEDIT AND BUTTON TO ADD NEW WORD
        """
        
        # CHECK CONNECTION
        
        if not FrameCheckConnection(self.__l_MW_manageWord,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_WORD_word.grapObject(parent=self.__l_MW_manageWord,listWords=self.__l_MW_manageWord.g_listWords)
    
    def __edit(self):
        """DISPLAY THE WIDGET THAT ONLY SHOW ALL QLINEEDIT AND BUTTON TO EDIT
        """
        
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MW_manageWord,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_WORD_word.grapObject(self.__l_MW_manageWord,self.__l_MW_manageWord.g_listWords, self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[self.__l_I_index]))
        
    def __grapNext(self):
        """Display in g_FS_showing a widget that only show QLabel 
        """
        
        # CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MW_manageWord,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        #check if self.__l_I_index little than lenght of self.__L_MW_manageWord.g_listWords.g_LIST_wordTexts, self.__l_I_index will be plus 1
        if self.__l_I_index < len(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts):
            self.__l_I_index += 1
        
        # self.__l_MW_manageWord.g_FS_showing.grapRenderWithWidget()
        self.__l_MW_manageWord.g_FS_showing.grapWithWidget(self.__l_WORD_word.grapDisplay(self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[self.__l_I_index])))
        self.__l_MW_manageWord.checkDisablePrevAndNext(self.__l_I_index)
        
        
    def __grapPrev(self):
        """Display in g_FS_showing a widget that only show QLabel 
        """
        
        #CHECK CONNECTIONS
        if not FrameCheckConnection(self.__l_MW_manageWord,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        #check if self.__l_I_index more than 0, self.__l_I_index will be plus 1
        if self.__l_I_index > 0:
            self.__l_I_index -= 1
            
        self.__l_MW_manageWord.g_FS_showing.grapWithWidget(self.__l_WORD_word.grapDisplay(self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[self.__l_I_index])))
        self.__l_MW_manageWord.checkDisablePrevAndNext(self.__l_I_index)
        
    def __grapShowBySearch(self):
        """DISPLAY THE WORD IN THE "INDEX" THAT RETURNED BY g_FS_searching
         """
        #CHECK CONNECTIONS
        if not FrameCheckConnection(self.__l_MW_manageWord,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_MW_manageWord.g_FS_searching.g_I_pos == -1: return
        
        self.__l_I_index = self.__l_MW_manageWord.g_FS_searching.g_I_pos

        self.__l_MW_manageWord.g_FS_showing.grapWithWidget(self.__l_WORD_word.grapDisplay(self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[self.__l_I_index])))
        self.__l_MW_manageWord.checkDisablePrevAndNext(self.__l_I_index)
    
    def __grapShowByChooseData(self):
        #CHECK CONNECTIONS
        if not FrameCheckConnection(self.__l_MW_manageWord,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_I_index = self.__l_MW_manageWord.g_QCBB_showData.currentIndex()
        
        self.__l_MW_manageWord.g_FS_showing.grapWithWidget(self.__l_WORD_word.grapDisplay(self.__l_MW_manageWord.g_listWords.getWord(self.__l_MW_manageWord.g_listWords.g_LIST_wordTexts[self.__l_I_index])))
        self.__l_MW_manageWord.checkDisablePrevAndNext(self.__l_I_index)
    
class UIWord(QWidget):
    def __init__(self, parent : QWidget) -> None:        
        super().__init__(parent)  
        self.__l_QW_parent = parent
          
        self.__l_QFL_layout = QFormLayout()
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setObjectName("containerWord")
        self.__l_QW_container.setFixedWidth(self.__l_QW_parent.width())
        self.__l_QW_container.setLayout(self.__l_QFL_layout)
    
    def grapDisplay(self, word : Word) -> QWidget:
        """ONLY USE TO DISPLAY WORD

        Args:
            word (Word): The word that will be showed in self.__l_QW_container

        Returns:
            QWidget: self.__l_QW_container that contain all QLabel to display word
        """
        
        #Make sure that in self.__l_QW_container don't have any childs into it
        self.__l_QW_container.deleteLater()
        self.__l_QFL_layout = QFormLayout()
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setObjectName("containerWord")
        self.__l_QW_container.setLayout(self.__l_QFL_layout)
        self.__l_QW_container.setFixedWidth(self.__l_QW_parent.width() * 99.8 /100)

        # DISPLAY WORD
        __l_QHL_word = QHBoxLayout()
        __l_label_word = QLabel(word.word)
        __l_label_word.setObjectName("title")
        __l_label_word.setParent(self.__l_QW_container)
        __l_QHL_word.addWidget(__l_label_word)
        self.__l_QFL_layout.addRow(__l_QHL_word)
        
        # DISPLAY fAi
        if word.fAi.__ne__("N/A"):
            self.__l_QL_fAi = QLabel(text=f"({word.fAi})")
            __l_QHL_fAi = QHBoxLayout()
            self.__l_QL_fAi.setObjectName("showing")
            __l_QHL_fAi.addWidget(self.__l_QL_fAi)
            self.__l_QFL_layout.addRow(__l_QHL_fAi)
        
        # DISPLAY PRONUNCIATION
        __l_QHL_pronunciation = QHBoxLayout()
        self.__l_label_pronunciation = QLabel(": ".join(["Pronunciation",word.pronunciation]))
        self.__l_label_pronunciation.setObjectName("showing")
        __l_QHL_pronunciation.addWidget(self.__l_label_pronunciation)
        self.__l_QFL_layout.addRow(__l_QHL_pronunciation)
        
        # DISPLAY PART_OF_SPEECH (PartOfSpeech)
        __l_QHL_partOfSpeech = QHBoxLayout()
        __l_label_partOfSpeech = QLabel(": ".join(["PartOfSpeech",word.partOfSpeech]))
        __l_label_partOfSpeech.setObjectName("showing")
        __l_label_partOfSpeech.setFixedWidth(self.__l_QW_container.width() / 2)
        __l_label_partOfSpeech.setParent(self.__l_QW_container)
        __l_QHL_partOfSpeech.addWidget(__l_label_partOfSpeech)
        self.__l_QFL_layout.addRow(__l_QHL_partOfSpeech) 
        
        # DISPLAY GRAMMAR
        __l_QVL_grammar = QVBoxLayout()
        __l_QL_grammarTitle = QLabel("Grammar:")
        __l_QL_grammarTitle.setObjectName("showing")
        __l_QL_grammarTitle.setFixedHeight(__l_QL_grammarTitle.sizeHint().height())
        __l_QVL_grammar.addWidget(__l_QL_grammarTitle)
        __l_QL_grammar = QLabel(text=word.grammar)
        __l_QL_grammar.setWordWrap(True)
        __l_QL_grammar.setFixedWidth(self.__l_QW_container.width() * 99 / 100)
        __l_QL_grammar.setObjectName("showing")
        __l_QL_grammar.setParent(self.__l_QW_container)
        __l_QVL_grammar.addWidget(__l_QL_grammar)
        self.__l_QFL_layout.addRow(__l_QVL_grammar)
        
        #DISPLAY SYNONYM
        __l_QVL_synonym = QVBoxLayout()
        __l_QL_synonymTitle = QLabel("Synonyms:")
        __l_QL_synonymTitle.setObjectName("showing")
        __l_QL_synonymTitle.setFixedHeight(__l_QL_synonymTitle.sizeHint().height())
        __l_QVL_synonym.addWidget(__l_QL_synonymTitle)
        __l_QL_synonym = QLabel(text=word.synonym)
        __l_QL_synonym.setWordWrap(True)
        __l_QL_synonym.setObjectName("showing")
        __l_QL_synonym.setFixedWidth(self.__l_QW_container.width() * 99 / 100)
        __l_QVL_synonym.addWidget(__l_QL_synonym)
        self.__l_QFL_layout.addRow(__l_QVL_synonym)
            
        # DISPLAY MEANING AND EXAMPLE (MeaningAndExample)
        __l_QVL_meaningAndExample = QVBoxLayout()
        __l_QVL_meaningAndExample.setContentsMargins(0,10,0,0)
        __l_QL_meaningAndExampleTitle = QLabel("Meaning and example:")
        __l_QL_meaningAndExampleTitle.setObjectName("showing")
        __l_QVL_meaningAndExample.addWidget(__l_QL_meaningAndExampleTitle)
        __l_label_MeaningAndExample = QLabel()
        __l_label_MeaningAndExample.setFixedWidth(self.__l_QW_container.width() * 99 /100)
        __l_label_MeaningAndExample.setText(word.meaningAndExample)
        __l_label_MeaningAndExample.setWordWrap(True)
        __l_label_MeaningAndExample.setContentsMargins(2,5,0,5)
        __l_label_MeaningAndExample.setObjectName("showing")
        __l_QVL_meaningAndExample.addWidget(__l_label_MeaningAndExample)
        self.__l_QFL_layout.addRow(__l_QVL_meaningAndExample)

        return self.__l_QW_container
    
    def grapObject(self, parent : ManageWord | None = None, listWords : ListWords | None = None, word : Word | None = None):        
        """ Create a new windows frame to display object word that will be used to create new word or edit wird

        Args:
            parent (ManageWord | None, optional): Used to set parent for FrameWindows that contain all childs. Defaults to None.
            listWords (ListWords | None, optional): Used to get method saveWOrd or deleteWord or updateWord. Defaults to None.
            word (Word | None, optional): The word that used to set information to self.g_FW_word.g_QW_containerShowing. Defaults to None.
        """
        
        parent.g_QW_container.hide()
        
        # Create new FrameWindows to show all childs
        self.g_FW_word = FrameWindows(parent)
        self.g_FW_word.setFixedWidth(parent.size().width())
        self.g_FW_word.g_B_exit.clicked.connect(parent.g_CMW_core.reload)
        self.__l_LIST_words = listWords
        
        #Create container by framescroll
        self.__l_FS_container = FrameScroll(self.g_FW_word.g_QW_containerShowing)
        self.__l_FS_container.g_QSA_container.setFixedWidth(self.g_FW_word.g_QW_containerShowing.width() * 99.5 / 100)
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setFixedSize(self.__l_FS_container.width(),
                                           self.__l_QW_container.height() * 2)
        self.__l_FS_container.grapWithWidget(self.__l_QW_container)
        
        # Create QForm
        self.__l_QFL_layoutContainerShowing = QFormLayout()
        self.__l_QW_container.setLayout(self.__l_QFL_layoutContainerShowing)
        self.__l_QW_container.setObjectName("containerShowingObject")
        
        # WORD
        self.__l_QHL_word = QHBoxLayout()
        self.__l_L_word = QLabel("Word")
        self.__l_L_word.setObjectName("wordObject")
        self.__l_L_word.setFixedSize(self.__l_L_word.sizeHint())
        self.__l_QHL_word.addWidget(self.__l_L_word)
        self.__l_QLE_word = QLineEdit()
        self.__l_QLE_word.setObjectName("wordObject")
        self.__l_QHL_word.addWidget(self.__l_QLE_word)
        self.__l_STR_fAi = "N/A"
        self.__l_QCB_formal = QCheckBox(text="formal")
        self.__l_QCB_formal.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__l_QCB_formal.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QCB_formal.setObjectName("formal")
        self.__l_QCB_formal.stateChanged.connect(partial(self.__setFormalAndInformal,self.__l_QCB_formal))
        self.__l_QHL_word.addWidget(self.__l_QCB_formal)
        self.__l_QCB_informal = QCheckBox(text="informal")
        self.__l_QCB_informal.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__l_QCB_informal.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QCB_informal.setObjectName("informal")
        self.__l_QCB_informal.stateChanged.connect(partial(self.__setFormalAndInformal,self.__l_QCB_informal))
        self.__l_QHL_word.addWidget(self.__l_QCB_informal)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_word)
        
        # PRONUNCIATION
        self.__l_QHL_pronunciation = QHBoxLayout()
        self.__l_L_pronunciation = QLabel("Pronunciation")
        self.__l_L_pronunciation.setFixedSize(self.__l_L_pronunciation.sizeHint())
        self.__l_L_pronunciation.setObjectName("wordObject")
        self.__l_QHL_pronunciation.addWidget(self.__l_L_pronunciation)
        self.__l_QLI_pronunciation = QInput()
        self.__l_QLI_pronunciation.setText("None")
        self.__l_QHL_pronunciation.addWidget(self.__l_QLI_pronunciation)
        self.__l_L_sound = QLabel("Sound")
        self.__l_L_sound.setFixedSize(self.__l_L_sound.sizeHint())
        self.__l_L_sound.setObjectName("wordObject")
        self.__l_QHL_pronunciation.addWidget(self.__l_L_sound)
        self.__l_L_nameFileSound = QLabel("No sound")
        self.__l_L_nameFileSound.setFixedSize(self.__l_L_nameFileSound.sizeHint())
        self.__l_L_nameFileSound.setObjectName("wordObject")
        self.__l_QHL_pronunciation.addWidget(self.__l_L_nameFileSound)
        self.__l_QPB_sound = QPushButton()
        self.__l_QPB_sound.setIcon(QPixmap(getPathFileImage("audio-speaker-on.png")))
        self.__l_QPB_sound.setFixedSize(self.__l_QPB_sound.sizeHint())
        self.__l_QPB_sound.setDisabled(True)
        self.__l_QHL_pronunciation.addWidget(self.__l_QPB_sound)
        self.__l_B_openFileDialog = QPushButton("...")
        self.__l_B_openFileDialog.clicked.connect(self.__openFileDialog)
        self.__l_B_openFileDialog.setFixedWidth(25)
        self.__l_QHL_pronunciation.addWidget(self.__l_B_openFileDialog)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_pronunciation)
        
        # PARTOFSPEECH
        self.__l_QHL_partOfSpeech = QHBoxLayout()
        self.__l_QL_partOfSpeech = QLabel("PartOfSpeech")
        self.__l_QL_partOfSpeech.setFixedHeight(self.__l_QL_partOfSpeech.sizeHint().height())
        self.__l_QL_partOfSpeech.setObjectName("wordObject")
        self.__l_QHL_partOfSpeech.addWidget(self.__l_QL_partOfSpeech)
        self.__l_QLE_partOfSpeech = QLineEdit()
        self.__l_QLE_partOfSpeech.setObjectName("partofspeech")
        self.__l_QHL_partOfSpeech.addWidget(self.__l_QLE_partOfSpeech)
        self.__l_B_partOfSpeech = QPushButton("...")
        self.__l_B_partOfSpeech.clicked.connect(lambda : self.__chooseData(g_LIST_PartOfSpeech, self.__l_QLE_partOfSpeech))
        self.__l_B_partOfSpeech.setFixedWidth(25)
        self.__l_QHL_partOfSpeech.addWidget(self.__l_B_partOfSpeech)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_partOfSpeech)
        
        #GRAMMAR WORD
        self.__l_QVL_grammar = QVBoxLayout()
        self.__l_QHL_grammar = QHBoxLayout()
        self.__l_QL_famyliWords = QLabel("Grammar")
        self.__l_QL_famyliWords.setFixedHeight(self.__l_QL_famyliWords.sizeHint().height())
        self.__l_QL_famyliWords.setObjectName("wordObject")
        self.__l_QHL_grammar.addWidget(self.__l_QL_famyliWords)
        self.__l_QPB_openWordgrammar = QPushButton(icon = QPixmap(getPathFileImage("word.png")))
        self.__l_QPB_openWordgrammar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QPB_openWordgrammar.setToolTip("Open MS word for grammar")
        self.__l_QPB_openWordgrammar.setFixedWidth(self.__l_QPB_openWordgrammar.sizeHint().width())
        self.__l_QPB_openWordgrammar.clicked.connect(lambda : self.__openMSWord(parent, self.__l_QTE_grammar))
        self.__l_QHL_grammar.addWidget(self.__l_QPB_openWordgrammar, alignment=Qt.AlignmentFlag.AlignRight)
        self.__l_QPB_autoChangeWord = QPushButton(icon = QPixmap(getPathFileImage("automation.png")))
        self.__l_QPB_autoChangeWord.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QPB_autoChangeWord.setToolTip("Auto change word")
        self.__l_QPB_autoChangeWord.setFixedWidth(self.__l_QPB_autoChangeWord.sizeHint().width())
        self.__l_QPB_autoChangeWord.clicked.connect(lambda : self.__autoConvert())
        self.__l_QHL_grammar.addWidget(self.__l_QPB_autoChangeWord)
        self.__l_QVL_grammar.addLayout(self.__l_QHL_grammar)
        self.__l_QTE_grammar = QTextEdit()
        self.__l_QTE_grammar.setFixedSize(self.g_FW_word.width(), self.__l_QW_container .height() * 10 / 100)
        self.__l_QVL_grammar.addWidget(self.__l_QTE_grammar)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QVL_grammar)
        
        # SYNONYMS
        self.__l_QVL_synonym = QVBoxLayout()
        self.__l_QHL_synonymAndOption = QHBoxLayout()
        self.__l_QL_synonym = QLabel("Synonym")
        self.__l_QL_synonym.setObjectName("wordObject")
        self.__l_QHL_synonymAndOption.addWidget(self.__l_QL_synonym)
        self.__l_QPB_openWordSynonym = QPushButton(icon = QPixmap(getPathFileImage("word.png")))
        self.__l_QPB_openWordSynonym.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QPB_openWordSynonym.setToolTip("Open MS Word for synonym")
        self.__l_QPB_openWordSynonym.clicked.connect(lambda : self.__openMSWord(parent, self.__l_QTE_synonym))
        self.__l_QHL_synonymAndOption.addWidget(self.__l_QPB_openWordSynonym,alignment=Qt.AlignmentFlag.AlignRight)
        self.__l_QVL_synonym.addLayout(self.__l_QHL_synonymAndOption)
        self.__l_QTE_synonym = QTextEdit()
        self.__l_QTE_synonym.setFixedSize(self.__l_QW_container.width(),
                                          self.__l_QW_container.height() * 15 / 100)
        self.__l_QVL_synonym.addWidget(self.__l_QTE_synonym)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QVL_synonym)
        
        
        #MEANING AND EXAMPLE
        self.__l_QVL_MeaningAndExample = QVBoxLayout()
        self.__l_QHL_meaningAndOptions = QHBoxLayout()
        self.__l_L_meaningAndExample = QLabel("MeaningAndExample")
        self.__l_L_meaningAndExample.setFixedSize(self.g_FW_word.g_QW_containerShowing.width(),
                                                  self.__l_L_meaningAndExample.sizeHint().height())
        self.__l_L_meaningAndExample.setObjectName("wordObject")
        self.__l_QPB_openWord = QPushButton(icon=QPixmap(getPathFileImage("word.png")))
        self.__l_QPB_openWord.setToolTip("Open MS Word")
        self.__l_QPB_openWord.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QPB_openWord.clicked.connect(lambda : self.__openMSWord(parent, self.__l_QTE_meaningAndExample))
        self.__l_QHL_meaningAndOptions.addWidget(self.__l_L_meaningAndExample)
        self.__l_QHL_meaningAndOptions.addWidget(self.__l_QPB_openWord)
        self.__l_QVL_MeaningAndExample.addLayout(self.__l_QHL_meaningAndOptions)
        self.__l_QTE_meaningAndExample = QTextEdit()
        self.__l_QVL_MeaningAndExample.addWidget(self.__l_QTE_meaningAndExample)
        
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QVL_MeaningAndExample)
        
        # SAVE 
        self.__l_QHL_save = QHBoxLayout()
        self.__l_QHL_save.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__l_QPB_save = QPushButton()
        self.__l_QPB_save.setIcon(QPixmap(getPathFileImage("save.png")))
        self.__l_QPB_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.__l_QPB_save.setToolTip("Save")
        self.__l_QPB_save.setFixedSize(100, self.__l_QPB_save.sizeHint().height())
        self.__l_QHL_save.addWidget(self.__l_QPB_save)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_save)
        
        # SET DATA IF WORD IS NOT NONE
        if word == None:
            self.__l_QPB_save.clicked.connect(lambda: self.__save(False))
        else:
            self.__l_QLE_word.setText(word.word)
            self.__l_STR_original = word.word
            self.__l_QTE_grammar.setText(word.grammar)
            self.__l_QTE_synonym.setText(word.synonym)
            self.__l_QLI_pronunciation.setText(word.pronunciation)
            self.__l_QLE_partOfSpeech.setText(word.partOfSpeech)
            if word.fAi.__eq__("formal"): 
                self.__l_QCB_formal.setChecked(True)
            if word.fAi.__eq__("informal"):
                self.__l_QCB_informal.setChecked(True)
            
            self.__l_L_nameFileSound.setText(word.audio)
            if word.audio.lower() == "no sound":
                self.__l_QPB_sound.setDisabled(True)
            else:
                self.__l_QPB_sound.setCursor(Qt.CursorShape.PointingHandCursor)
                self.__l_QPB_sound.clicked.connect(lambda: play(word.audio))
                self.__l_QPB_sound.setEnabled(True)
            self.__l_QTE_meaningAndExample.setText(word.meaningAndExample)
            
            self.__l_QPB_save.clicked.connect(lambda: self.__save(True))
        
        self.g_FW_word.show()
        self.show()
        
    def __setFormalAndInformal(self, checkBox : QCheckBox, state):
        state = Qt.CheckState(state)
        
        if state == Qt.CheckState.Checked and checkBox.objectName().__eq__("formal"):
            self.__l_QCB_informal.setChecked(False)
        if state == Qt.CheckState.Checked and checkBox.objectName().__eq__("informal"):
            self.__l_QCB_formal.setChecked(False)

        self.__l_STR_fAi = checkBox.text()
        if not self.__l_QCB_formal.isChecked() and not self.__l_QCB_informal.isChecked():
            self.__l_STR_fAi = "N/A"
    
    def __autoConvert(self):
        if self.__l_QLE_word.text().lower().__eq__(""):
            __l_FM_warningWord = FrameMessage(self.__l_QW_parent, "HAVE ANY WORD TO PREDICT !!", WARNING)
            __l_FM_warningWord.g_QPB_OK.clicked.connect(__l_FM_warningWord.deleteLater)
            return
        
        def exit():
            if len(__l_FCD_chooseData.g_LIST_checkedData) == 0: return
            __l_STR_grammar = self.__l_QTE_grammar.toPlainText()
            
            __l_STR_predict = ""
            for type in __l_FCD_chooseData.g_LIST_checkedData:
                __l_STR_predict += convertWord(self.__l_QLE_word.text(),type) + "\n"
            
            if __l_STR_grammar.endswith("\n") or __l_STR_grammar.__eq__(""):
                __l_STR_grammar += __l_STR_predict
            elif not __l_STR_grammar.endswith("\n"):
                __l_STR_grammar += "\n" + __l_STR_predict
            self.__l_QTE_grammar.setText(__l_STR_grammar)
                
        __l_FCD_chooseData = FrameChooseData(self.__l_QW_parent, g_LIST_convert)
        __l_FCD_chooseData.g_B_exit.clicked.connect(exit)
    
    def __openMSWord(self ,parent, widgetText):
        __l_FSC_openWord = FrameLockScreen(parent, "Opening word...")
        __l_FSC_openWord.g_B_exit.clicked.connect(lambda : widgetText.setText(getTextFromDocx("writting.docx")))
        __l_FSC_openWord.g_B_exit.clicked.connect(closeMicrosoftWord)
        
        if widgetText.toPlainText().__eq__(""):
            openEmptyMicrosoftWord("writting.docx")
        else:
            openMicrosoftWordWithText("writting.docx", widgetText.toPlainText())
    
    def __openFileDialog(self):
        """OPEN FRAME DOWNLOAD TO DOWNLOAD FILE AUDIO
        """
        
        def __exit():
            nameFile = self.__l_FD_frameDowload.getNameFile()
            self.__l_QPB_sound.clicked.connect(lambda : play(nameFile))
            self.__l_QPB_sound.setDisabled(False)
            self.__l_L_nameFileSound.setText(self.__l_FD_frameDowload.getNameFile())
            self.__l_L_nameFileSound.setFixedWidth(self.__l_L_nameFileSound.sizeHint().width())
            
        self.__l_FD_frameDowload = FrameDowload(self.__l_QW_parent)
        self.__l_FD_frameDowload.g_QLE_URL.returnPressed.connect(__exit)
        
        self.show()
        self.__l_FD_frameDowload.show()
        
    def __chooseData(self, listData : list, qlineEdit : QLineEdit | None):
        """CALL FRAME CHOOSE DATA TO SELECT DATA

        Args:
            parent (BaseManage): parent to set for FrameChooseData
            listData (list): list contain all options
            qlineEdit (QLineEdit): that will be settext when exit framechoosedata
        """
        
        def exit():
            qlineEdit.setText(",".join(__l_FCD_chooseData.g_LIST_checkedData))
            
            if qlineEdit.objectName().__eq__("partofspeech") and len(__l_FCD_chooseData.g_LIST_checkedData) > 1:
                meaningAndExample = ""
                
                __l_I_pos = 0
                if self.__l_QTE_meaningAndExample.toPlainText().__ne__("") : return
                for __l_I_pos in range(len(__l_FCD_chooseData.g_LIST_checkedData)):
                    meaningAndExample += "*" + __l_FCD_chooseData.g_LIST_checkedData[__l_I_pos].upper()
                    if __l_I_pos < len(__l_FCD_chooseData.g_LIST_checkedData) - 1:
                        meaningAndExample += "\n" + "\n"
                
                self.__l_QTE_meaningAndExample.setText(meaningAndExample)
                
        __l_FCD_chooseData = FrameChooseData(self.__l_QW_parent,listData)
        __l_FCD_chooseData.setCheckData(qlineEdit.text())
        __l_FCD_chooseData.g_B_exit.clicked.connect(exit)

    def __save(self, update : bool):
        """SAVE DATA IN THIS MOMENT
            update is FALSE:
                save data as new data
            update is TRUE:
                IF self.__l_QLE_word is "", delete data
                else, edit data
            
        Args:
            update (bool): check add new or update or delete
        """
        
        # CHECK CONNECTION
        if not FrameCheckConnection(self.g_FW_word,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_QTE_grammar.toPlainText().__eq__(""):
            self.__l_QTE_grammar.setText("No Grammar")
        if self.__l_QTE_synonym.toPlainText().__eq__(""):
            self.__l_QTE_synonym.setText("No Synonym")
        if self.__l_QLE_partOfSpeech.text().__eq__(""):
            self.__l_QLE_partOfSpeech.setText("N/A")
        
        if not update:
            if self.__l_QLE_word.text() == "":
                __l_FM_warningWord = FrameMessage(self.g_FW_word, "YOU FORGET ENTERING NAME OF WORD!!!", WARNING)
                __l_FM_warningWord.g_QPB_OK.clicked.connect(__l_FM_warningWord.deleteLater)
                return
            
            self.__l_LIST_words.saveData(self.__l_QLE_word.text(),
                                         self.__l_QLE_partOfSpeech.text(),
                                         self.__l_STR_fAi,
                                         self.__l_L_nameFileSound.text(),
                                         self.__l_QLI_pronunciation.text(),
                                         self.__l_QTE_grammar.toPlainText(),
                                         self.__l_QTE_synonym.toPlainText(),
                                         self.__l_QTE_meaningAndExample.toPlainText())
        else:
            if self.__l_QLE_word.text().__eq__(""):
                self.__l_LIST_words.deleteData(self.__l_STR_original)
                __l_FM_message = FrameMessage(self.g_FW_word,"DELETE SUCCESSFULLY", SUCCESSFUL)
                __l_FM_message.g_B_exit.clicked.connect(self.g_FW_word.g_B_exit.click)
                __l_FM_message.g_QPB_OK.clicked.connect(self.g_FW_word.g_B_exit.click)
                __l_FM_message.g_QPB_CANCEL.clicked.connect(self.g_FW_word.g_B_exit.click)
                return
            else:
                self.__l_LIST_words.updateData(self.__l_STR_original,
                                               self.__l_QLE_word.text(),
                                               self.__l_QLE_partOfSpeech.text(),
                                               self.__l_STR_fAi,
                                               self.__l_L_nameFileSound.text(),
                                               self.__l_QLI_pronunciation.text(),
                                               self.__l_QTE_grammar.toPlainText(),
                                               self.__l_QTE_synonym.toPlainText(),
                                               self.__l_QTE_meaningAndExample.toPlainText())
        
        __l_FM_success = FrameMessage(self.g_FW_word, "SAVE SUCCESSFULLY, DO YOU WANT EXIT?", SUCCESSFUL)
        __l_FM_success.g_QPB_OK.clicked.connect(self.g_FW_word.g_B_exit.click)
        __l_FM_success.g_QPB_CANCEL.clicked.connect(__l_FM_success.g_B_exit.click)
        
# GRAMMAR
class ManageGrammar(BaseManage):
    """UI GRAMMAR

    Args:
        BaseManage (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., listGrammars: ListGrammar | None = ...) -> None:
        super().__init__(parent, listGrammars.g_LIST_grammarTexts)
        self.g_LG_grammars = listGrammars

        self.g_CMG_core = CoreManageGrammar(self)
        
class CoreManageGrammar:
    """CATCH HANDLE AND RESOLVE EVENT FROM MANAGE GRAMMAR
    """
    
    def __init__(self, manageGrammar : ManageGrammar) -> None:
        self.__l_MG_grammar = manageGrammar
        self.__l_I_index = 0
        self.__l_GU_grammar = GrammarUI(self.__l_MG_grammar.g_FS_showing)
        
        self.__l_MG_grammar.g_FS_showing.grapWithWidget(self.__l_GU_grammar.grapDisplay(self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[0])))
        self.__l_MG_grammar.g_QPB_addNew.clicked.connect(lambda : self.__addNew())
        self.__l_MG_grammar.g_QPB_edit.clicked.connect(lambda :self.__edit() )
        self.__l_MG_grammar.g_QPB_prev.clicked.connect(lambda : self.__grapPrev())
        self.__l_MG_grammar.g_QPB_next.clicked.connect(lambda : self.__grapNext())
        self.__l_MG_grammar.g_FS_searching.g_LW_results.itemSelectionChanged.connect(self.__grapSearch)
        self.__l_MG_grammar.g_QCBB_showData.currentIndexChanged.connect(self.__grapChooseData)

    def reload(self):
        """RELOAD self.__l_MG_grammar.g_QW_container to display to screen
        """
        if self.__l_I_index > len(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts):
            self.__l_I_index = len(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts) - 1
        
        self.__l_MG_grammar.g_QW_container.show()
        self.__l_MG_grammar.g_FS_showing.grapWithWidget(self.__l_GU_grammar.grapDisplay(self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[0])))
        self.__l_MG_grammar.checkDisablePrevAndNext(self.__l_I_index)
        self.__l_MG_grammar.updateDataShow()
    
    def __addNew(self):
        """CALL FRAME THAT USED TO ADD NEW GRAMMAR
        """
        
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MG_grammar,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_GU_grammar.grapObject(self.__l_MG_grammar,self.__l_MG_grammar.g_LG_grammars)
    
    def __edit(self):
        """CALL FRAME THAT USED TO EDIT GRAMMAR
        """
        
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MG_grammar,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_GU_grammar.grapObject(self.__l_MG_grammar, self.__l_MG_grammar.g_LG_grammars, self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[self.__l_I_index]))     
    
    def __grapNext(self):
        """CALL TO DISPLAY THE WORD IN SHOWING WIDGET
        """
        
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MG_grammar,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_I_index < len(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts):
            self.__l_I_index += 1
        
        self.__l_MG_grammar.g_FS_showing.grapWithWidget(self.__l_GU_grammar.grapDisplay(self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[self.__l_I_index])))
        
        self.__l_MG_grammar.checkDisablePrevAndNext(self.__l_I_index)
    
    def __grapPrev(self):
        """CALL TO DISPLAY THE WORD IN SHOWING WIDGET 
        """
        
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MG_grammar, "https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_I_index > 0:
            self.__l_I_index -= 1
        self.__l_MG_grammar.g_FS_showing.grapWithWidget(self.__l_GU_grammar.grapDisplay(self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[self.__l_I_index])))
        self.__l_MG_grammar.checkDisablePrevAndNext(self.__l_I_index)
    
    def __grapSearch(self):
        """CALL TO DISPLAY WORD THAT RETURN FORM SEARCH FRAME
        """
        
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MG_grammar, "https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_I_index = self.__l_MG_grammar.g_FS_searching.g_I_pos
        self.__l_MG_grammar.g_FS_showing.grapWithWidget(self.__l_GU_grammar.grapDisplay(self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[self.__l_I_index])))
        self.__l_MG_grammar.checkDisablePrevAndNext(self.__l_I_index)
    
    def __grapChooseData(self):
        #CHECK CONNECTION
        if not FrameCheckConnection(self.__l_MG_grammar, "https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_I_index = self.__l_MG_grammar.g_QCBB_showData.currentIndex()
        self.__l_MG_grammar.g_FS_showing.grapWithWidget(self.__l_GU_grammar.grapDisplay(self.__l_MG_grammar.g_LG_grammars.getGrammar(self.__l_MG_grammar.g_LG_grammars.g_LIST_grammarTexts[self.__l_I_index])))
        self.__l_MG_grammar.checkDisablePrevAndNext(self.__l_I_index)
    
class GrammarUI(QWidget):
    """UI OF GRAMMAR

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent : QWidget | None = Ellipsis) -> None:
        super().__init__(parent)
        self.__l_QW_parent = parent
        
        self.__l_QFL_layout = QFormLayout()
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setObjectName("containerGrammar")
        self.__l_QW_container.setFixedWidth(self.__l_QW_parent.width())
        self.__l_QW_container.setLayout(self.__l_QFL_layout)
    
    def grapDisplay(self, grammar : Grammar) ->QWidget:
        """ONLY USE TO DISPLAY GRAMMAR

        Args:
            grammar (Gord): The grammar that will be showed in self.__l_QW_container

        Returns:
            QWidget: self.__l_QW_container that contain all QLabel to display word
        """
        
        self.__l_QW_container.deleteLater()
        self.__l_QFL_layout = QFormLayout()
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QW_container = QWidget()
        self.__l_QW_container.setObjectName("containerWord")
        self.__l_QW_container.setLayout(self.__l_QFL_layout)
        self.__l_QW_container.setFixedWidth(self.__l_QW_parent.width() * 99.8 /100)

        __l_label_grammar = QLabel()
        __l_label_grammar.setWordWrap(True)
        __l_label_grammar.setText(grammar.nameOfGrammar.upper())
        __l_label_grammar.setStyleSheet(
            """
                background-color : #f5f5f5;
                font-family: "Arial";
                font-size: 25px;
            """
        )
        self.__l_QFL_layout.addRow(__l_label_grammar)
        
        __l_QHL_relative = QHBoxLayout()
        __l_QHL_relative.setContentsMargins(0,0,0,0)
        __l_label_relative = QLabel(": ".join(["Relative",grammar.relative]))
        __l_label_relative.setObjectName("showing")
        __l_QHL_relative.addWidget(__l_label_relative)
        self.__l_QFL_layout.addRow(__l_QHL_relative)

        __l_QL_caseAndExample = QLabel()
        __l_QL_caseAndExample.setFixedWidth(self.__l_QW_container.width() * 99 / 100)
        __l_QL_caseAndExample.setText(grammar.caseAndExampe)
        __l_QL_caseAndExample.setWordWrap(True)
        __l_QL_caseAndExample.setContentsMargins(2,0,0,0)
        __l_QL_caseAndExample.setObjectName("showing")
        self.__l_QFL_layout.addRow(__l_QL_caseAndExample)
        
        self.__l_QW_container.setFixedHeight(self.__l_QFL_layout.totalSizeHint().height())

        return self.__l_QW_container
    
    def grapObject(self, parent : ManageGrammar, listGrammars : ListGrammar, grammar : Grammar | None = None):
        """ Create a new windows frame to display object grammar that will be used to create new word or edit wird

        Args:
            parent (ManageGrammar | None, optional): Used to set parent for FrameWindows that contain all childs. Defaults to None.
            listGrammars (ListGrammars | None, optional): Used to get method saveGrammar or deleteGrammar or updateGrammar. Defaults to None.
            grammar (Grammar | None, optional): The word that used to set information to self.g_FW_grammar.g_QW_containerShowing. Defaults to None.
        """
        
        parent.g_QW_container.hide()
        self.g_FW_grammar = FrameWindows(parent)
        self.g_FW_grammar.setFixedWidth(parent.size().width())
        def exit():
            parent.g_CMG_core.reload()
        
        self.g_FW_grammar.g_B_exit.clicked.connect(exit)
        self.__l_LIST_gramamrs = listGrammars
        
        self.__l_QFL_layoutContainerShowing = QFormLayout()
        self.g_FW_grammar.g_QW_containerShowing.setLayout(self.__l_QFL_layoutContainerShowing)
        self.g_FW_grammar.g_QW_containerShowing.setObjectName("containerShowingObject")
        
        self.__l_QHL_nameOfGrammar = QHBoxLayout()
        self.__l_QL_nameOfGrammar = QLabel("NameOfGrammar")
        self.__l_QL_nameOfGrammar.setObjectName("grammarObject")
        self.__l_QHL_nameOfGrammar.addWidget(self.__l_QL_nameOfGrammar)
        self.__l_QLE_nameOfGrammar = QLineEdit()
        self.__l_QHL_nameOfGrammar.addWidget(self.__l_QLE_nameOfGrammar)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_nameOfGrammar)
        
        self.__l_QHL_relative = QHBoxLayout()
        self.__l_QL_relative = QLabel("Relative")
        self.__l_QL_relative.setObjectName("grammarObject")
        self.__l_QHL_relative.addWidget(self.__l_QL_relative)
        self.__l_QLE_relative = QLineEdit()
        self.__l_QHL_relative.addWidget(self.__l_QLE_relative)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_relative)
        
        self.__l_QVL_caseAndExample = QVBoxLayout()
        __l_QHL_caseExampleAndOption = QHBoxLayout()
        self.__l_QL_caseAndExample = QLabel("CaseAndExample")
        self.__l_QL_caseAndExample.setObjectName("grammarObject")
        self.__l_QPB_openWord = QPushButton(icon=QPixmap(getPathFileImage("word.png")))
        self.__l_QPB_openWord.setToolTip("Open MS Word")
        self.__l_QPB_openWord.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__l_QPB_openWord.setFixedWidth(self.__l_QPB_openWord.sizeHint().width())
        self.__l_QPB_openWord.clicked.connect(lambda : self.__openWord(parent))
        __l_QHL_caseExampleAndOption.addWidget(self.__l_QL_caseAndExample)
        __l_QHL_caseExampleAndOption.addWidget(self.__l_QPB_openWord)
        self.__l_QVL_caseAndExample.addLayout(__l_QHL_caseExampleAndOption)
        self.__l_QTE_caseAndExample = QTextEdit()
        self.__l_QVL_caseAndExample.addWidget(self.__l_QTE_caseAndExample)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QVL_caseAndExample)
        
        self.__l_QHL_save = QHBoxLayout()
        self.__l_QHL_save.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.__l_QPB_save = QPushButton()
        self.__l_QPB_save.setIcon(QPixmap(getPathFileImage("save.png")))
        self.__l_QPB_save.setFixedSize(100,self.__l_QPB_save.sizeHint().height())
        self.__l_QPB_save.setToolTip("Save")
        self.__l_QPB_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.__l_QHL_save.addWidget(self.__l_QPB_save)
        self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_save)
        
        if grammar == None:
            self.__l_QPB_save.clicked.connect(lambda : self.__saveData(False))
        else:
            self.__l_QLE_nameOfGrammar.setText(grammar.nameOfGrammar)
            self.__l_STR_nameOfGrammarOriginal = grammar.nameOfGrammar
            self.__l_QLE_relative.setText(grammar.relative)
            self.__l_QTE_caseAndExample.setText(grammar.caseAndExampe)
            self.__l_QPB_save.clicked.connect(lambda:self.__saveData(True))
        
        self.g_FW_grammar.show()
        self.show()
    
    def __openWord(self, parent):
        __l_FLS_openWord = FrameLockScreen(parent, "Opeing MS Word...")
        __l_FLS_openWord.g_B_exit.clicked.connect(closeMicrosoftWord)
        __l_FLS_openWord.g_B_exit.clicked.connect(lambda : self.__l_QTE_caseAndExample.setText(getTextFromDocx("writting.docx")))
        
        if self.__l_QTE_caseAndExample.toPlainText().__eq__(""):
            openEmptyMicrosoftWord("writting.docx")
        else:
            openMicrosoftWordWithText("writting.docx", self.__l_QTE_caseAndExample.toPlainText())
    
    def __saveData(self, update : bool):
        """SAVE DATA IN THIS MOMENT
            update is FALSE:
                save data as new data
            update is TRUE:
                IF self.__l_QLE_grammar is "", delete data
                else, edit data
            
        Args:
            update (bool): check add new or update or delete
        """
        
        # CHECK CONNECTION 
        if not FrameCheckConnection(self.g_FW_grammar,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_QLE_relative.text().__eq__(""):
            self.__l_QLE_relative.setText("N/A")
        
        if not update:
            if self.__l_QLE_nameOfGrammar.text() == "":
                FrameMessage(self.g_FW_grammar,"YOU FORGET ENTERING NAME OF GRAMMAR!!!", WARNING)
                return
            
            self.__l_LIST_gramamrs.saveData(self.__l_QLE_nameOfGrammar.text(),
                                            self.__l_QLE_relative.text(),
                                            self.__l_QTE_caseAndExample.toPlainText())
        else:
            if self.__l_QLE_nameOfGrammar.text().__eq__(""):
                self.__l_LIST_gramamrs.deleteData(self.__l_STR_nameOfGrammarOriginal)
                __l_FM_message = FrameMessage(self.g_FW_grammar, "DELETE SUCCESSLY",SUCCESSFUL)
                __l_FM_message.g_B_exit.clicked.connect(self.g_FW_grammar.g_B_exit.click)
                __l_FM_message.g_QPB_CANCEL.clicked.connect(self.g_FW_grammar.g_B_exit.click)
                __l_FM_message.g_QPB_OK.clicked.connect(self.g_FW_grammar.g_B_exit.click)
                return
            else:
                self.__l_LIST_gramamrs.updateGrammar(self.__l_STR_nameOfGrammarOriginal,self.__l_QLE_nameOfGrammar.text(),self.__l_QLE_relative.text(),self.__l_QTE_caseAndExample.toPlainText())
            
        __l_FM_success = FrameMessage(self.g_FW_grammar, "SAVE SUCCESSLY, DO YOU WANT TO EXIT?", SUCCESSFUL)
        __l_FM_success.g_QPB_OK.clicked.connect(self.g_FW_grammar.g_B_exit.click)
        __l_FM_success.g_QPB_CANCEL.clicked.connect(__l_FM_success.g_B_exit.click)
        
# COLLECTION
class ManageCollection(BaseManage):
    def __init__(self, parent: QWidget | None = ..., listData: ListCollection | None = ...) -> None:
        super().__init__(parent, listData.g__LIST_collectionText)
        self.g__listCollections = listData
        
        self.g__CMC_core = CoreManageCollection(self)
        
class CoreManageCollection:
    def __init__(self, manageCollections : ManageCollection) -> None:
        self.__l_MC_manageCollections = manageCollections
        self.__l_I_index = 0
        self.__l_CU_collectionUI = CollectionUI(self.__l_MC_manageCollections.g_FS_showing)
        
        self.__l_MC_manageCollections.g_FS_showing.grapWithWidget(self.__l_CU_collectionUI.grapDisplay(self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[0])))
        self.__l_MC_manageCollections.g_QPB_addNew.clicked.connect(self.__addNew)
        self.__l_MC_manageCollections.g_QPB_edit.clicked.connect(self.__edit)
        self.__l_MC_manageCollections.g_QPB_prev.clicked.connect(self.__grapPrev)
        self.__l_MC_manageCollections.g_QPB_next.clicked.connect(self.__grapNext)
        self.__l_MC_manageCollections.g_FS_searching.g_LW_results.itemSelectionChanged.connect(self.__grapSearch)
        self.__l_MC_manageCollections.g_QCBB_showData.currentIndexChanged.connect(self.__grapChooseData)
        
    def reload(self):
        if self.__l_I_index >= len(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText):
            self.__l_I_index = len(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText) - 1
        
        self.__l_MC_manageCollections.g_QW_container.show()
        self.__l_MC_manageCollections.g_FS_showing.grapWithWidget(self.__l_CU_collectionUI.grapDisplay(self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[self.__l_I_index])))
        self.__l_MC_manageCollections.checkDisablePrevAndNext(self.__l_I_index)
        self.__l_MC_manageCollections.updateDataShow()
        
    def __addNew(self):
        if not FrameCheckConnection(self.__l_MC_manageCollections,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        self.__l_CU_collectionUI.grapObject(self.__l_MC_manageCollections, self.__l_MC_manageCollections.g__listCollections)
    
    def __edit(self):
        if not FrameCheckConnection(self.__l_MC_manageCollections,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return

        self.__l_CU_collectionUI.grapObject(self.__l_MC_manageCollections, self.__l_MC_manageCollections.g__listCollections, self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[self.__l_I_index]))
        
    def __grapNext(self):
        if not FrameCheckConnection(self.__l_MC_manageCollections,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_I_index < len(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText):
            self.__l_I_index += 1
        
        self.__l_MC_manageCollections.g_FS_showing.grapWithWidget(self.__l_CU_collectionUI.grapDisplay(self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[self.__l_I_index])))
        self.__l_MC_manageCollections.checkDisablePrevAndNext(self.__l_I_index)
        
    def __grapPrev(self): 
        if not FrameCheckConnection(self.__l_MC_manageCollections,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_I_index > 0:
            self.__l_I_index -= 1
            
        self.__l_MC_manageCollections.g_FS_showing.grapWithWidget(self.__l_CU_collectionUI.grapDisplay(self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[self.__l_I_index])))
        self.__l_MC_manageCollections.checkDisablePrevAndNext(self.__l_I_index)
        
    def __grapSearch(self):
        if not FrameCheckConnection(self.__l_MC_manageCollections,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return 
        
        self.__l_I_index = self.__l_MC_manageCollections.g_FS_searching.g_I_pos
        
        self.__l_MC_manageCollections.g_FS_showing.grapWithWidget(self.__l_CU_collectionUI.grapDisplay(self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[self.__l_I_index])))
        self.__l_MC_manageCollections.checkDisablePrevAndNext(self.__l_I_index)
        
    def __grapChooseData(self):
        if not FrameCheckConnection(self.__l_MC_manageCollections,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return 
        
        self.__l_I_index = self.__l_MC_manageCollections.g_QCBB_showData.currentIndex()
        self.__l_MC_manageCollections.g_FS_showing.grapWithWidget(self.__l_CU_collectionUI.grapDisplay(self.__l_MC_manageCollections.g__listCollections.getCollection(self.__l_MC_manageCollections.g__listCollections.g__LIST_collectionText[self.__l_I_index])))
        self.__l_MC_manageCollections.checkDisablePrevAndNext(self.__l_I_index) 
        
class CollectionUI(QWidget):
    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)
        self.__l_QW_parent = parent
        
        self.__l_QFL_layout = QFormLayout()
        self.__l_QFL_layout.setContentsMargins(0,0,0,0)
        self.__l_QW_container = QWidget()
        # self.__l_QW_container.setObjectName("containerGrammar")
        self.__l_QW_container.setFixedWidth(self.__l_QW_parent.width())
        self.__l_QW_container.setLayout(self.__l_QFL_layout)
        
    def grapDisplay(self, collection : Collection) ->QWidget:
            """ONLY USE TO DISPLAY COLLECTION

            Args:
                grammar (Gord): The collection that will be showed in self.__l_QW_container

            Returns:
                QWidget: self.__l_QW_container that contain all QLabel to display word
            """

            self.__l_QW_container.deleteLater()
            self.__l_QFL_layout = QFormLayout()
            self.__l_QFL_layout.setContentsMargins(0,0,0,0)
            self.__l_QW_container = QWidget()
            self.__l_QW_container.setObjectName("containerWord")
            self.__l_QW_container.setLayout(self.__l_QFL_layout)
            self.__l_QW_container.setFixedWidth(self.__l_QW_parent.width() * 99.8 /100)

            __l_label_collection = QLabel()
            __l_label_collection.setWordWrap(True)
            __l_label_collection.setText(collection.nameOfCollection.upper())
            __l_label_collection.setStyleSheet(
                """
                    background-color : #f5f5f5;
                    font-family: "Arial";
                    font-size: 25px;
                """
            )
            self.__l_QFL_layout.addRow(__l_label_collection)

            __l_QL_collections = QLabel()
            __l_QL_collections.setFixedWidth(self.__l_QW_container.width() * 99 / 100)
            __l_QL_collections.setText(collection.collections)
            __l_QL_collections.setWordWrap(True)
            __l_QL_collections.setContentsMargins(2,0,0,0)
            __l_QL_collections.setObjectName("showing")
            self.__l_QFL_layout.addRow(__l_QL_collections)

            self.__l_QW_container.setFixedHeight(self.__l_QFL_layout.totalSizeHint().height())

            return self.__l_QW_container
        
    def grapObject(self, parent : ManageCollection, listCollections : ListCollection, collection : Collection | None = None):
           """ Create a new windows frame to display object grammar that will be used to create new word or edit wird
    
           Args:
               parent (ManageCollection | None, optional): Used to set parent for FrameWindows that contain all childs. Defaults to None.
               listGrammars (ListCollections | None, optional): Used to get method saveCollection or deleteCollection or updateCollection. Defaults to None.
               collection (Collection | None, optional): The word that used to set information to self.g_FW_collection.g_QW_containerShowing. Defaults to None.
           """
           
           parent.g_QW_container.hide()
           self.g_FW_collection = FrameWindows(parent)
           self.g_FW_collection.setFixedWidth(parent.size().width())
           def exit():
               parent.g__CMC_core.reload()
           
           self.g_FW_collection.g_B_exit.clicked.connect(exit)
           self.__l_LIST_collections = listCollections
           
           self.__l_QFL_layoutContainerShowing = QFormLayout()
           self.g_FW_collection.g_QW_containerShowing.setLayout(self.__l_QFL_layoutContainerShowing)
           self.g_FW_collection.g_QW_containerShowing.setObjectName("containerShowingObject")
           
           self.__l_QHL_nameOfCollection = QHBoxLayout()
           self.__l_QL_nameOfCollection = QLabel("NameOfCollection")
           self.__l_QL_nameOfCollection.setObjectName("grammarObject")
           self.__l_QHL_nameOfCollection.addWidget(self.__l_QL_nameOfCollection)
           self.__l_QLE_nameOfCollection = QLineEdit()
           self.__l_QHL_nameOfCollection.addWidget(self.__l_QLE_nameOfCollection)
           self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_nameOfCollection)
           
           self.__l_QVL_collections = QVBoxLayout()
           __l_QHL_collections = QHBoxLayout()
           self.__l_QL_collections   = QLabel("Collections")
           self.__l_QL_collections  .setObjectName("grammarObject")
           self.__l_QPB_openWord = QPushButton(icon=QPixmap(getPathFileImage("word.png")))
           self.__l_QPB_openWord.setToolTip("Open MS Word")
           self.__l_QPB_openWord.setCursor(Qt.CursorShape.PointingHandCursor)
           self.__l_QPB_openWord.setFixedWidth(self.__l_QPB_openWord.sizeHint().width())
           self.__l_QPB_openWord.clicked.connect(lambda : self.__openWord(parent))
           __l_QHL_collections.addWidget(self.__l_QL_collections)
           __l_QHL_collections.addWidget(self.__l_QPB_openWord)
           self.__l_QVL_collections.addLayout(__l_QHL_collections)
           self.__l_QTE_collections = QTextEdit()
           self.__l_QVL_collections.addWidget(self.__l_QTE_collections)
           self.__l_QFL_layoutContainerShowing.addRow(self.__l_QVL_collections)
           
           self.__l_QHL_save = QHBoxLayout()
           self.__l_QHL_save.setAlignment(Qt.AlignmentFlag.AlignHCenter)
           self.__l_QPB_save = QPushButton()
           self.__l_QPB_save.setIcon(QPixmap(getPathFileImage("save.png")))
           self.__l_QPB_save.setFixedSize(100,self.__l_QPB_save.sizeHint().height())
           self.__l_QPB_save.setToolTip("Save")
           self.__l_QPB_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
           self.__l_QHL_save.addWidget(self.__l_QPB_save)
           self.__l_QFL_layoutContainerShowing.addRow(self.__l_QHL_save)
           
           if collection == None:
               self.__l_QPB_save.clicked.connect(lambda : self.__saveData(False))
           else:
               self.__l_QLE_nameOfCollection.setText(collection.nameOfCollection)
               self.__l_STR_nameOfGrammarOriginal = collection.nameOfCollection
               self.__l_QTE_collections.setText(collection.collections)
               self.__l_QPB_save.clicked.connect(lambda:self.__saveData(True))
           
           self.g_FW_collection.show()
           self.show()
    
    def __openWord(self, parent):
        __l_FLS_lockScreen = FrameLockScreen(parent, "Opening MS Word")
        __l_FLS_lockScreen.g_B_exit.clicked.connect(closeMicrosoftWord)
        __l_FLS_lockScreen.g_B_exit.clicked.connect(lambda : self.__l_QTE_collections.setText(getTextFromDocx("writting.docx")))
        
        if self.__l_QTE_collections.toPlainText().__eq__(""):
            openEmptyMicrosoftWord("writting.docx")
        else:
            openMicrosoftWordWithText("writting.docx", self.__l_QTE_collections.toPlainText())    
            
    def __saveData(self, update : bool) -> None:
        if not FrameCheckConnection(self.g_FW_collection,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return

        if not update:
            if self.__l_QLE_nameOfCollection.text().strip() == "":
                FrameMessage(self.g_FW_collection,"YOU FORGET ENTERING NAME OF COLLECTIONS!!!", WARNING)
                return
            
            self.__l_LIST_collections.saveCollection(self.__l_QLE_nameOfCollection.text(), self.__l_QTE_collections.toPlainText())
        else:
            if self.__l_QLE_nameOfCollection.text().strip() == "":
                self.__l_LIST_collections.deleteCollection(self.__l_STR_nameOfGrammarOriginal)
                __l_FM_message = FrameMessage(self.g_FW_collection, "DELETE SUCCESSLY",SUCCESSFUL)
                __l_FM_message.g_B_exit.clicked.connect(self.g_FW_collection.g_B_exit.click)
                __l_FM_message.g_QPB_CANCEL.clicked.connect(self.g_FW_collection.g_B_exit.click)
                __l_FM_message.g_QPB_OK.clicked.connect(self.g_FW_collection.g_B_exit.click)
                return
            else:
                self.__l_LIST_collections.updateCollection(self.__l_STR_nameOfGrammarOriginal, self.__l_QLE_nameOfCollection.text(), self.__l_QTE_collections.toPlainText())
        
        __l_FM_success = FrameMessage(self.g_FW_collection, "SAVE SUCCESSFULLY, DO YOU WANT TO EXIT?", SUCCESSFUL)
        __l_FM_success.g_QPB_OK.clicked.connect(self.g_FW_collection.g_B_exit.click)
        __l_FM_success.g_QPB_CANCEL.clicked.connect(__l_FM_success.g_B_exit.click)