from Core.Core_UI import *
from Core.FrameWork import *
from Core.Core_QSS import *
from Core.Core_Image import *
from Core.Core_Language import *
from Core.FrameWork import FrameChat
from Bus.Word import Word, ListWords
from Bus.Grammar import Grammar, ListGrammar
from Bus.Collection import Collection, ListCollection
from Core.Core_Audio import *
import asyncio

class Chat(QWidget):
    """UI OF CHAT

    Args:
        QWidget (_type_): _description_
    """
    
    def __init__(self, parent: QWidget | None = ..., listWords : ListWords | None =..., listGrammars : ListGrammar | None = ..., listCollections : ListCollection | None = ...) -> None:
        super().__init__(parent)
        self.setFixedSize(parent.size())
        self.setObjectName("Chat")
        self.g_LW_words = listWords
        self.g_LG_grammars = listGrammars
        self.g_LC_collections = listCollections
        setQSS(self,"chat.qss")
        
        self.__l_QVL_layout = QVBoxLayout()
        self.__l_QVL_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__l_QVL_layout.setContentsMargins(0,0,0,0)
        self.__l_QVL_layout.setSpacing(0)
        self.setLayout(self.__l_QVL_layout)
        
        # topic
        self.__l_QW_containerTopics = QWidget()
        self.__l_QW_containerTopics.setObjectName("topic")
        self.__l_QW_containerTopics.setFixedSize(self.width(),
                                                 self.height() * 5 / 100)
        self.g_QL_topic = QLabel(self.__l_QW_containerTopics)
        self.g_QL_topic.setFixedHeight(self.__l_QW_containerTopics.height())
        self.g_QL_topic.setText("TOPIC: WORD")
        self.g_QL_topic.setObjectName("topic")
        self.__l_QVL_layout.addWidget(self.__l_QW_containerTopics)
        
        # showing chat
        self.__l_QW_containerShowingChat = QWidget()
        self.__l_QW_containerShowingChat.setFixedSize(self.width(),
                                                      self.height() * 90 / 100)
        self.g_FS_showingChat = FrameScroll(self.__l_QW_containerShowingChat)
        self.g_FS_showingChat.g_QSA_container.setObjectName("showingChat")
        
        self.__l_QVL_layout.addWidget(self.__l_QW_containerShowingChat)
        
        # chatting
        self.__l_QW_containerChatting = QWidget()
        self.__l_QW_containerChatting.setFixedSize(self.width(),
                                                   self.height() * 5 / 100)
        self.__l_QHL_containerChatting = QHBoxLayout()
        self.__l_QHL_containerChatting.setContentsMargins(0,0,0,10)
        self.__l_QHL_containerChatting.setSpacing(1)
        self.__l_QW_containerChatting.setLayout(self.__l_QHL_containerChatting)
        self.g_QLE_inputChatting = QLineEdit()
        self.g_QLE_inputChatting.setObjectName("inputChatting")
        self.g_QLE_inputChatting.setFixedHeight(self.__l_QW_containerChatting.height())
        self.g_QLE_inputChatting.setPlaceholderText("Chatting...")
        self.__l_QHL_containerChatting.addWidget(self.g_QLE_inputChatting)
        self.g_QPB_chatting = QPushButton()
        self.g_QPB_chatting.setFixedHeight(self.__l_QW_containerChatting.height())
        self.g_QPB_chatting.setFixedWidth(30)
        self.g_QPB_chatting.setToolTip("send")
        self.g_QPB_chatting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.g_QPB_chatting.setIcon(QPixmap(getPathFileImage("send.png")))
        self.__l_QHL_containerChatting.addWidget(self.g_QPB_chatting)
        self.__l_QVL_layout.addWidget(self.__l_QW_containerChatting)
        
        CoreChat(self)
    
