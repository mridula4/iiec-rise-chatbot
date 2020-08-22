import os
import pyttsx3 

print("Hello Mridu, I am Ron! your chat Bot")
pyttsx3.speak("Hello Mridu, I am Ron! your chat Bot")

    
while(True):
    print()
	
    print("Which service would you like to use: \t" ,end='')
    pyttsx3.speak("Which service would you like to use")
	
    p=input()

        
    if ("chrome" in p):
        os.system("chrome")
       
        
    elif  ("quick access" in p):
        os.system("start menu")
        
    elif ("editor" in p) or ("notepad++" in p):
        os.system("notepad++")
        
    elif ("linkedin" in p):
        os.system("chrome https://www.linkedin.com/in/mridula-gaba-46913215a/")
        
    elif ("gmail" in p):
        os.system("chrome www.gmail.com")
     
    elif ("exit" in p) or ("close" in p):
        print("It seems you want to exit! Happy to help you! Good Bye!")
        pyttsx3.speak("It seems you want to exit! Happy to help you! Good Bye!")
        break
           
    else:
        print("I am sorry, this service is not available")
        pyttsx3.speak("I am sorry, this service is not available")