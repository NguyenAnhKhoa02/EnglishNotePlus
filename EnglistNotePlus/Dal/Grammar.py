from Dal.Database import FireBase

class GrammarDB(FireBase):
    def __init__(self) -> None:
        super().__init__("Grammar")
        
    def getAllDocument(self) -> list:
        return super().getAllDocument()
    
    def getAllDataInDocument(self, doc : str) -> dict:
        return self.g_collection.document(doc).get().to_dict()
        
    def deleteData(self, grammar):
        self.g_collection.document(grammar).delete()
        
    def saveData(self, grammar):
        self.g_collection.document(grammar.nameOfGrammar).set(grammar.to_dict())