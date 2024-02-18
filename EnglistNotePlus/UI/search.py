from Core.Core_QSS import QWidget
from Core.Core_UI import *
from Core.Core_Audio import *
from Core.Core_Text import *
from Bus.Word import ListWords, Word
from Bus.Collection import ListCollection, Collection
from Bus.Grammar import ListGrammar, Grammar
from Core.Core_UI import QWidget
from Core.FrameWork import *
from Core.FrameWork import QWidget

listType = [
    "Eng - Viet",
    "Grammar",
    "Collection"
]

class Search(QWidget):
    def __init__(self, parent: QWidget, listWords : ListWords, listGrammars : ListGrammar, listCollections : ListCollection) -> None:
        self.g_LW_listWords = listWords
        self.g_LG_listGrammars = listGrammars
        self.g_LC_listCOllections = listCollections
        
        super().__init__(parent)
        self.setFixedSize(parent.size())
        self.setObjectName("Search")
        setQSS(self, "search.qss")
        
        self.__l_QW_container = QWidget(self)
        self.__l_QW_container.setFixedSize(self.size())
        self.__l_QW_container.setObjectName("container")
        
        __l_QHL_layout = QHBoxLayout()
        __l_QHL_layout.setSpacing(0)
        __l_QHL_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.__l_QW_container.setLayout(__l_QHL_layout)
        
        self.__l_QW_searchContainer = QWidget()
        self.__l_QW_searchContainer.setFixedSize(self.__l_QW_container.width() * 80 / 100,
                                                 self.__l_QW_container.height() * 4 / 100)
        self.g_FS_frameSearch = FrameSearch(self.__l_QW_searchContainer,self.g_LW_listWords.g_LIST_wordTexts)
        self.g_FS_frameSearch.g_QLE_input.setStyleSheet("background-color:white")
        __l_QHL_layout.addWidget(self.__l_QW_searchContainer)
        
        self.g_QCBB_changeType = QComboBox()
        self.g_QCBB_changeType.setFixedHeight(self.g_FS_frameSearch.height())
        self.g_QCBB_changeType.setCursor(Qt.CursorShape.PointingHandCursor)
        self.g_QCBB_changeType.setContentsMargins(0,0,0,0)
        self.g_QCBB_changeType.addItems(listType)
        self.g_QCBB_changeType.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        __l_QHL_layout.addWidget(self.g_QCBB_changeType)
        
        self.g_CS_core = CoreSearch(self)
    
    def hideSearch(self) -> None:
        self.hide()
        if self.g_CS_core.g_UI_ui != None:
            self.g_CS_core.g_UI_ui.hide()
    
    def showSearch(self) -> None:
        self.show()
        if self.g_CS_core.g_UI_ui != None:
            self.g_CS_core.g_UI_ui.show()
    
