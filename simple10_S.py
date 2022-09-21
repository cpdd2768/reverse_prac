import string
letters = list(string.ascii_letters) + list(string.digits) + ['+', '/']

output = ''
# print(letters)
# print(len(dec))
ec =  'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'
while ec:
    num = []
    c = []
    a = list(ec[:4])
    num = [ letters.index(i) for i in a ]
    b =[('{:0>6}').format((bin(i)).replace('0b', '')) for i in num]#在format里面就要把0b换了，不然first loop45：101101会多两位
    b = ''.join(b)#convert
    thr = [b[x:x+8] for x in [0,8,16]]#三组
    c = [(('{}').format(int(x,2))) for x in thr]
    print(c)
    ec = ec[4:]
    for i in c:
        output += chr(int(i))
    print(output)

lst = ['']*33
output = list(output)
print(output)
print(len(output))

for i in range(len(output)):
    if i % 2 == 0:
        lst[i] = chr(ord(output[i]) + 2)
    lst[i] = chr(ord(output[i]) - 1)
lst.reverse()
f = ''.join(lst)
print(f)











