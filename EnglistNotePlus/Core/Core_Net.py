import requests
from Core.Core_Audio import *
import os
import webbrowser

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}
TIMEOUT = 60

def dowloadFile(url : str) -> None:
    r = requests.get(url,headers=HEADERS)
    
    with open(getPathFileAudio(os.path.basename(url).title()),'wb') as f:
        f.write(r.content)  

def checkConnection(url : str) -> bool:
    try:
        requests.head(url, timeout=TIMEOUT, headers=HEADERS)
        return True
    except:
        return False
    

def openBrowserWord(question) -> None:
    webbrowser.open(f"https://dictionary.cambridge.org/dictionary/english/{question}")
    
def openBrowserFindImages(question) -> None:
    webbrowser.open(f"https://www.google.com/search?q={question}&hl=vi&tbm=isch&source=hp&biw=1280&bih=648&ei=VAC5ZIuxNYbh-Abc-pK4Cg&iflsig=AD69kcEAAAAAZLkOZMWAKgKWaOM9wbUJm9_D-lqVZV1z&ved=0ahUKEwiLq7yq_pyAAxWGMN4KHVy9BKcQ4dUDCAc&uact=5&oq=attic&gs_lp=EgNpbWciBWF0dGljMggQABiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEi_FFDqCVjWEnAAeACQAQCYAWygAY0EqgEDMS40uAEDyAEA-AEBigILZ3dzLXdpei1pbWeoAgA&sclient=img")
    
def openBrowserFindInGoogle(question) -> None:
    webbrowser.open(f"https://www.google.com/search?q={question}&sxsrf=AB5stBg2B1NG2zG9C4v0K0Aw8ITBKags_Q%3A1689993636092&source=hp&ei=pEG7ZNLRA_am1e8Pg7iPqA8&iflsig=AD69kcEAAAAAZLtPtOTUI4EO6SrxLTuPlETfRKW6SQGA&ved=0ahUKEwjSs-bypKGAAxV2U_UHHQPcA_UQ4dUDCAk&uact=5&oq=allo&gs_lp=Egdnd3Mtd2l6IgRhbGxvMgcQABiKBRhDMggQABiABBixAzIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgsQLhiABBixAxiDATIIEAAYgAQYsQMyBRAAGIAESPYFUABYAHAAeACQAQCYAboBoAG6AaoBAzAuMbgBA8gBAIgGAQ&sclient=gws-wiz")