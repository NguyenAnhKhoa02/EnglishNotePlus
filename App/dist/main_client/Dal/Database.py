import os

import firebase_admin
from firebase_admin import credentials, firestore

def init():
        pathService = os.path.join(os.path.dirname(__file__),"serviceAccountKey.json")
        cred = credentials.Certificate(pathService)
        app = firebase_admin.initialize_app(cred)

class FireBase:
    def __init__(self, collection : str) -> None:
        db = firestore.client()
        self.g_collection = db.collection(collection)
        
    def getAllDocument(self) -> list:
        self.__l_LIST_doc = list()
        
        for doc in self.g_collection.stream():
            self.__l_LIST_doc.append(f"{doc.id}")
            
        return self.__l_LIST_doc
    
    def saveData(self):
        pass