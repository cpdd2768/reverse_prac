flag =''
f = [] 
s1 = ['']*27#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
s12 = ['']*27
key = [0, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, 13, 16, 19, 22, 25]
aaa = 'ioOavquaDb}x2ha4[~ifqZaujQ#'
for x in range(3):
    for i in range(len(aaa)):
        if (i + x) % 3 == 0:
            print(str(i),',',end='')

for i in range(len(aaa)):
    #s12.insert(key[i],aaa[i]) #为啥不一样捏
    s1[key[i]] = aaa[i]
    # if s12 == s1:
    #     print(yes)
    # else:
    #     print('n0!')

print(s1)

for i in range(len(s1)):
    if i % 2 == 0:
        f.append(chr(ord(s1[i]) - 1))
    else:
        f.append(chr(ord(s1[i]) - 2))
flag = flag.join(f)  #列表，字符串相互转换
print(flag)

