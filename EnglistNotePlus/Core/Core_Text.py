def getListBracket(text : str) -> list:
    listBrackets = list()
    
    coupleBracket = list()
    openBrakcet = 0
    for index in range(text.__len__()):
        if text[index].__eq__("("):
            if openBrakcet == 0: 
                coupleBracket.append(index)
                openBrakcet += 1
            else: 
                openBrakcet += 1
        if text[index].__eq__(")"):
           if openBrakcet == 1:
               coupleBracket.append(index)
               listBrackets.append(coupleBracket)
               openBrakcet = 0
               coupleBracket = list()
           elif openBrakcet > 1:
               openBrakcet -= 1
               
    return listBrackets
            
def convertFromChatToSearch(text : str) -> str:
    __l_LIST_waitConvert = text.split("\n")
    
    for count in range(__l_LIST_waitConvert.__len__()):
        __l_STR_convert = __l_LIST_waitConvert[count]
        
        if __l_STR_convert.startswith("-"):
            __l_LIST_brakcets = getListBracket(__l_STR_convert)
            
            if len(__l_LIST_brakcets) > 0:
                __l_STR_convert = __l_STR_convert[:__l_LIST_brakcets[-1][0]] + "\n" + " " + __l_STR_convert[__l_LIST_brakcets[-1][0] + 1 :]
                __l_STR_convert = __l_STR_convert[:__l_LIST_brakcets[-1][1] + 1] + "\n"
                
            __l_LIST_waitConvert[count] = __l_STR_convert

    return "\n".join(__l_LIST_waitConvert)