# microChecker
A simple program for checking C programs.

# features
  - compile main.c file with gcc 
  - pass every .in file to STDIN
  - check STDOUT against .out file
  - check STDERR against .err file
  - check return value
  - check for program timeout

# dependecies
 - **gcc**
 - **python** 3.6.4+
    * module: **termcolor**

# install process
1) install and set up gcc
2) install and set up Python (make sure path is set up)
3) install termcolor module to Python
4) download .in .out .err files and save to folder "data"
5) (optional) in folder "data" create file "config.conf" and on separate lines add return values of individual test in order pub01 -> pub02 -> pub03 -> ...
    example:
    ```
    0
	0
	100
    ```
    if you need to supply command line arguments to tested program. Add them to the file like this:
    ```
    0 arg1
    0
    100 arg1 arg2
    ```
6) add your own "main.c" or edit premade file
7) start program in color capable console. With
    ```
    python.exe .\microCheck.py
    ```
    (Program is being developed in Windows PowerShell in [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701))
8) You should see gcc errors or program output showing differences between .in .out .err files. Or an OK message. You can fix your main.c file and rerun check.
9) After you pass step 8. You can rerun the check with -Final flag.
    ```
    python.exe .\microCheck.py -Final
    ```
    this step will recompile your code with flags "-pedantic -Wall -Werror -std=c99 -O2"
10) after passing step 10 your program is working as expected based on files in folder data