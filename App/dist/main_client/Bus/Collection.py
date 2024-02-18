from Dal.Collection import CollectionDB
import difflib

class Collection:
    def __init__(self, nameOfCollection  :str | None = "", collections : str | None = "") -> None:
        self.nameOfCollection = nameOfCollection.lower().strip()
        self.collections = collections
        
    def to_dict(self):
        return {
            "NameOfCollection" : self.nameOfCollection.lower().strip(),
            "Collections" : self.collections
        }
        
    def from_dict(self, dict  :dict):
        self.nameOfCollection = dict.get("NameOfCollection")
        self.collections = dict.get("Collections")
        
        return self
    
class ListCollection:
    def __init__(self) -> None:
        self.__l_CD_collection = CollectionDB()
        self.g__LIST_collectionText = self.__l_CD_collection.getAllCollections()
        
    def getCollection(self, collection : str) -> Collection:
        __l_C_collection = Collection()
        __l_C_collection.from_dict(self.__l_CD_collection.getAllDataInDocument(collection))
        return __l_C_collection
    
    def saveCollection(self, nameOfCollection : str, collections : str):
        if not nameOfCollection in self.g__LIST_collectionText:
            self.g__LIST_collectionText.append(nameOfCollection.lower())
            self.g__LIST_collectionText.sort()
        
        self.__l_CD_collection.saveData(Collection(nameOfCollection, collections))
        
    def updateCollection(self, nameOfCollectionOriginal : str, nameOfCollection : str, collections : str):
        self.g__LIST_collectionText[self.g__LIST_collectionText.index(nameOfCollectionOriginal)] = nameOfCollection.lower()
        self.g__LIST_collectionText.sort()
        
        self.__l_CD_collection.deleteData(nameOfCollectionOriginal)
        self.__l_CD_collection.saveData(Collection(nameOfCollection, collections))
        
    def deleteCollection(self, nameOfCollectionOriginal : str):
        self.g__LIST_collectionText.remove(nameOfCollectionOriginal)
        self.__l_CD_collection.deleteData(nameOfCollectionOriginal)
        
    def findRelativeCollections(self, nameOfCollection : str) -> list:
        __l_STR_relative = [relative for relative in self.g__LIST_collectionText if nameOfCollection in relative]
        
        if len(__l_STR_relative) > 0:
            return __l_STR_relative
        return difflib.get_close_matches(nameOfCollection, self.g__LIST_collectionText)