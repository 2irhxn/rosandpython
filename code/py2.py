#!/usr/bin/env python3

#数据类型

#整数
a = 10  # 十进制
b = 0b1010  # 二进制
c = 0o12  # 八进制  
d = 0x1A  # 十六进制
print(a, b, c, d)       

#浮点数
e = 3.14           
f = -1.5e-2  # 科学计数法
print(e, f)         

#字符串
g = 'Hello, World!'
h = "Python is great!"       
print(g, h)     
#转义字符
i = 'It\'s a nice day!'
j = "Hello, World!\nHow are you?"
k = "This is a tab:\tSee?"
l = "This is a backslash: \\"
print(i)      
print(j)       
print(k)      
print(l)    

#多行字符串
m = '''这是一个多行字符串，
可以包含换行符和特殊字符。'''      
print(m)    

#布尔值
n = True          
o = False        
print(n, o)     

#布尔运算
print("逻辑与:True and False", True and False)   # False
print("逻辑或:True or False", True or False)    # True
print("逻辑非:not True", not True)         # False

#空值
p = None
print(p)

#变量类型
#动态语言
a = 123 # a是整数   
print(a)
a = 'ABC' # a变为字符串   
print(a)

#静态语言
#int a = 123; // a是整数类型变量
#a = "ABC"; // 错误：不能把字符串赋给整型变量

#常量
PI = 3.14159 # 这是一个常量，通常用大写表示

#除法
print("10/3=", 10 / 3)      # 结果是浮点数  3.333333333
print("9/3=", 9 / 3)        # 结果也是浮点数 3.0
print("10//3=", 10 // 3)    # 地板除，得到整数 3
print("10%3=", 10 % 3)      # 取模，得到余数 1
