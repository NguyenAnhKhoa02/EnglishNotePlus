from Dal.Database import FireBase

class CollectionDB(FireBase):
    def __init__(self: str) -> None:
        super().__init__("Collection")
        
    def getAllCollections(self) -> list:
        return super().getAllDocument()
    
    def getAllDataInDocument(self, doc : str) -> dict:
        return self.g_collection.document(doc).get().to_dict()
    
    def deleteData(self, collection):
        self.g_collection.document(collection).delete()
    
    def saveData(self, collection):
        self.g_collection.document(collection.nameOfCollection).set(collection.to_dict())