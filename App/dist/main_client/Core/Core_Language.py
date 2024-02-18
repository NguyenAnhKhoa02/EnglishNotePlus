import enchant

__g_LIST_es = ["o","ch","sh","th","ss","gh","z"]
__g_LIST_vowel = ["a","o","e","u","i"]

g_LIST_convert = ["Present form", "Past form", "Plural noun",
                  "Continuous form", "Suffix (-able)", "Suffix (-ible)",
                  "Suffix (-ness)", "Suffix (-ity)", "Suffix (-ment)"]
g_LIST_convert.sort()

enlish_dict = enchant.Dict("en_US")

def isEnglish(string : str) -> bool:
    return enlish_dict.check(string)

def convertWord(word : str, type : str) -> str:
    """Return the word was changed by recommended

    Args:
        word (str): the word that will be changed
        type (str): type of the word will chage to

    Returns:
        str
    """
    
    __l_STR_wordConvert = word.lower().strip()
    isConvert = False
    
    match type.lower():
        case "present form":
            if __l_STR_wordConvert[-1].__eq__("y"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "ies"
                isConvert = True
                
            if not isConvert:
                for es in __g_LIST_es:
                    if __l_STR_wordConvert.endswith(es):
                        isConvert = True
                        __l_STR_wordConvert += "es"
                        break
                    
            if not isConvert:
                __l_STR_wordConvert += "s"
                
            __l_STR_wordConvert += " (present)"
        
        case "plural noun":
            if __l_STR_wordConvert[-1].__eq__("y"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "ies"
                isConvert = True
                
            if not isConvert:
                for es in __g_LIST_es:
                    if __l_STR_wordConvert.endswith(es):
                        isConvert = True
                        __l_STR_wordConvert += "es"
                        break
                    
            if not isConvert:
                __l_STR_wordConvert += "s"
                
            __l_STR_wordConvert += " (plural noun)"
        
        case "past form":
            if __l_STR_wordConvert[-1].__eq__("y"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "i"
            elif __l_STR_wordConvert[-1].__eq__("e"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                
            __l_STR_wordConvert += "ed (V2 and V3)" 
            
        case "continuous form":
            if __l_STR_wordConvert[-1].__eq__("e"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
            
            __l_STR_wordConvert += "ing (continuous)"
            
        case "suffix (-able)": 
            if __l_STR_wordConvert[-1].__eq__("e") and not __l_STR_wordConvert.endswith("ce") and not __l_STR_wordConvert.endswith("ge") and not __l_STR_wordConvert.endswith("ate"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
            elif __l_STR_wordConvert[len(__l_STR_wordConvert) - 2] in __g_LIST_vowel:
                __l_STR_wordConvert += __l_STR_wordConvert[-1]
            elif __l_STR_wordConvert.endswith("ate"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-3]
            elif __l_STR_wordConvert.endswith("y"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "i"
                
            
            __l_STR_wordConvert += "able (adjective)"
            
        case "suffix (-ible)":
            if __l_STR_wordConvert.endswith("e"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
            elif __l_STR_wordConvert.endswith("mit"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "ss"
            elif __l_STR_wordConvert.endswith("nd"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "s"
                
            __l_STR_wordConvert += "ible (adjective)"
            
        case "suffix (-ness)":
            if __l_STR_wordConvert.endswith("y"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                __l_STR_wordConvert += "i"
                
            __l_STR_wordConvert += "ness (noun)"
            
        case "suffix (-ity)":
            if __l_STR_wordConvert.endswith("ble"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-2]
                __l_STR_wordConvert += "il"
            elif __l_STR_wordConvert.endswith("e"):
                __l_STR_wordConvert = __l_STR_wordConvert[:-1]
            elif __l_STR_wordConvert.endswith("ous"):
                __l_STR_wordConvert = __l_STR_wordConvert [:-3]
                
            __l_STR_wordConvert += "ity (noun)"
            
        case "suffix (-ment)":
            if __l_STR_wordConvert.endswith("y"):
                if __l_STR_wordConvert[len(__l_STR_wordConvert) - 2] not in __g_LIST_vowel:
                    __l_STR_wordConvert = __l_STR_wordConvert[:-1]
                    __l_STR_wordConvert += "i"
                    
            __l_STR_wordConvert += "ment (noun)"
            
    return __l_STR_wordConvert