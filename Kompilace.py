import sys
from distutils.spawn import find_executable
import subprocess
from podpFce import colored

def NalezeniKompilatoru():
    clang_executable = find_executable('clang')
    gcc_executable = find_executable('gcc')
    gpp_executable = find_executable('g++')
    compiler = None

    if "-cpp" not in sys.argv:
        if gcc_executable == None and clang_executable == None:
            print(colored("Nenalezen kompilátor (Clang / Gcc)", "red"))
            sys.exit()
        elif (gcc_executable != None) and "-forceclang" not in sys.argv:
            print("Kompilátor: gcc")
            compiler = "Gcc"
        elif (clang_executable == None) and "-forceclang" in sys.argv:
            colored("Kompilátor clang nenalezen. používá se gcc", "red")
            compiler = "Gcc"
        else:
            print("Kompilátor: Clang")
            compiler = "Clang"

        if "-final" in sys.argv and compiler != "Clang":
            with open("main.c", "r") as file:
                if file.read()[-1] != "\n":
                    print(colored("Soubor main.c nekončí prázdným řádkem", "red"))
                    sys.exit()
    else:
        if gpp_executable == None:
            print(colored("Nenalezen kompilátor (Clang / Gcc)", "red"))
            sys.exit()
        else:
            print("Kompilátor: g++")
            compiler = "g++"

    return compiler

def ZkompilujVse(compiler):
    if "-cpp" not in sys.argv:
        FileEnd = "*.c"
    else:
        FileEnd = "*.cpp"
    cmd = [compiler, FileEnd, "-o", "main.exe"]

    if '-nocolor' not in sys.argv:
        if compiler == "Gcc":
            cmd.append("-fdiagnostics-color=always")
        if compiler == "g++":
            cmd.append("-fdiagnostics-color=always")
        if compiler == "Clang":
            cmd += ["-fcolor-diagnostics", "-fansi-escape-codes"]

    if "-final" in sys.argv:
        cmd += ["-pedantic", "-Wall", "-Werror", "-O2"]
        if "-cpp" not in sys.argv:
            cmd += ["-std=c99"]
        else:
            cmd += ["-std=c++17"]
    else:
        cmd += ["-g3"]

    proc = subprocess.Popen(cmd,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                            )

    stdout_value, stderr_value = proc.communicate()

    vystup = stderr_value.decode().replace("\r\n", "\n")
    print(vystup)
    if proc.returncode != 0:
        print(colored("ERROR KOMPILACE", "red"))
        sys.exit()
    else:
        if "warning:" in vystup:
            print(colored("OK-Varování", "yellow", "on_magenta"))
        else:
            print(colored("kompilace OK", "green"))

    print("\n")