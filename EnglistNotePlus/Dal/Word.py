from Dal.Database import FireBase

class WordDB(FireBase):
    def __init__(self) -> None:
        super().__init__("Word")
    
    def getAllDocument(self) -> list:
        listWord = [data for data in super().getAllDocument()]
        return listWord
    
    def getAllDataInDocument(self, doc : str) -> dict:
        return self.g_collection.document(doc).get().to_dict()
    
    def saveData(self, word):
        self.g_collection.document(word.word.lower()).set(word.to_dict())
        
    def deleteData(self, word):
        self.g_collection.document(word).delete()
        
    def getAllWordsByMeaning(self, meaningSearch : str) -> list:
        __l_LIST_word = list()
        
        for doc in self.g_collection.stream():
            meaning = " ".join([mean for mean in doc.to_dict()["MeaningAndExample"].split("\n") if not str(mean).startswith("-")])
            word = doc.id
            
            meaning = meaning.replace(","," ")
            if meaning.lower().find(meaningSearch) > -1:
                __l_LIST_word.append(word)
            
        return __l_LIST_word