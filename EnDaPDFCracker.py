#Import all needed modules
import time
import PyPDF2
from Modules.Style import *

#Create banner var
banner = """
     ______       _____          _____  _____  ______    _____                _             
    |  ____|     |  __ \        |  __ \|  __ \|  ____|  / ____|              | |            
    | |__   _ __ | |  | | __ _  | |__) | |  | | |__    | |     _ __ __ _  ___| | _____ _ __ 
    |  __| | '_ \| |  | |/ _` | |  ___/| |  | |  __|   | |    | '__/ _` |/ __| |/ / _ \ '__|
    | |____| | | | |__| | (_| | | |    | |__| | |      | |____| | | (_| | (__|   <  __/ |   
    |______|_| |_|_____/ \__,_| |_|    |_____/|_|       \_____|_|  \__,_|\___|_|\_\___|_|   
"""
#Define a keyboard executing handler
def keyboard_handler():
    try:
        enter()
        exiting = input(Fore.RESET + f"    [{Fore.RED}?{Fore.RESET}]" + Fore.LIGHTRED_EX + " Do you want to do exit the program? (Y/N)" + Fore.RESET + " >> ")
        enter()
        if str(exiting).lower() in ("y","yes","yeah","stay","ja"):
            try:
                print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.WHITE + "]" + Fore.WHITE + " >> " + Fore.LIGHTBLUE_EX + "Roger that, exiting the EnDa PDF Cracker!" + Fore.RESET)
                time.sleep(2)
                exit()
            except:
                exit()
        elif str(exiting).lower() in ("n","no","exit","quit","nein"):
            pass
        else:
            print(Fore.WHITE + "    [" + Fore.RED + "!" + Fore.WHITE + ']' + Fore.RED + " ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "The inputed option does not exist!" + Fore.RESET)
            keyboard_handler()
    except KeyboardInterrupt:
        keyboard_handler()
    except EOFError:
        keyboard_handler()

#Define the child function which verifies the password
def verify_the_password(file:str,password:str):
    try:
        reader = PyPDF2.PdfReader(file)
        nr = reader.decrypt(password=password)
        if nr > 0:
            return True
        else:
            return False
    except:
        return False
    
clearConsole()
print(banner_color(banner,random.randint(1,5)))
enter(2)
if os.name in ("dos","nt"):
    os.system(f"title EnDa PDF Cracker ^| File : N/A ^| Password : N/A ^| Tries : 0/0 ^| EnDaTeam on GITHUB")
print(Fore.LIGHTRED_EX + "    [=============================" + Fore.WHITE + " Welcome to EnDa PDF Cracker " + Fore.LIGHTRED_EX + "=============================]")
print(Fore.LIGHTYELLOW_EX + "    [=======================" + Fore.WHITE + " Input the pdf file and see the password " + Fore.LIGHTYELLOW_EX + "=======================]")
enter()
while True:
    try:
        while True:
            path_of_pdf = input(Fore.WHITE + "    [" + Fore.MAGENTA + "+" + Fore.WHITE + "] " + Fore.LIGHTYELLOW_EX + "Input the path of PDF file" + Fore.WHITE + " >> " + Fore.RESET)
            enter()
            try:
                reader = PyPDF2.PdfReader(path_of_pdf)
            except:
                pass
            if not os.path.isfile(path_of_pdf):
                print(Fore.WHITE + "    [" + Fore.RED + "!" + Fore.WHITE + ']' + Fore.RED + " ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "The inputed file does not exist!" + Fore.RESET)
                enter()
            elif not reader.is_encrypted:
                print(Fore.WHITE + "    [" + Fore.RED + "!" + Fore.WHITE + ']' + Fore.RED + " ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "The inputed file is not protected with a password!" + Fore.RESET)
                enter()
            else:
                break
        while True:
            path_of_wordlist = input(Fore.WHITE + "    [" + Fore.MAGENTA + "+" + Fore.WHITE + "] " + Fore.LIGHTYELLOW_EX + "Input the path of wordlist file" + Fore.WHITE + " >> " + Fore.RESET)
            enter()
            if path_of_wordlist.lower() in (""," "):
                path_of_wordlist = "DefaultWordlist.txt"
            if not os.path.isfile(path_of_wordlist):
                print(Fore.WHITE + "    [" + Fore.RED + "!" + Fore.WHITE + ']' + Fore.RED + " ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "The inputed file does not exist!" + Fore.RESET)
                enter()
            else:
                break
        ok = False
        tries = 0
        with open(path_of_wordlist, 'r') as file:
            maxim = len(file.readlines())
        try:
            with open(path_of_wordlist, 'r') as file:
                for line in file:
                    tries = tries + 1
                    password = line.strip()
                    print(f"    {Fore.WHITE}[{Fore.YELLOW}!{Fore.RESET}] [{Fore.LIGHTCYAN_EX}{tries}{Fore.WHITE}/{Fore.LIGHTGREEN_EX}{maxim}{Fore.WHITE}] >> Trying {password}                                                                    ",end="\r")
                    if verify_the_password(path_of_pdf,password):
                        print(Fore.WHITE + '    [' + Fore.GREEN + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " Password Found" + Fore.WHITE + ' >> ' + Fore.LIGHTCYAN_EX + "Password" + Fore.WHITE + " : " + Fore.LIGHTGREEN_EX + password + f" ({tries}/{maxim})" + Fore.RESET)
                        ok = password
                    if os.name in ("dos","nt"):
                        os.system(f"title EnDa PDF Cracker ^| File : {path_of_pdf} ^| Password : {ok} ^| Tries : {tries}/{maxim} ^| EnDaTeam on GITHUB")
                    if ok:
                        break
        except KeyboardInterrupt:
            enter()
            keyboard_handler()
        if not ok:
            print(Fore.WHITE + '    [' + Fore.RED + "-" + Fore.WHITE + "] >>" + Fore.LIGHTRED_EX + " Password could be found!" + Fore.RESET)
        enter()
        another_scan = input(Fore.RESET + f"    [{Fore.BLUE}?{Fore.RESET}]" + Fore.CYAN + " Do you want to do another scan? (Y/N)" + Fore.RESET + " >> ")
        if str(another_scan).lower() in ("n","no","exit","quit"):
            try:
                enter()
                print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.BLUE + "]" + Fore.WHITE + " >> " + Fore.LIGHTBLUE_EX + "Roger that, exiting the EnDa PDF Cracker!" + Fore.RESET)
                time.sleep(2)
                exit()
            except:
                exit()
        enter()
    except KeyboardInterrupt:
        enter()
        keyboard_handler()