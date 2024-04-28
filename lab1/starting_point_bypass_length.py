#!/usr/bin/env python3

from pwn import *
from sys import argv

# start process interaction
# use "process" from pwntools
maxlen = 0
maxltrace = []
for x in range(10001):
    strlen = 0
    if len(argv) > 1:
        if argv[1] == "ltrace":
            p = process("ltrace ./crackme.exe", shell=True)
        elif argv[1] == "strace":
            p = process("strace ./crackme.exe", shell=True)
        else:
            p = process("./crackme.exe")
    else: 
        p = process("./crackme.exe")

    # send input
    # use "send"/"sendline" from pwntools
    long = "".join(["a" for i in range(x)]).encode("ascii")
    p.sendline(long)

    currltrace = []
    # keep reading output until program terminates
    while True:
        try:
            #use "readline" from pwntools
            out = p.recvline()
            strlen+=len(out)
            currltrace.append(out.decode("ascii"))

            # print(out)
        except:
            #could not read line => program exited
            break
    if strlen > maxlen:
        if maxlen > 0 and strlen - maxlen > 37:
            maxltrace = currltrace
            print(x)
            print("".join(maxltrace))
            break
        maxlen = strlen    

    p.close()
