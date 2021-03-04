# microChecker
Jednoduchý program pro testování programů v C/C++

## Vlastnosti
- kompilace C/C++ programů s gcc (nebo Clang) / g++
- odeslání dat ze soubor .in do STDIN
- kontrola STDOUT vůči .out
- kontrola STDERR vůči .err
- kontrola návratových hodnot
- kontrola proti nekonečným smyčkám

## Závislosti
- Kompilátor **gcc** nebo **Clang** (Výchozí: gcc, Clang se spustí pokud není nalezeno gcc)
- Případně kompilátor **g++**

## Instalace
1) nainstalujte gcc (nebo Clang) / g++
2) nainstalujte Python a moduly cx_Freeze a termcolor
```
pip install --upgrade cx_Freeze
pip install termcolor
```
3) stáhněte tento repozitář
4) v tomto repozitáři spusťe kompilaci přes
```
python build.py bdist_msi
```
5) spusťte instalační soubor ve složce dist/ a nainstalujete microChecker
- Program je automaticky přidáván do systémové proměnné PATH

## Příprava projektu
1) otevře složku vašeho projektu (s vaším .c/.cpp souborem) a vytvořte složku "data":

![projekt](/Obrazky/projekt.png)

2) stáhněte soubory .in .out .err a vložte je do složky "data"
3) (volitelné) můžete přidat návratové hodnoty a případné argumenty testovanému programu pro kontrolu. Toto nastavení provedete příkazem:
```
microCheck.exe -config
```
4) v adresáři vašeho projektu zapněte program v kompatibilní konzoli příkazem:
```
microCheck.exe
```
nebo pro použit s C++ přidejte argument *-cpp*
```
microCheck.exe -cpp
```
(program je vytvářen v: [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) a PowerShellu)
(pokud vidíte v konzoli "divné znaky", zkuste program zapnout s dodatkem -nocolor)
5) měli by jste vidět výstup kompilátoru, rozdíly ve výstupu vašeho programu vůči .out a .err, nebo zprávu OK.
6) poté co vám funguje program. Můžete ho znova spustit s argumentem "-Final".
```
microCheck.exe -Final
```
Váš program bude překompiláván s argumenty: "-pedantic -Wall -Werror -std=c99 -O2" nebo "-pedantic -Wall -Werror -std=c++17 -O2" při použití -cpp
7) po tomto kroku váš program splňuje funkci dle souborů ve složce "data"

## Přídavné funkce
- argument `-cpp` přepnutí z režimu C do režimu C++
- argument `-cls` před spuštěním programu vyčistí obrazovku
- argument `-readable` zobrazí zvýraznění chyb v čitelném formátu
- argument `-export` uloží chybné výstupy STDOUT a STDERR do složky Exports
- argument `-exportall` uloží všechny výstupy STDOUT a STDERR do složky Exports
- argument `-final` zkompuje program s argumenty: "-pedantic -Wall -Werror -std=c99 -O2"
- argument `-nocolor` nebude používat barvy při výpise do konzole
- argument `-hex` Kromě znakového výstupu vypíše i porovnání v šestnáctkové soustavě
- argument `-forceclang` využije kompilátor Clang i když je dostupné Gcc
- argument `-keep` Zanechá již zkompilovaný soubor main.exe

# Další informace
- Hlavním programem je soubor `microCheck.py`, soubory `Kompilace.py` a `podpFce.py` obsahují přídavné funkce pro chod programu. soubor `build.py` je použit pro vytváření instalačního souboru pomocí cx_Freeze
- Převod programu do souboru .msi je prováděn knihovnou [cx_Freeze](https://pypi.org/project/cx-Freeze/) příkazem