class CoreChat:
    def __init__(self, chatting : Chat):
        self.__l_CHAT_chatting = chatting
        self.__l_LIST_chatting = list()
        self.__l_WORD_current = Word()
        self.__l_GRAMMAR_current = Grammar()
        self.__l_STR_wordSearch = ""
        self.__l_STR_topic = "word"
        
        self.__l_FC_FrameChat = FrameChat()
        self.__l_FC_FrameChat.setToppic(self.__l_STR_topic)
        
        self.__l_CHAT_chatting.g_QPB_chatting.clicked.connect(lambda: self.grapChatting())
        self.__l_CHAT_chatting.g_QPB_chatting.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__l_CHAT_chatting.g_QLE_inputChatting.returnPressed.connect(self.__l_CHAT_chatting.g_QPB_chatting.click)
        self.__l_CHAT_chatting.g_QLE_inputChatting.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        
    def grapChatting(self):
        if not FrameCheckConnection(self.__l_CHAT_chatting,"https://console.firebase.google.com/project/englishnoteplus/overview").g_BOOL_connect:
            return
        
        __l_STR_textChat = self.__l_CHAT_chatting.g_QLE_inputChatting.text().strip().lower()
        
        if __l_STR_textChat == "": return
        
        # showing send
        __l_LABEL_showingSend = QLabel(__l_STR_textChat)
        __l_LABEL_showingSend.setContentsMargins(0,5,0,5)
        __l_LABEL_showingSend.setObjectName("showingSend")
        __l_LABEL_showingSend.setFixedWidth(self.__l_CHAT_chatting.width())
        __l_LABEL_showingSend.setFixedHeight(__l_LABEL_showingSend.sizeHint().height())
        
        self.__l_LIST_chatting.append(__l_LABEL_showingSend)
        
        # showing receive word
        __l_LABEL_showingReceive = QLabel()
        __l_LABEL_showingReceive.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        __l_LABEL_showingReceive.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        __l_LABEL_showingReceive.setObjectName("showingReceive")
        __l_LABEL_showingReceive.setContentsMargins(0,5,0,5)
        __l_LABEL_showingReceive.setFixedWidth(self.__l_CHAT_chatting.width() * 99.8 / 100)
        __l_LABEL_showingReceive.setWordWrap(True)
        
        if self.__detectKeyControl(__l_STR_textChat, __l_LABEL_showingReceive):
            pass
        elif self.__findWordFromMeaningAndDetectWord(__l_STR_textChat, __l_LABEL_showingReceive):
            pass
        elif __l_STR_textChat.lower().startswith("`topic"):
            self.__changedTopic(__l_STR_textChat,__l_LABEL_showingReceive)
        elif self.__l_STR_topic.lower().__eq__("word"):
            self.__resolveWord(__l_STR_textChat, __l_LABEL_showingReceive)
        elif self.__l_STR_topic.lower().__eq__("grammar"):
            self.__resolveGrammar(__l_STR_textChat,__l_LABEL_showingReceive)
        elif self.__l_STR_topic.lower().__eq__("collection"):
            self.__resolveCollection(__l_STR_textChat, __l_LABEL_showingReceive)

        if __l_LABEL_showingReceive.layout().__class__.__name__.__ne__("QVBoxLayout"):
            __l_LABEL_showingReceive.setFixedHeight(__l_LABEL_showingReceive.sizeHint().height())
            
        self.__l_LIST_chatting.append(__l_LABEL_showingReceive)
        self.__l_CHAT_chatting.g_FS_showingChat.grapRenderWithListWidget(self.__l_LIST_chatting)
        self.__l_CHAT_chatting.g_QLE_inputChatting.setText("")
        self.__l_CHAT_chatting.g_QLE_inputChatting.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    
    def __changedTopic(self,textChat : str ,labelReceive : QLabel): 

        if len(textChat.split(" ")) == 1:
            labelReceive.setText(
                "To change topic to word, text \" topic word \"\n"
                "To change topic to grammar, text \" topic grammar \n"
                "To change topic to collection, text \" topic grammar"
            )
        elif textChat.split(" ")[1].lower().__eq__("word"):
            self.__l_STR_topic = "word"
            self.__l_CHAT_chatting.g_QL_topic.setText("TOPIC: WORD")
            labelReceive.setText("Topic has been changed to: word")
        elif textChat.split(" ")[1].lower().__eq__("grammar"):
            self.__l_STR_topic = "grammar"
            self.__l_CHAT_chatting.g_QL_topic.setText("TOPIC: GRAMMAR")
            labelReceive.setText("Topic has been changed to: grammar")
        elif textChat.split(" ")[1].lower().__eq__("collection"):
            self.__l_STR_topic = "collection"
            self.__l_CHAT_chatting.g_QL_topic.setText("TOPIC: COLLECTION")
            labelReceive.setText("Topic has been changed to : collection")
        else:
            labelReceive.setText("I don't know this topic!")
            
        self.__l_FC_FrameChat.setToppic(self.__l_STR_topic)
            
        self.__l_CHAT_chatting.g_QL_topic.setFixedWidth(self.__l_CHAT_chatting.g_QL_topic.sizeHint().width())
    
    def __resolveWord(self, key : str, labelReceive  :QLabel) -> None:
        if key.lower().__eq__("`*") or key.lower().__eq__("`all"):
            labelReceive.setText(
                "All keys (start with`): \n"
                "is formal or isformal : display this wordis is formal or not \n"
                "meaning: display meaning of word \n"
                "part of speech or parhofspeech: display part-of-speech of word \n"
                "skill : display skill of word \n"
                "synonyms or synonym: display synonym of word \n"
                "grammar: display changing of word"
                "pronounce or audio or pronunciation : display pronunciation of word"
            )
            return
        
        # SHOW THE WORD THAT CANT'T SEARCH ABOUT THIS KEY WORD
        if key not in self.__l_CHAT_chatting.g_LW_words.g_LIST_wordTexts and self.__l_WORD_current.word.__ne__(key) and not key.startswith("`"):
            self.__l_STR_wordSearch = key
            self.__l_WORD_current.word = ""
            self.__l_FC_FrameChat.showDontKnow(key, labelReceive, 
                                                   textMessage= f"I don't know this word, you can search the word \"{key}\" in the internet")
            return
        
        # SHOW THE WORD THAT HAVE DATA
        if key in self.__l_CHAT_chatting.g_LW_words.g_LIST_wordTexts:
            self.__l_STR_wordSearch = key
            __l_I_listWord = self.__l_CHAT_chatting.g_LW_words.g_LIST_wordTexts.index(key)
            self.__l_WORD_current = self.__l_CHAT_chatting.g_LW_words.getWord(self.__l_CHAT_chatting.g_LW_words.g_LIST_wordTexts[__l_I_listWord])
            labelReceive.setText(self.__l_WORD_current.meaningAndExample)
            return
        
        # CHECK THE WORD CURRENT BEFORE ACTIVE KEY WORD
        if self.__l_WORD_current.word.__eq__(""):
            labelReceive.setText("What is the word are you saying?")
            return
        
        # SPLIT KEY AND HANDLE KEY WORD
        key = key.split("`")[1].lower()
        match key:
            case "meaning":
                labelReceive.setText(self.__l_WORD_current.meaningAndExample)
            case "partofspeech" | "part of speech":
                labelReceive.setText(self.__l_WORD_current.partOfSpeech)
            case "is formal" | "isformal":
                if self.__l_WORD_current.fAi.__eq__("formal"):
                    labelReceive.setText(f"This word is {self.__l_WORD_current.fAi}")
                else:
                    labelReceive.setText(self.__l_WORD_current.fAi)
            case "synonyms" | "synonym":
                labelReceive.setText(self.__l_WORD_current.synonym)
            case "grammar":
                labelReceive.setText(self.__l_WORD_current.grammar)
            case "pronunce" | "pronunciation" | "audio" | "voice":
                if self.__l_WORD_current.audio.__eq__("No sound"):
                    labelReceive.setText("I can't pronunce this word")
                else:
                    __l_QPB_audio = QPushButton(labelReceive)
                    __l_QPB_audio.setText(self.__l_WORD_current.pronunciation)
                    __l_QPB_audio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                    __l_QPB_audio.setToolTip(f"pronunce of the word : {self.__l_WORD_current.word}")
                    __l_STR_nameFile = self.__l_WORD_current.audio
                    __l_QPB_audio.clicked.connect(lambda : play(__l_STR_nameFile))
                    __l_QPB_audio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                    play(__l_STR_nameFile)
            case _:
                labelReceive.setText("Sorry! I don't understand your text!")
    
    def __resolveGrammar(self, key : str, labelReceive : QLabel):
        if key.lower().__eq__("`*") or key.lower().__eq__("`all"):
            labelReceive.setText(
                "All keys (start with`): \n"
                "relative or relativegramamrs : display about the relative gramamars\n"
                "caseandexample or case or example : display about the case and the example"
            )
            return
        
        # SHOW HINT
        if len(key) > 1 and not key.startswith("`"):
            __l_LIST_relativeGramamr = self.__l_CHAT_chatting.g_LG_grammars.searchRelativeGrammar(key.lower())
            if len(__l_LIST_relativeGramamr) > 0 and key not in self.__l_CHAT_chatting.g_LG_grammars.g_LIST_grammarTexts:
                self.__l_FC_FrameChat.showHint(key ,__l_LIST_relativeGramamr, labelReceive)
                return
        
        # CAN'T FIND THE WORD
        if key.lower() not in self.__l_CHAT_chatting.g_LG_grammars.g_LIST_grammarTexts and self.__l_GRAMMAR_current.nameOfGrammar.__ne__(key) and not key.lower().startswith("`"):
            self.__l_STR_wordSearch = key
            self.__l_FC_FrameChat.showDontKnow(key=key,
                                               labelReceive= labelReceive,
                                               textMessage= "You can search this grammar in the internet!")
            return
        
        # SHOW CASE AND GRAMMAR OF GRAMAMR
        if key.lower() in self.__l_CHAT_chatting.g_LG_grammars.g_LIST_grammarTexts:
            self.__l_STR_wordSearch = key
            __l_I_listGrammar = self.__l_CHAT_chatting.g_LG_grammars.g_LIST_grammarTexts.index(key)
            self.__l_GRAMMAR_current = self.__l_CHAT_chatting.g_LG_grammars.getGrammar(self.__l_CHAT_chatting.g_LG_grammars.g_LIST_grammarTexts[__l_I_listGrammar])
            labelReceive.setText(self.__l_GRAMMAR_current.caseAndExampe)
            return
            
        if self.__l_GRAMMAR_current.nameOfGrammar.__eq__(""):
            labelReceive.setText("What's the gramamr been talking?")
            return

        key = key.split("`")[1].lower()
        match key:
            case "relative" | "relativegrammars":
                labelReceive.setText(self.__l_GRAMMAR_current.relative)
            case "caseandexample" | "case" | "example":
                labelReceive.setText(self.__l_GRAMMAR_current.caseAndExampe)
            case _:
                labelReceive.setText("Sorry! I don't understand your text!")
    
    def __resolveCollection(self, key : str, labelReceive : QLabel) -> None:
        if key.__eq__("`*"):
            labelReceive.setText("This topic don't have any special key")
            return
        
        #SHOW HINT
        if len(key) > 1 and not key.startswith("`") and key not in self.__l_CHAT_chatting.g_LC_collections.g__LIST_collectionText: 
            __l_LIST_relative = self.__l_CHAT_chatting.g_LC_collections.findRelativeCollections(key)
            if len(__l_LIST_relative) > 0:
                self.__l_FC_FrameChat.showHint(key, __l_LIST_relative, labelReceive)
                return
        
        #SHOW DON'T KNOW COLLECTION
        if key not in self.__l_CHAT_chatting.g_LC_collections.g__LIST_collectionText:
            labelReceive.setText(f"Sorry, I don't know the collection namely \"{key}\"")
            return    

        #KNOW THE COLLECTION
        if key in self.__l_CHAT_chatting.g_LC_collections.g__LIST_collectionText:
            __l_STR_message = self.__l_CHAT_chatting.g_LC_collections.getCollection(key).collections
            labelReceive.setText(__l_STR_message)
    
    def __detectKeyControl(self, key  : str, labelReceive : QLabel) -> bool:
        """Resolve all key that will be run relative system

        Args:
            key (str): the key use to resolve
            labelReceive (QLabel): the label that will be showed

        Returns:
            bool: _description_
        """
        
        if key.lower().__eq__("`*control"):
            labelReceive.setText(
                "openbrowser or search: search the word on the page cambridge dictionary in the internet\n"
                "images or img or imgs : search the images of word in google image"
            )
            return True

        if self.__l_STR_wordSearch.__eq__("") and len(key.split(" ")) <= 1: return False
        
        if key.lower().startswith("`openbrowser") or key.lower().startswith("`search"):
            if len(key.split(" ")) > 1:
                keySearch = key.split(" ", 1)[1]
                
                if self.__l_STR_topic.lower().__eq__("word"):
                    labelReceive.setText(f"Searching word \"{keySearch}\"")
                    openBrowserWord(keySearch)
                elif self.__l_STR_topic.lower().__eq__("grammar"):
                    labelReceive.setText(f"Searching grammar \"{keySearch}\"")
                    openBrowserFindInGoogle(keySearch)
            else:
                if self.__l_STR_topic.lower().__eq__("word"):
                    labelReceive.setText(f"Searching word \"{self.__l_STR_wordSearch}\"")
                    openBrowserWord(self.__l_STR_wordSearch)
                elif self.__l_STR_topic.lower().__eq__("grammar"):
                    labelReceive.setText(f"Searching grammar \"{self.__l_STR_wordSearch}\"")
                    openBrowserFindInGoogle(self.__l_STR_wordSearch)
            return True

        elif key.lower().startswith("`images") or key.lower().startswith("`img") or key.lower().startswith("`imgs"):
            if len(key.split(" ",1)) > 1:
                print(key.split(" ",1))
                labelReceive.setText(f"Searching images for text \"{key.split(' ', 1)[1]}\"")
                openBrowserFindImages(key.split(" ", 1)[1])
            else:
                labelReceive.setText(f"Searching images for text \"{self.__l_STR_wordSearch}\"")
                openBrowserFindImages(self.__l_STR_wordSearch)
            return True
            
        return False

    def __findWordFromMeaningAndDetectWord(self, key :  str, labelReceive : QLabel) -> bool:
        """Check the word is have in list and return the results

        Args:
            key (str): the word is finding
            labelReceive (QLabel): label will display information

        Returns:
            bool: return false if the word is have in list or some others reason
        """
        
        if key.startswith("`"): return False
        
        if self.__l_STR_topic.lower().__ne__("word"): return False

        if key in self.__l_CHAT_chatting.g_LW_words.g_LIST_wordTexts: return False
        
        __l_STR_message = ""
        __l_LIST_relative = self.__l_CHAT_chatting.g_LW_words.searchWordsInRelative(key)

        if len(__l_LIST_relative) > 0:
            __l_STR_message += f"I know some words spell like this word: \n"
            __l_STR_message += "\n".join(__l_LIST_relative)
                
        __l_LIST_words = self.__l_CHAT_chatting.g_LW_words.findWordFromMeaning(key)
        
        if (len(__l_LIST_words)) > 0:
            if __l_STR_message.__ne__(""): __l_STR_message += "\n\n"
            
            __l_STR_message += f"I recognize the text \"{key}\" is same like meaning of some words: \n"
            __l_STR_message += "\n".join(__l_LIST_words)
            labelReceive.setText(__l_STR_message)
            
        if __l_STR_message.__eq__(""):
            if isEnglish(key):
                return False
            else:
                self.__l_FC_FrameChat.showDontKnow(key=key,
                                                   labelReceive=labelReceive,
                                                   textMessage="Sorry, I don't know this word, you can search it in the internet: ",
                                                   query= f"{key} tiếng anh gọi là gì")

        labelReceive.setText(__l_STR_message)
        return True