arr = [0x000000A0, 0x000000E6, 0x0000007A, 0x0000011E, 0x000000E6, 0x00000090, 0x00000122, 0x000000D0, 0x000000F0, 0x00000090, 0x0000012C, 0x000000D8, 0x00000122, 0x000000F4, 0x000000F0, 0x00000064, 0x00000100, 0x00000136]

flag = ''
x = 1
for i in range(len(arr)):
    for x in range(32,127):

        v3 = (x >> 7) >> 4
        v9 = (((v3 + (x >> 4)) & 0xF) - v3)
        v4 = ((16 * x) >> 31) >>28
        v8 =((v4 + ((16 * x) >> 4)) & 0xF) - v4
        v7 = 22 * v9 + 12 * v8
    
        while v7 == arr[i]:
            flag += chr(x)
            break
        

print(flag)
    

