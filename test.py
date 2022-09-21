# a = 'abcdefg'
# for x in [0,2,4,6]:
#     b = [a[x:x+2]] 
#     print(b)
# c = ['c','f','e']
# num = [ a.index(i) for i in c]
# print(num)
# import string
# ec =  'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'
# a = list(ec[:4])
# num = [ ec.index(i) for i in a ]
# print(len(ec))
# letters = list(string.ascii_letters) + list(string.digits) + ['+', '/']
# print(len(letters))
# input_str = 'asddfggfd'
# str_ascii_list = [ ('{:0>8}').format(str(bin(ord(i))).replace('0b', '')) for i in input_str ]
# print(str_ascii_list)