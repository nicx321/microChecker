import subprocess
from threading import Timer
import os
import sys
import pip
from podpFce import colored, BasicSetup
from Kompilace import NalezeniKompilatoru, ZkompilujVse

#ARGUMENTY
vysledek = []
optVysledek = None
Exports = []

Fail = 0

BasicSetup()
compiler = NalezeniKompilatoru()
ZkompilujVse(compiler)

#config soubor
if not os.path.isfile("./data/config.conf"):
    print(colored("\"data/config.conf\" nenalezen", "yellow"))
else:
    readData = open("./data/config.conf", "r")
    conf = readData.readlines()
    readData.close()
    optVysledek = []
    for line in conf: 
        optVysledek.append(line.replace("\n", "").split(" "))

#KONTROLA
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

    my_timer = Timer(10, kill, [proc])
    try:
        my_timer.start()
        stdout_value, stderr_value = proc.communicate(data.encode())
    finally:
        my_timer.cancel()

    ret = proc.returncode
    if TIMEOUT:
        return["T", ["", ""], ["", ""]]

    try:
        outData = stdout_value.decode().replace("\r\n", "\n")
    except UnicodeDecodeError:
        print(stdout_value)

    try:
        ErrorData = stderr_value.decode().replace("\r\n", "\n")
    except UnicodeDecodeError:
        print(ErrorData)

    if "-exportall" in sys.argv:
        if not os.path.exists('Exports'):
            os.mkdir('Exports')
        global Exports
        WriteData = open("./Exports/"+name+".out", "w")
        WriteData.write(outData)
        WriteData.close()
        Exports.append("./Exports/"+name+".out")
        WriteData = open("./Exports/"+name+".err", "w")
        WriteData.write(ErrorData)
        WriteData.close()
        Exports.append("./Exports/"+name+".err")

    if not os.path.isfile("./data/"+name+".out"):
        print("nenalezen soubor \"" + name + ".out\"")
        sys.exit()

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
        if "-export" in sys.argv:
            if not os.path.exists('Exports'):
                os.mkdir('Exports')
            global Exports
            if Datatype == "stdout":
                End = ".out"
            else:
                End = ".err"
            WriteData = open("./Exports/"+name+End, "w")
            WriteData.write(A)
            WriteData.close()
            Exports.append("./Exports/"+name+End)
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
                    if(A[j-1] == "\n"):
                        print(colored("n", "cyan"), end = "")
                    elif(A[j-1] == "\a"):
                        print(colored("a", "cyan"), end = "")
                    elif(A[j-1] == "\t"):
                        print(colored("t", "cyan"), end = "")
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

        if "-hex" in sys.argv:
            width = 8
            print("\n")
            A_Hex = []
            B_Hex = []
            for i in range(Clen):
                A_Hex.append("..")
                B_Hex.append("..")
            for i, char in enumerate(A):
                A_Hex[i] = hex(ord(char))[2:]
            while (len(A_Hex))%width != 0:
                A_Hex.append("  ")
            for i, char in enumerate(B):
                B_Hex[i] = hex(ord(char))[2:]
            while (len(B_Hex))%width != 0:
                B_Hex.append("  ")
            
            FoundA = False
            FoundB = False
            print("0000: ", end="")
            for i in range(max(len(A_Hex), len(B_Hex))):
                if A_Hex[i] != B_Hex[i] and FoundA == False:
                    print(colored(A_Hex[i], "red"), end=" ")
                    FoundA = True
                else:
                    print(A_Hex[i], end=" ")
                if (i+1)%width==0:
                    if FoundA and not FoundB:
                        print("    !", end="     ")
                    else:
                        print("     ", end="     ")
                    for y in range(i-width+1, i+1):
                        if A_Hex[y] != B_Hex[y] and FoundB == False:
                            print(colored(B_Hex[y], "green"), end=" ")
                            FoundB = True
                        else:
                            if B_Hex[y] == ".." and A_Hex[y] != " ":
                                print(colored(B_Hex[y], "yellow"), end=" ")
                            else:
                                print(B_Hex[y], end=" ")
                        
                    print("\n", end="")
                    if i+1 != max(len(A_Hex), len(B_Hex)):
                        print('%04d' % (i+1)+": ", end="")
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
                    print(colored(str(vysledek[i][0])+"("+str(optVysledek[i][0])+")", 'red'), end="\t|")
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
    sys.exit()

for i, name in enumerate(names):
    if optVysledek == None:
        args = ""
    else:
        args = ""
        for arg in optVysledek[i][1:]:
            args += arg+" "
    vysledek.append(run(name, args))

ErrHighLight(vysledek)

if Exports != []:
    print("Exported:")
    for Export in Exports:
        print("\t"+Export)
    print("\n")

prettyTable(vysledek)

if Fail == 0:
    print(colored("""
       _    
      | |   
  ___ | | __
 / _ \\| |/ /
| (_) |   < 
 \\___/|_|\\_\\""", "green"))

if Fail >= 4:
    print(colored("\n\t(╯°□°）╯︵ ┻━┻", "red"))

if "-keep" not in sys.argv:
    os.remove("main.exe")