#!/usr/bin/env python3

from pwn import *
from sys import argv


def merge_strings(arr):
    def backtrack(curr, remaining, results):
        if not remaining:
            results.append(curr)
            return
        for i in range(len(remaining)):
            new_curr = curr + remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(new_curr, new_remaining, results)
    
    results = []
    backtrack('', arr, results)
    return results

passparts = ["zihldazjcn", "vlrgmhasbw", "jqvanafylz", "hhqtjylumf", "yemlopqosj", "mdcdyamgec", "nhnewfhetk"]
allpass = merge_strings(passparts)

outarr = []
for i in range(len(allpass)):
# start process interaction
# use "process" from pwntools
    if len(argv) > 1:
        if argv[1] == "ltrace":
            p = process("ltrace  -o crackme_ltrace_bypass_checks.txt ./crackme.exe", shell=True)
        elif argv[1] == "strace":
            p = process("strace -o crackme_strace_bypass_checks.txt ./crackme.exe", shell=True)
        else:
            p = process("./crackme.exe")
    else: 
        p = process("./crackme.exe")


    p.sendline(allpass[i].encode("ascii"))
    out = ''
    while True:
        try:
            #use "readline" from pwntools
            out = p.recvline()
        except:
            #could not read line => program exited
            break
    print(i)
    print(allpass[i])
    print(out)
    outarr.append(out)
    p.close()


print(outarr)
# b'timctf{7dfadd1ee67a9c516c9efbf8f0cf43f4}\n'



# passw = "".join(passparts)
# print(passw)
# print(len(passw))

# # send input
# # use "send"/"sendline" from pwntools
# long = (passw + "".join(["a" for i in range(70-len(passw))])).encode("ascii")
# p.sendline(long)

# keep reading output until program terminates
# while True:
#     try:
#         #use "readline" from pwntools
#         print(p.recvline())
#     except:
#         #could not read line => program exited
#         break

# p.close()
