#!/usr/bin/env python3

#字符编码
print('包含中文的str')
ord('A') # ord()函数返回字符对应的ASCII码值
ord('a') # ord()函数返回字符对应的ASCII码值
ord('中') # ord()函数返回字符对应的ASCII码值
chr(66) # chr()函数将ASCII码转换为字符
chr(25991) # chr()函数将ASCII码转换为字符
'\u4e2d\u6587' # Unicode编码，表示中文字符

x = b'ABC' # bytes类型，表示字节串，前面加b表示这是一个bytes对象
y = 'ABC' # str类型，表示字符串，前面没有b表示这是一个str对象

print(type(x))  # <class 'bytes'>
print(type(y))  # <class 'str'>
print(x == y)   # False  类型不同，不相等

b'ABC'.decode('ascii') # 将bytes对象解码为str对象，使用ascii编码
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # 将bytes对象解码为str对象，使用utf-8编码
'ABC'.encode('ascii') # 将str对象编码为bytes对象，使用ascii编码

b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') # 将bytes对象解码为str对象，使用utf-8编码，并忽略错误的字节

len('ABC') # 3，字符串的长度是字符的个数
len('中文') # 2，字符串的长度是字符的个数。

len(b'ABC') # 3，字节串的长度是字节的个数
len(b'\xe4\xb8\xad\xe6\x96\x87') # 6，字节串的长度是字节的个数，每个中文字符占3个字节
len('中文'.encode('utf-8')) # 6，字符串编码为字节串后，每个中文字符占3个字节，总共占6个字节

len('中文'.encode('utf-8', errors='ignore')) # 2，字符串编码为字节串后，每个中文字符占3个字节，总共占6个字节，忽略错误的字

len('中文'.encode('gbk')) # 4，字符串编码为字节串后，每个中文字符占3个字节，总共占6个字节，GBK编码不支持中文字符

#格式化
print('Hello, %s' % 'world') # 使用 % 操作符进行字符串格式化

print('Hi, %s, you have $%d.' % ('Michael', 1000000)) # 使用 % 操作符进行字符串格式化，%s 表示字符串，%d 表示整数，%f 表示浮点数，%x 表示十六进制数，%o 表示八进制数，%% 表示百分号，%r 表示原始字符串

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125) # 使用 format 方法进行字符串格式化

# f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
# The area of a circle with radius 2.5 is 19.62
# f-string 是 Python 3.6 引入的，可以方便地在字符串中嵌入

