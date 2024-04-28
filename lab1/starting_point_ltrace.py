#!/usr/bin/env python3

from pwn import *
from sys import argv

# start process interaction
# use "process" from pwntools
if len(argv) > 1:
    if argv[1] == "ltrace":
        p = process("ltrace  -o crackme_ltrace.txt ./crackme.exe", shell=True)
    elif argv[1] == "strace":
        p = process("strace -o crackme_strace.txt ./crackme.exe", shell=True)
    else:
        p = process("./crackme.exe")
else: 
    p = process("./crackme.exe")


# send input
# use "send"/"sendline" from pwntools
p.sendline(b"hello")

# keep reading output until program terminates
while True:
    try:
        #use "readline" from pwntools
        print(p.recvline())
    except:
        #could not read line => program exited
        break

p.close()
