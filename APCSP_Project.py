#################################################
# AI downsides can negatively affect the internet 
#################################################

from characters import Characters
import os
import time
from info import main_info

# Values
Loop = True
Main = True
Credits = False
Info = False

while Main == True:

    while Credits == True:
        os.system('clear')
        print(Characters['credits'])
        print("""\n    Data Breaches Cost 40 percent Less for Companies with AI-Enabled Cybersecurity
    Retail Touchpoints
    link: https://www.retailtouchpoints.com/wp-content/uploads/2024/02/IG_Techopedia_2.19.24.png
    ---------------------------------------------------------------------
    AI Is Dangerous, but Not for the Reasons You Think 
    Sasha Luccioni 
    link: https://youtu.be/eXdVDhOGqoE?si=OWWsvMtofpK42L01
    ---------------------------------------------------------------------
   Wach, K., Duong, C. D., Ejdys, J., Kazlauskaitė, R., Korzynski, P., Mazurek, G., ... & Ziemba, E. (2023). 
   The dark side of generative artificial intelligence: A critical analysis of controversies and risks of ChatGPT. 
   Entrepreneurial Business and Economics Review, 11(2), 7-30.
   file:///home/deck/Downloads/msieja,+EBER-11-02-01-pp007--2113-Wach,Duong,Ejdys,Kazlauskaite,Korzynski,Mazurek,Paliszkiewicz,Ziemba.pdf

    ---------------------------------------------------------------------""")
        exit = input("\n[TYPE 'exit' to LEAVE] ").lower()
        match exit:
            case "exit":
                Loop = True
                Credits = False
    while Info == True:
        main_info()

    while Loop == True:
        # Main Menu while loop #
        os.system('clear')
        print(Characters['logo'])
        print("\n(1)START"), '\n', print("(2)CREDITS"), '\n', print("(3)QUIT")

        menu = str(input("[]> "))

        match menu:
            case "1":
                Info = True
                Loop = False
            case "2":
                Credits = True
                Loop = False
            case "3":
                quit()