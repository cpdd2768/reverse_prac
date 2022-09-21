from msvcrt import kbhit
from re import A


s = '5B134977135E7D13'
f = ''
a = 0
k = [0x10,0x20,0x30]
for i in range(0,len(s),2):
    f += chr(int(s[i:i+2],16)^k[a])
    a += 1
    i += 1
    if a >= 3:
        a = 0
print(f) 