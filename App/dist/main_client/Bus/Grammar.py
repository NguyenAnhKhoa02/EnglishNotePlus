from Dal.Grammar import GrammarDB

import difflib

class Grammar:
    def __init__(self, nameOfGrammar : str | None = "", relative : str | None = "", caseAndExample : str | None = "") -> None:
        self.nameOfGrammar = nameOfGrammar.lower().strip()
        self.relative = relative
        self.caseAndExampe = caseAndExample
        
    def to_dict(self) -> dict:
        return {"NameOfGrammar" : self.nameOfGrammar.lower().strip(),
                "Relative" : self.relative,
                "CaseAndExample" : self.caseAndExampe}
        
    def from_dict(self, dict : dict):
        self.nameOfGrammar = dict.get("NameOfGrammar")
        self.relative = dict.get("Relative")
        self.caseAndExampe = dict.get("CaseAndExample")
        
        return self
        
class ListGrammar:
    def __init__(self):
        self.__l_GD_grammar = GrammarDB()
        self.g_LIST_grammarTexts = self.__l_GD_grammar.getAllDocument()
        
    def getGrammar(self, grammar : str) ->Grammar:
        __l_G_grammar = Grammar()
        __l_G_grammar.from_dict(self.__l_GD_grammar.getAllDataInDocument(grammar))
        return __l_G_grammar
    
    def deleteData(self, nameOfGrammar : str):
        self.g_LIST_grammarTexts.remove(nameOfGrammar)
        self.__l_GD_grammar.deleteData(nameOfGrammar)
    
    def saveData(self, nameOfGrammar : str, relative : str, caseExample : str):
        self.g_LIST_grammarTexts.append(nameOfGrammar.lower())
        self.g_LIST_grammarTexts.sort()
        
        self.__l_GD_grammar.saveData(Grammar(nameOfGrammar,relative,caseExample))
        
    def updateGrammar(self,nameOfGrammarOriginal ,nameOfGrammar : str, relative : str, caseAndExample : str):
        self.g_LIST_grammarTexts[self.g_LIST_grammarTexts.index(nameOfGrammarOriginal)] = nameOfGrammar
        self.g_LIST_grammarTexts.sort()
        
        self.__l_GD_grammar.deleteData(nameOfGrammarOriginal)
        self.__l_GD_grammar.saveData(Grammar(nameOfGrammar, relative, caseAndExample))
        
    def searchRelativeGrammar(self, nameOfGrammar : str) -> list:
        __l_LIST_relative = [data for data in self.g_LIST_grammarTexts if nameOfGrammar in data]
        
        return __l_LIST_relative