class CoreSearch:
    def __init__(self, searchUI : Search) -> None:
        self.__l_S_searchUI = searchUI
        self.g_UI_ui = None
        
        self.__l_S_searchUI.g_FS_frameSearch.g_LW_results.itemSelectionChanged.connect(lambda : self.__grapDisplay())        
        self.__l_S_searchUI.g_QCBB_changeType.currentIndexChanged.connect(lambda : self.updateList())

    def __grapDisplay(self):
        if not FrameCheckConnection(self.__l_S_searchUI,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_S_searchUI.g_FS_frameSearch.g_I_pos == -1 : return
        
        if self.__l_S_searchUI.g_QCBB_changeType.currentText().__eq__("Eng - Viet"):
            self.__l_S_searchUI.hide()
            self.g_UI_ui = WordUI(self.__l_S_searchUI.g_QCBB_changeType.currentText(), self.__l_S_searchUI, self.__l_S_searchUI.g_LW_listWords.getWord(self.__l_S_searchUI.g_LW_listWords.g_LIST_wordTexts[self.__l_S_searchUI.g_FS_frameSearch.g_I_pos]))
            
        if self.__l_S_searchUI.g_QCBB_changeType.currentText().__eq__("Grammar"):
            self.__l_S_searchUI.hide()
            self.g_UI_ui = GrammarUI(self.__l_S_searchUI.g_QCBB_changeType.currentText(),self.__l_S_searchUI, self.__l_S_searchUI.g_LG_listGrammars.getGrammar(self.__l_S_searchUI.g_LG_listGrammars.g_LIST_grammarTexts[self.__l_S_searchUI.g_FS_frameSearch.g_I_pos]))
        
        if self.__l_S_searchUI.g_QCBB_changeType.currentText().__eq__("Collection"):
            self.__l_S_searchUI.hide()
            self.g_UI_ui = CollectionUI(self.__l_S_searchUI.g_QCBB_changeType.currentText(), self.__l_S_searchUI, self.__l_S_searchUI.g_LC_listCOllections.getCollection(self.__l_S_searchUI.g_LC_listCOllections.g__LIST_collectionText[self.__l_S_searchUI.g_FS_frameSearch.g_I_pos]))

    def updateList(self):
        if self.__l_S_searchUI.g_QCBB_changeType.currentText().__eq__("Eng - Viet"):
            self.__l_S_searchUI.g_FS_frameSearch.updateListSearch(self.__l_S_searchUI.g_LW_listWords.g_LIST_wordTexts)
            
        elif self.__l_S_searchUI.g_QCBB_changeType.currentText().__eq__("Grammar"):
            self.__l_S_searchUI.g_FS_frameSearch.updateListSearch(self.__l_S_searchUI.g_LG_listGrammars.g_LIST_grammarTexts)

        elif self.__l_S_searchUI.g_QCBB_changeType.currentText().__eq__("Collection"):
            self.__l_S_searchUI.g_FS_frameSearch.updateListSearch(self.__l_S_searchUI.g_LC_listCOllections.g__LIST_collectionText)
    
class BaseShowing(FrameWindows):
    def __init__(self, parent: QWidget | None = ..., listData : list | None = ..., type : str | None = ...) -> None:
        super().__init__(parent)
        self.g_QW_containerShowing.setFixedHeight(self.height() * 95 / 100)
        
        __l_QVL_layout = QVBoxLayout()
        __l_QVL_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        __l_QVL_layout.setSpacing(0)
        __l_QVL_layout.setContentsMargins(0,0,0,0)
        self.g_QW_containerShowing.setLayout(__l_QVL_layout)
        self.g_QW_containerShowing.setStyleSheet("background-color:white")
        
        __l_QHL_layoutSearch = QHBoxLayout()
        __l_QVL_layout.addLayout(__l_QHL_layoutSearch)
        self.__l_QW_containerSearch = QWidget()
        self.__l_QW_containerSearch.setStyleSheet("background-color:None")
        self.__l_QW_containerSearch.setFixedWidth(parent.width() * 93 / 100)
        self.__l_QW_containerSearch.setFixedHeight(parent.height() * 4 / 100)
        self.g_FS_searching = FrameSearch(self.__l_QW_containerSearch, listData)
        self.g_FS_searching.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__l_QL_type = QLabel(text=type)
        self.__l_QL_type.setFont(QFont("Times New Roman", 12))
        __l_QHL_layoutSearch.addWidget(self.__l_QW_containerSearch)
        __l_QHL_layoutSearch.addWidget(self.__l_QL_type)
        
        self.g_FS_showing = FrameScroll(self.g_QW_containerShowing)
        self.g_FS_showing.g_QSA_container.setWidgetResizable(True)
        __l_QVL_layout.addWidget(self.g_FS_showing)
        
    def getUI(self) -> QWidget:
        return self
        
class WordUI(BaseShowing):
    def __init__(self, type : str | None = ... , searchUI : Search | None = ..., word  : Word | None = ...) -> None:
        self.g_S_searchUI = searchUI
        super().__init__(searchUI.parentWidget(), searchUI.g_LW_listWords.g_LIST_wordTexts, type)
        
        def exit():
            searchUI.show()
            searchUI.g_CS_core.g_UI_ui = None
            
        self.g_B_exit.clicked.connect(lambda : exit())
        self.__l_QW_showing = QWidget()
        self.grapWord(word)
        
        CoreWordUI(self)
        self.show()
        
    def grapWord(self, word : Word):
        self.__l_QW_showing.deleteLater()
        self.__l_QW_showing = QWidget()
        self.__l_QW_showing.setFixedWidth(self.g_FS_showing.width() * 99.8 / 100)
        __l_QFL_showing = QFormLayout()
        __l_QFL_showing.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QW_showing.setLayout(__l_QFL_showing)
        
        # DISPLAY WORD AND SOUND
        __l_QHL_wordAndSound = QHBoxLayout()
        __l_QL_word = QLabel(text=word.word)
        __l_QL_word.setFont(QFont("Roboto",25))
        __l_QL_word.setFixedSize(__l_QL_word.sizeHint())
        __l_QHL_wordAndSound.addWidget(__l_QL_word)
        
        if word.audio.__ne__("No sound"):
            __l_QPB_audio = QPushButton()
            __l_QPB_audio.setIcon(QPixmap(getPathFileImage("audio-speaker-on.png")))
            __l_QPB_audio.setCursor(Qt.CursorShape.PointingHandCursor)
            __l_QPB_audio.setStyleSheet("background-color:None")
            __l_QPB_audio.setToolTip("Audio")
            __l_QPB_audio.clicked.connect(lambda : play(word.audio))
            __l_QPB_audio.setFixedSize(__l_QPB_audio.sizeHint())
            __l_QHL_wordAndSound.addWidget(__l_QPB_audio, alignment=Qt.AlignmentFlag.AlignRight)
            
        __l_QFL_showing.addRow(__l_QHL_wordAndSound)
        
        # DISPLAY PRONUNCIATION
        if word.pronunciation.__ne__("None"):
            __l_QL_pronunciation = QLabel(text=word.pronunciation)
            __l_QL_pronunciation.setFont(QFont("Roboto",8, italic=True))
            __l_QFL_showing.addRow(__l_QL_pronunciation)
        
        #DISPLAY PART OF SPEECH
        __l_QL_partOfSpeech = QLabel(text=f"{word.partOfSpeech} \n")
        __l_QL_partOfSpeech.setFont(QFont("Roboto",9))
        __l_QFL_showing.addRow(__l_QL_partOfSpeech)
        
        # DISPLAY FORMAL AND INFORMAL
        if word.fAi.__ne__("N/A"):
            __l_QL_fAi = QLabel(f"({word.fAi})")
            __l_QL_fAi.setFont(QFont("Roboto",10))
            __l_QFL_showing.addRow(__l_QL_fAi)
        
        # DISPLAY MEANING
        __l_QL_meaningAndExample = QLabel(text=convertFromChatToSearch(word.meaningAndExample))
        __l_QL_meaningAndExample.setFont(QFont("Roboto",11))
        __l_QL_meaningAndExample.setWordWrap(True)
        __l_QFL_showing.addRow(__l_QL_meaningAndExample)
        
        # DISPLAY GRAMMAR
        if word.grammar.__ne__("No Grammar"):
            __l_QVL_grammar = QVBoxLayout()
            __l_QVL_grammar.setSpacing(0)
            
            __l_QL_titleGrammar = QLabel(text="GRAMMAR")
            __l_QL_titleGrammar.setStyleSheet("background-color:#ccd9ff")
            __l_QF_titleGrammar = QFont("ROboto",11)
            __l_QF_titleGrammar.setBold(True)
            __l_QF_titleGrammar.setUnderline(True)
            __l_QL_titleGrammar.setFont(__l_QF_titleGrammar)
            __l_QVL_grammar.addWidget(__l_QL_titleGrammar)
            
            __l_QL_grammar = QLabel(text=word.grammar)
            __l_QL_grammar.setStyleSheet("background-color:#ccd9ff")
            __l_QL_grammar.setFont(QFont("Roboto",11))
            __l_QVL_grammar.addWidget(__l_QL_grammar)
            
            __l_QFL_showing.addRow(__l_QVL_grammar)
            
        # DISPLAY SYNONYM
        if word.synonym.__ne__("No Synonym"):
            __l_QVL_synomym = QVBoxLayout()
            __l_QVL_synomym.setSpacing(0)
            
            __l_QL_titleSynonym = QLabel(text="SYNONYM")
            __l_QL_titleSynonym.setStyleSheet("background-color:#d6d6f5")
            __l_QF_titleSynonym = QFont("Roboto",11)
            __l_QF_titleSynonym.setBold(True)
            __l_QF_titleSynonym.setUnderline(True)
            __l_QL_titleSynonym.setFont(__l_QF_titleSynonym)
            __l_QVL_synomym.addWidget(__l_QL_titleSynonym)
            
            __l_QL_synonym = QLabel(text=word.synonym)
            __l_QL_synonym.setFont(QFont("Roboto",11))
            __l_QL_synonym.setStyleSheet("background-color:#d6d6f5")
            __l_QVL_synomym.addWidget(__l_QL_synonym)
            
            __l_QFL_showing.addRow(__l_QVL_synomym)
        
        self.g_FS_showing.grapWithWidget(self.__l_QW_showing)
        
class CoreWordUI:
    def __init__(self, wordUI : WordUI) -> None:
        self.__l_WU_wordUI = wordUI

        self.__l_WU_wordUI.g_FS_searching.g_LW_results.itemSelectionChanged.connect(lambda: self.grapWord())
        
    def grapWord(self):
        if not FrameCheckConnection(self.__l_WU_wordUI,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_WU_wordUI.g_FS_searching.g_I_pos == -1 : return
        
        self.__l_WU_wordUI.grapWord(self.__l_WU_wordUI.g_S_searchUI.g_LW_listWords.getWord(self.__l_WU_wordUI.g_S_searchUI.g_LW_listWords.g_LIST_wordTexts[self.__l_WU_wordUI.g_FS_searching.g_I_pos]))
        
class GrammarUI(BaseShowing):
    def __init__(self, type: str , searchUI : Search, grammar : Grammar) -> None:
        self.g_S_searchUI = searchUI
        super().__init__(searchUI.parentWidget(), searchUI.g_LG_listGrammars.g_LIST_grammarTexts, type)
        
        def exit():
            searchUI.show()
            searchUI.g_CS_core.g_UI_ui = None
            
        self.g_B_exit.clicked.connect(lambda : exit())
        
        self.__l_QW_showing = QWidget()
        self.grapGrammar(grammar)
        
        CoreGramamrUI(self)
        self.show()
        
    def grapGrammar(self, grammar : Grammar):
        self.__l_QW_showing.deleteLater()
        self.__l_QW_showing = QWidget()
        self.__l_QW_showing.setFixedWidth(self.g_FS_showing.width() * 99.8 / 100)
        
        __l_QVL_showing = QVBoxLayout()
        __l_QVL_showing.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QW_showing.setLayout(__l_QVL_showing)
        
        __l_QL_grammar = QLabel(text=grammar.nameOfGrammar.upper())
        __l_QL_grammar.setWordWrap(True)
        __l_QL_grammar.setFont(QFont("Roboto",25))
        __l_QVL_showing.addWidget(__l_QL_grammar)
        
        __l_QL_caseAndExample = QLabel(text=grammar.caseAndExampe)
        __l_QL_caseAndExample.setWordWrap(True)
        __l_QL_caseAndExample.setFont(QFont("Roboto",11))
        __l_QVL_showing.addWidget(__l_QL_caseAndExample)
        
        self.g_FS_showing.grapWithWidget(self.__l_QW_showing)
        
class CoreGramamrUI:
    def __init__(self, grammarUI : GrammarUI) -> None:
        self.__l_GU_grammarUI = grammarUI
        
        self.__l_GU_grammarUI.g_FS_searching.g_LW_results.itemSelectionChanged.connect(lambda : self.__grapGrammar())
        
    def __grapGrammar(self):
        if not FrameCheckConnection(self.__l_GU_grammarUI,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_GU_grammarUI.g_FS_searching.g_I_pos == -1 : return
        
        self.__l_GU_grammarUI.grapGrammar(self.__l_GU_grammarUI.g_S_searchUI.g_LG_listGrammars.getGrammar(self.__l_GU_grammarUI.g_S_searchUI.g_LG_listGrammars.g_LIST_grammarTexts[self.__l_GU_grammarUI.g_FS_searching.g_I_pos]))

class CollectionUI(BaseShowing):
    def __init__(self, type : str ,searchUI : Search, collection : Collection) -> None:
        self.g_S_searchUI = searchUI
        super().__init__(searchUI.parentWidget(), searchUI.g_LC_listCOllections.g__LIST_collectionText, type)
        
        def exit():
            searchUI.show()
            searchUI.g_CS_core.g_UI_ui = None
            
        self.g_B_exit.clicked.connect(lambda: exit())
        
        self.__l_QW_showing = QWidget()
        self.grapCollection(collection)
        
        CoreCollectionUI(self)
        self.show()
    
    def grapCollection(self, collection : Collection):
        self.__l_QW_showing.deleteLater()
        self.__l_QW_showing = QWidget()
        self.__l_QW_showing.setFixedWidth(self.g_FS_showing.width() * 99.8 / 100)
        
        __l_QVL_showing = QVBoxLayout()
        __l_QVL_showing.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QW_showing.setLayout(__l_QVL_showing)
        
        __l_QL_nameOfCollection = QLabel(text=collection.nameOfCollection.upper())
        __l_QL_nameOfCollection.setFont(QFont("Roboto", 25))
        __l_QL_nameOfCollection.setWordWrap(True)
        __l_QVL_showing.addWidget(__l_QL_nameOfCollection)
        
        __l_QL_collections = QLabel(text=collection.collections)
        __l_QL_collections.setWordWrap(True)
        __l_QL_collections.setFont(QFont("Roboto",11))
        __l_QVL_showing.addWidget(__l_QL_collections)
        
        self.g_FS_showing.grapWithWidget(self.__l_QW_showing)
        
class CoreCollectionUI:
    def __init__(self, collectionUI : CollectionUI) -> None:
        self.__l_CU_collectionUI = collectionUI
        
        self.__l_CU_collectionUI.g_FS_searching.g_LW_results.itemSelectionChanged.connect(lambda : self.__grapCollection())
        
    def __grapCollection(self):
        if not FrameCheckConnection(self.__l_CU_collectionUI,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        if self.__l_CU_collectionUI.g_FS_searching.g_I_pos == -1 : return
        
        self.__l_CU_collectionUI.grapCollection(self.__l_CU_collectionUI.g_S_searchUI.g_LC_listCOllections.getCollection(self.__l_CU_collectionUI.g_S_searchUI.g_LC_listCOllections.g__LIST_collectionText[self.__l_CU_collectionUI.g_FS_searching.g_I_pos]))