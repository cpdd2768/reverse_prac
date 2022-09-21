import base64
correct = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
f = ''
c = base64.b64decode(correct)
for i in c:
    f += chr((i - 16) ^ 32)
#用‘b’指的是“b”这个字符，所以输出才只有一个字符
#c编译出来了之后，就是int，（why？），所以ord（）配不起
print(f)


