from Dal.Word import WordDB
import difflib

class Word:
    def __init__(self, word :str | None = "", partOfSpeech : str | None = "", fAi : str | None = "" , pronunciation : str | None = "",audio : str | None = "", grammar : str | None = "",synonym : str | None = "" ,meaningAndExample : str | None = "") -> None:
        self.word : str = word.lower().strip()
        self.partOfSpeech : str = partOfSpeech
        self.fAi : str = fAi
        self.pronunciation : str = pronunciation
        self.audio : str = audio
        self.grammar : str = grammar
        self.meaningAndExample : str = meaningAndExample
        self.synonym : str = synonym
        
    def to_dict(self)->dict:
        dictWord =   {"Word" : self.word.lower().strip(),
                      "PartOfSpeech" : self.partOfSpeech,
                      "fAi" : self.fAi,
                      "Pronunciation" : self.pronunciation,
                      "Audio" : self.audio,
                      "Grammar" : self.grammar,
                      "Synonyms" : self.synonym,
                      "MeaningAndExample" : self.meaningAndExample}   
        return dictWord
        
    def from_dict(self, dict  :dict):
        self.word = dict.get("Word")
        self.fAi = dict.get("fAi")
        self.pronunciation = dict.get("Pronunciation")
        self.audio = dict.get("Audio")
        self.grammar = dict.get("Grammar")
        self.synonym = dict.get("Synonyms")
        self.partOfSpeech = dict.get("PartOfSpeech")
        self.meaningAndExample = dict.get("MeaningAndExample")
        
        return self

class ListWords:
    def __init__(self) -> None:
        self.__l_WD_data = WordDB()
        self.g_LIST_wordTexts = self.__l_WD_data.getAllDocument()
    
    def getWord(self, word : str) -> Word:
        __l_word = Word()
        __l_word.from_dict(self.__l_WD_data.getAllDataInDocument(word))
        return __l_word
        
    def saveData(self, word :str, partOfSpeech : str, fAi : str , audio : str, pronunciation : str ,grammar : str, synonym : str ,meaningAndExample : str) -> None:
        if word not in self.g_LIST_wordTexts:
            self.g_LIST_wordTexts.append(word.lower())
            self.g_LIST_wordTexts.sort()
            
        __l_word = Word(word,partOfSpeech,fAi,pronunciation,audio,grammar,synonym,meaningAndExample)
        
        self.__l_WD_data.saveData(__l_word)
        
    def updateData(self,wordOriginal : str ,word :str, partOfSpeech : str, fAi : str , audio : str, pronunciation : str ,grammar : str, synosnym : str,meaningAndExample : str) -> None:
        self.g_LIST_wordTexts[self.g_LIST_wordTexts.index(wordOriginal)] = word
        self.g_LIST_wordTexts.sort()
        
        self.__l_WD_data.deleteData(wordOriginal)
        __l_word = Word(word,partOfSpeech,fAi,pronunciation,audio,grammar, synosnym,meaningAndExample)            
        
        self.__l_WD_data.saveData(__l_word)
        
    def deleteData(self, wordOriginal : str):
        self.g_LIST_wordTexts.remove(wordOriginal)
        self.__l_WD_data.deleteData(wordOriginal)
        
    def searchWordsInRelative(self, word : str) ->list:
        """search the text that exists in list

        Args:
            word (str): word exists in list

        Returns:
            list: list contain all relative words
        """
        
        return difflib.get_close_matches(word,self.g_LIST_wordTexts)

    def findWordFromMeaning(self, meaningSearch : str) -> list:
        
        return self.__l_WD_data.getAllWordsByMeaning(meaningSearch)