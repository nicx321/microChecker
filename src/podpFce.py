import sys
import os

istermcolor = True

def BasicSetup():
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
