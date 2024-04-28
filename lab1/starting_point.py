#!/usr/bin/env python3

from pwn import *


# start process interaction
# use "process" from pwntools
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
