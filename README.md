# microChecker
Jednoduchý program pro testování programů v C

## Vlastnosti
  - kompilace C programů s gcc 
  - odeslání dat ze soubor .in do STDIN
  - kontrola STDOUT vůči .out
  - kontrola STDERR vůči .err
  - kontrola návratových hodnot
  - kontrola proti nekonečným smyčkám

## Závyslosti
 - **gcc**
 - **python** 3.6.4+
    * modul: **termcolor** (instalace při prvním zapnutí)

## Příprava projektu
1) nainstalujte gcc
2) nainstalujte Python
3) vytvořte hlavní složku projektu a vložte do ní soubory microChecker
4) stáhněte soubory .in .out .err a vložte je do složky "data"
5) (volitelné) ve složce "data" vytvořte soubor "config.conf" a na samostatné řádky vložte návratové hodnoty testů v pořadí pub01 -> pub02 -> pub03 -> ...
    například:
    ```
    0
	0
	100
    ```
    Pokud potřebujete programu předávat argumenty. Přidejte je do souboru takto::
    ```
    0 arg1
    0
    100 arg1 arg2
    ```
6) do hlavní složky přidejte váš "main.c", nebo upravte předvytvořený soubor.
7) zapněte program v kompatibilní konzoli příkazem:
    ```
    python.exe .\microCheck.py
    ```
    (program je vytvářen v: [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701))
8) měli by jste vidět chybové hlášky gcc, nebo rozdíly ve výstupu vašeho programu vůči .out a .err, nebo zprávu OK.
9) poté co vám funguje program. Můžete ho znova spustit s argumentem "-Final".
    ```
    python.exe .\microCheck.py -Final
    ```
    Váš program bude překompiláván s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
10) po tomto kroku váš program splňuje funkci dle souborů ve složce "data"

## Přídavné funkce
 - argument "-cls" před spuštěním programu vyčistí obrazovku
 - argument "-export" uloží chybné výstupy STDOUT a STDERR do složky Exports
 - argument "-exportall" uloží všechny výstupy STDOUT a STDERR do složky Exports
 - argument "-final" zkompuje program s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
 - argument "-nocolor" nebude používat barvy při výpise do konzole
 - argument "-hex" Kromě znakového výstupu vypíše i porovnání v šestnáctkové soustavě 