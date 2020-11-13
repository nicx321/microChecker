import sys
import os

istermcolor = True

def BasicSetup():
    global termcolor
    try:
        import termcolor  
    except ImportError:
        x = input("chybí balíček \"termcolor\" přejete si ho nainstalovat? (y/n): ")
        if(x in ['y', 'Y']):
            import pip
            pip.main(['install', "termcolor"])
            import termcolor
        else:
            istermcolor = False
    
    for i, arg in enumerate(sys.argv):
        sys.argv[i] = arg.lower()

    if "-cls" in sys.argv:
        os.system('cls' if os.name=='nt' else 'clear')

def colored(*args):
    if '-nocolor' in sys.argv or not istermcolor:
        return args[0]
    if(len(args)==2):
        return termcolor.colored(args[0], args[1])
    if(len(args)==3):
        return termcolor.colored(args[0], args[1], args[2])

def generateConfigFile():
    print("Zadejte návratovou hodnutu (celé číslo) jednotlivých testů,")
    print("K jednotlivým testům můžet zadat i argumenty, nebo zanechte prázdný řádek")
    names = []
    out = ""
    for file in os.listdir("./data/"):
        if file.endswith(".in"):
            names.append(file[:-3])
    for name in names:
        Ret = input("Návratová hodnota testu "+ name +": ")
        try:
            Ret = str(int(Ret))
        except:
            print("!!Návratová hodnota není číslo!!")
            return
        Args = input("argumenty testu "+ name +": ")
        out += Ret + " " + Args + "\n"
    file = open("./data/config.conf", "w")
    file.write(out)
    file.close()
    print("Config vytvořen a uložen")