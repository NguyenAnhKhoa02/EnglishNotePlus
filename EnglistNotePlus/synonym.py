import os

import firebase_admin
from firebase_admin import credentials, firestore

from Bus.Word import Word
from Bus.Grammar import Grammar
from Bus.Collection import Collection

pathService1 = os.path.join(os.path.dirname(__file__),"serviceAccountKey.json")
cred1 = credentials.Certificate(pathService1)
firebase_admin.initialize_app(cred1)
db1 = firestore.client()
collection1 = db1.collection("Collection")

listWord = list()
for doc in collection1.stream():
    listWord.append(Collection().from_dict(doc.to_dict()))

pathService2 = os.path.join(os.path.dirname(__file__),"englishnoteplus-873c5-firebase-adminsdk-xxwz4-bb170d4a6a.json")
cred2 = credentials.Certificate(pathService2)

db2 = firestore.client(firebase_admin.initialize_app(cred2, name="second"))
collection2 = db2.collection("Collection")

for word in listWord:
    print(word.nameOfCollection)
    collection2.document(word.nameOfCollection).set(word.to_dict())