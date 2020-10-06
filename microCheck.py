import subprocess
import os
from termcolor import colored
import subprocess
from threading import Timer

vysledek = []
optVysledek = None

Fail = 0

if not os.path.isfile("main.c"):
    print(colored("nenalezen soubor \"main.c\"", "red"))
    exit()

proc = subprocess.Popen(["gcc", "main.c", "-o", "main.exe", "-fdiagnostics-color=always"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )

stdout_value, stderr_value = proc.communicate()

vystup = stderr_value.decode().replace("\r\n", "\n")
print(vystup)
if proc.returncode != 0:
    print(colored("ERROR KOMPILACE", "red"))
    exit()
else:
    if "warning:" in vystup:
        print(colored("OK-Varování", "yellow", "on_magenta"))
        Fail += 1
    else:
        print(colored("kompilace OK", "green"))

print("\n\n")

if not os.path.isfile("./data/config.conf"):
    print(colored("\"data/config.conf\" nenalezen", "yellow"))
else:
    readData = open("./data/config.conf", "r")
    conf = readData.readlines()
    readData.close()
    optVysledek = []
    for line in conf: 
        optVysledek.append(line.replace("\n", "").split(" "))

def run(name, args):
    readData = open("./data/"+name+".in", "r")
    data = readData.read()
    readData.close()

    proc = subprocess.Popen("main.exe "+args,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
    global TIMEOUT
    TIMEOUT = False
    def kill(x):
        global TIMEOUT, Fail
        x.kill()
        TIMEOUT = True
        Fail += 1

    my_timer = Timer(5, kill, [proc])
    try:
        my_timer.start()
        stdout_value, stderr_value = proc.communicate(data.encode())
    finally:
        my_timer.cancel()

    ret = proc.returncode
    if TIMEOUT:
        return["T", ["", ""], ["", ""]]

    outData = stdout_value.decode().replace("\r\n", "\n")
    ErrorData = stderr_value.decode().replace("\r\n", "\n")

    if not os.path.isfile("./data/"+name+".out"):
        print("nenalezen soubor \"" + name + ".out\"")
        exit()

    readData = open("./data/"+name+".out", "r")
    AgainstData = readData.read()
    readData.close()

    ERR = ""
    if os.path.isfile("./data/"+name+".err"):
        readData = open("./data/"+name+".err", "r")
        ERR = readData.read()
        readData.close()

    return [ret, [outData, AgainstData], [ErrorData, ERR]]

def cmpPrint(A, B, name, Datatype):
    global Fail
    if A != B:
        Fail += 1
        print(colored(name.upper()+ " > " + Datatype, "red"))
        print(" "*12, end="")
        print("výstup", end="")
        print(" "*34, end="")
        print(name)

        Alen = len(A)
        Blen = len(B)
        Clen = max(Alen, Blen)

        if Clen == 0:
            print("\n\n")
            return

        if Blen == 0:
            print(" "*30, end="\t\t")

        row = 0
        rem = 0
        foundA = False
        foundB = False
        for j in range(1, Clen+1):
            if j-1 < Alen:
                if j-1 >= Blen:
                    if(A[j-1] == "\n"):
                        print(colored("n", "cyan"), end = "")
                    elif(A[j-1] == "\a"):
                        print(colored("a", "cyan"), end = "")
                    elif(A[j-1] == "\t"):
                        print(colored("t", "cyan"), end = "")
                    else:
                        print(colored(A[j-1], "yellow"), end="")
                elif A[j-1] != B[j-1] and not foundA:
                    if(A[j-1] == "\n"):
                        print(colored("n", "cyan", "on_red"), end = "")
                    elif(A[j-1] == "\a"):
                        print(colored("a", "cyan", "on_red"), end = "")
                    elif(A[j-1] == "\t"):
                        print(colored("t", "cyan", "on_red"), end = "")
                    else:
                        print(colored(A[j-1], "white", "on_red"), end="")
                    foundA = True
                else:
                    print(A[j-1], end="")
            else:
                print(colored(" ", "white", 'on_yellow'), end="")
            if (j % 30) == 0:
                print("\t\t", end="")
                for k in range(row*30, (row+1)*30):
                    if k < Blen:
                        if B[k] == "\n":
                            print(colored("n", "cyan"), end = "")
                        elif B[k] == "\a":
                            print(colored("a", "cyan"), end = "")
                        elif B[k] == "\t":
                            print(colored("t", "cyan"), end = "")
                        else:
                            if k < Alen:
                                if A[k] != B[k] and not foundB:
                                    print(colored(B[k], "white", "on_green"), end="")
                                    foundB = True
                                else:
                                    print(B[k], end="")
                            else:
                                if  not foundB:
                                    print(colored(B[k], "white", "on_green"), end="")
                                    foundB = True
                                else:
                                    print(B[k], end="")
                                
                print("")
                row += 1
            rem = j%30

        for l in range(30-rem):
            print(" ", end="")
        print("\t\t", end="")
        for k in range(row*30, (row+1)*30):
            if k < Blen:
                if B[k] == "\n":
                    print(colored("n", "cyan"), end = "")
                elif B[k] == "\a":
                    print(colored("a", "cyan"), end = "")
                elif B[k] == "\t":
                    print(colored("t", "cyan"), end = "")
                else:
                    if k < Alen:
                        if A[k] != B[k] and not foundB:
                            print(colored(B[k], "white", "on_green"), end="")
                            foundB = True
                        else:
                            print(B[k], end="")
                    else:
                        print(B[k], end="")
        print("\n\n")

def ErrHighLight(vysledek):
    duals = []
    for i, name in enumerate(names):
        cmpPrint(vysledek[i][1][0], vysledek[i][1][1], name, "stdout")
        cmpPrint(vysledek[i][2][0], vysledek[i][2][1], name, "stderr")

def prettyTable(vysledek):
    global Fail
    print("Test\t|return\t|stdout\t|stderr\t|")
    print("---------------------------------")
    for i, name in enumerate(names):
        print(name, end="\t|")
        if vysledek[i][0] != "T":
            if optVysledek != None:
                if str(vysledek[i][0]) == str(optVysledek[i][0]):
                    print(vysledek[i][0], end="\t|")
                else:
                    print(colored(str(vysledek[i][0])+" ("+str(optVysledek[i][0])+")", 'red'), end="\t|")
                    Fail += 1
            else:
                if vysledek[i][0] == 0:
                    print(colored("0", 'yellow'), end="\t|")
                else:
                    print(colored(vysledek[i][0], 'magenta'), end="\t|")
            if(vysledek[i][1][1] == ""):
                print("  ---", end="\t|")
            else:
                if vysledek[i][1][0]!=vysledek[i][1][1]:
                    print(colored('FAIL', 'red'), end="\t|")
                else:
                    print("OK", end="\t|")
            if(vysledek[i][2][1] == ""):
                print("  ---", end="\t|")
            else:
                if vysledek[i][2][0]!=vysledek[i][2][1]:
                    print(colored('FAIL', 'red'), end="\t|")
                else:
                    print("OK", end="\t|")
            print("")
        else:
            print(colored("\t TIMEOUT\t", "red")+"|")

names = []
for file in os.listdir("./data/"):
    if file.endswith(".in"):
        names.append(file[:-3])

if names == []:
    print("nenalezeny soubory .in")
    exit()

for i, name in enumerate(names):
    if optVysledek == None:
        args = ""
    else:
        args = ""
        for arg in optVysledek[i][1:]:
            args += arg+" "
    vysledek.append(run(name, args))

ErrHighLight(vysledek)

prettyTable(vysledek)

if Fail == 0:
    print(colored("""
       _    
      | |   
  ___ | | __
 / _ \\| |/ /
| (_) |   < 
 \\___/|_|\\_\\""", "green"))

if Fail >= 2:
    print(colored("\n\t(╯°□°）╯︵ ┻━┻", "red"))