from PySide6.QtWidgets import (
    QApplication
)

from UI.client import Client 
from UI.initialization import initialization

if __name__ == "__main__":
    __l_QA_application = QApplication()
    
    __l_Init_initialization = initialization()
    if __l_Init_initialization.g_BOOL_Connection:
        __l_CLIENT_client = Client(__l_Init_initialization.g_listWords, 
                                   __l_Init_initialization.g_ListGrammars,
                                   __l_Init_initialization.g_ListCollections)
        __l_CLIENT_client.show()

    __l_QA_application.exec()
    
"""
VERSION: 
    NUMBER_OF_VERSION.COUNT_EACH_CHANGE.DAY
    
    START_DAY : 27 / 7 / 2023
    NUMBER_OF_VERSION : HAVE BIG UPDATE OR SPECIAL UPDATE
    
    COUNT_EACH_CHANGED : COUNT TIMES CHANGED EACH SPECIAL OR BIG UPDATE
    
    ENCODE VERSION
    DAY_IN_VERSION = 6 * DAY
    
    DECODE VERSION
    DAY = DAY_IN_VERSION / 6
"""
    
"""
    VERSION: BETA 1.2.16632138
    CHANGE FONT
    UPDATE UI FAMILY_WORD AND EXAMPLE_AND_MEANING
    DATE: 27/7/2023
"""

"""VERSION: BETA 1.2.1.18432138
   ADJUST FORM OF VERSION
   REMOVE CHAGNE "\\" TO "-" BEFORE SAVE TO DB AND CONVERT "-" TO "\\" WHEN READ FROM DB
   DATE: 30 / 7 / 2023
"""

"""VERSION: BETA 1.3.1.1692138
   FIX ONLY STORE STRING LOWER IN LIST WORD AND GRAMMAR
   ADD NEW FEATURE FREE_SEARCHING_WORD
   DATE: 2 / 8 / 2023

   EX:
    `search hello ====> open browser that include content about hello
"""

"""
   *BIG UPDATE
   VERSION: BETA 2.1.1.2892138
   DATE: 4 / 8 / 2023
   
   === SPECIAL ===:
   New_Core has been created: Core_Language which will work about "word" (ex: to change type of word)
   ===  END    ===
   
   Word has been altered: database, structure
   ==> To devide "familywords" into grammar and synonyms
   ==> Add feature "Auto change word" to "wordObject"
   ==> To adjust key "familywords" to new "wordObject"
   ==> To change all data of "word" in database
   ==> The UI display when setText from MS Word has been updated
   
   The FrameSearch will return result more exactly
"""

"""VERSION: BETA 2.2.1.3492138
   DATE: 5 / 8 / 2023
   
   Add feature find word from vietnamese
   ===> Text is vietnamese, detect and display words
"""

"""VERSION: BETA 3.1.5172138
   DATE: 6 / 8 / 2023
   
   === BIG UPDATE ===
   Add new topic "Collection"
   Update new form version
   ===> NUMBER_OF_VERSION.COUNT_EACH_CHANGE.DAY
   ===    END     ===
   
   Fix error UI message
"""
#
#
#
"""VERSION: BETA 3.1.5172138
   DATE: 7 / 8 / 2023
   
   === HOT FIX ===
   update new detect language : chage detect vietnamese to detect english
   update UI showing-chat
   ===   END   ===
"""

"""VERSION: BETA 3.2.8292138
   DATE: 13 / 8 / 2023
   
   === UPDATE ===
   update detect language: the detection vietnamese is more accurate
   update UI note:
    + to choose at least two data will set text partofspeech to qtextedit meaningAndExample
    + successfull message have to options:
      click OK to exit this add_new_object_screen
      click CANCEL to still in add_new_object_screen
   ===   END    ====
"""

"""VERSION: BETA 3.3.492138
   DATE: 15 / 8 / 2023
   
   ===   UPDATE   ===
   Change feature findMeaning to findMeaning and detect word
   ===    END     ===
"""

"""VERSION: BETA 4.0.13092138
   DATE: 21 / 8 / 2023
   
   ===   CHANGE   ===
   Alter propery of database:
   + Deleted "level", add new property formal_and_informal (fAi) instead
   ===    END     ===
   
   ===   UPDATE UI   ===
   Add new feature in note:
   + Show all data in combobox and display data of the word which was opted
   ===     END       ===
"""

#======================= VERSION OFFICIAL ===============================

"""VERSION: 1.0.3552138
   DATE: 5 / 9 /2023
   
   === ADD NEW FEATURES ===
   Search
   ===      END         ===
"""

"""VERSION: 1.1.6552138
   DATE: 10 / 9 / 2023
   
   ===   FIX   ===
   UI of search feature has been fixed
   Synchronous error between search feature and note - when add new data - has been fix
   ===   END   ===
"""