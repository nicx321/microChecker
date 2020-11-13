# microChecker
Jednoduchý program pro testování programů v C

## Vlastnosti
  - kompilace C programů s gcc (nebo Clang)
  - odeslání dat ze soubor .in do STDIN
  - kontrola STDOUT vůči .out
  - kontrola STDERR vůči .err
  - kontrola návratových hodnot
  - kontrola proti nekonečným smyčkám

## Závislosti
 - Kompilátor **gcc** nebo **Clang** (Výchozí: gcc, Clang se spustí pokud není nalezeno gcc)

## Příprava projektu
1) nainstalujte gcc (nebo Clang)
2) vytvořte hlavní složku projektu a vložte do ní soubory microChecker
3) stáhněte soubory .in .out .err a vložte je do složky "data"
4) (volitelné) můžete přidat návratové hodnoty, a případné argumenty testovanému programu, pro porovnání. Toto nastavení provedete příkazem:
    ```
    .\microCheck.exe -config
    ```
5) do hlavní složky přidejte váš "main.c", nebo upravte předvytvořený soubor.
6) zapněte program v kompatibilní konzoli příkazem:
    ```
    .\microCheck.exe
    ```
    (program je vytvářen v: [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701))
    (pokud vidíte v konzoli "divné znaky", zkuste program zapnout s dodatkem -nocolor)
7) měli by jste vidět výstup kompilátoru, rozdíly ve výstupu vašeho programu vůči .out a .err, nebo zprávu OK.
8) poté co vám funguje program. Můžete ho znova spustit s argumentem "-Final".
    ```
    .\microCheck.exe -Final
    ```
    Váš program bude překompiláván s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
9) po tomto kroku váš program splňuje funkci dle souborů ve složce "data"

## Přídavné funkce
 - argument "-cls" před spuštěním programu vyčistí obrazovku
 - argument "-export" uloží chybné výstupy STDOUT a STDERR do složky Exports
 - argument "-exportall" uloží všechny výstupy STDOUT a STDERR do složky Exports
 - argument "-final" zkompuje program s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
 - argument "-nocolor" nebude používat barvy při výpise do konzole
 - argument "-hex" Kromě znakového výstupu vypíše i porovnání v šestnáctkové soustavě 
 - argument "-forceclang" využije kompilátor Clang i když je dostupné Gcc 
 - argument "-keep" Zanechá již zkompilovaný soubor main.exe

# Další informace
 - Zdrojové kódy programu naleznete ve složce `src`, hlavním programem je soubor `microCheck.py`, soubory `Kompilace.py` a `podpFce.py` obsahují přídavné funkce pro chod programu.
 - Převod programu do souboru .exe je prováděn knihovnou [pyinstaller](https://pypi.org/project/pyinstaller/) příkazem
     ```
    pyinstaller --onefile .\microCheck.py
     ```