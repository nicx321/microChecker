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

## Instalace
 1) nainstalujte gcc (nebo Clang)
 2) stáhněte instalační soubor (microCheck-9.0-win32.msi) z tohoto repositáře
 3) spusťte instalační soubor a nainstalujete microChecker
 - Program je automaticky přidáván do systémové proměnné PATH

## Příprava projektu
1) otevře složku vašeho projektu (s vaším .c souborem) a vytvořte složku "data":
![projekt](/src/Obrazky/projekt.png)
2) stáhněte soubory .in .out .err a vložte je do složky "data"
3) (volitelné) můžete přidat návratové hodnoty a případné argumenty testovanému programu pro kontrolu. Toto nastavení provedete příkazem:
    ```
    microCheck.exe -config
    ```
4) v adresáři vašeho projektu zapněte program v kompatibilní konzoli příkazem:
    ```
    microCheck.exe
    ```
    (program je vytvářen v: [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701))
    (pokud vidíte v konzoli "divné znaky", zkuste program zapnout s dodatkem -nocolor)
5) měli by jste vidět výstup kompilátoru, rozdíly ve výstupu vašeho programu vůči .out a .err, nebo zprávu OK.
6) poté co vám funguje program. Můžete ho znova spustit s argumentem "-Final".
    ```
    microCheck.exe -Final
    ```
    Váš program bude překompiláván s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
7) po tomto kroku váš program splňuje funkci dle souborů ve složce "data"

## Přídavné funkce
 - argument "-cls" před spuštěním programu vyčistí obrazovku
 - argument "-readable" zobrazí zvýraznění chyb v čitelném formátu
 - argument "-export" uloží chybné výstupy STDOUT a STDERR do složky Exports
 - argument "-exportall" uloží všechny výstupy STDOUT a STDERR do složky Exports
 - argument "-final" zkompuje program s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
 - argument "-nocolor" nebude používat barvy při výpise do konzole
 - argument "-hex" Kromě znakového výstupu vypíše i porovnání v šestnáctkové soustavě 
 - argument "-forceclang" využije kompilátor Clang i když je dostupné Gcc 
 - argument "-keep" Zanechá již zkompilovaný soubor main.exe

# Další informace
 - Zdrojové kódy programu naleznete ve složce `src`, hlavním programem je soubor `microCheck.py`, soubory `Kompilace.py` a `podpFce.py` obsahují přídavné funkce pro chod programu. soubor `build.py` je použit pro vytváření instalačního souboru pomocí cx_Freeze
 - Převod programu do souboru .msi je prováděn knihovnou [cx_Freeze](https://pypi.org/project/cx-Freeze/) příkazem
     ```
    python build.py bdist_msi
     ```