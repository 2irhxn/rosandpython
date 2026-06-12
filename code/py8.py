#!/usr/bin/env python3

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])  # 从索引0开始取，直到索引3为止，但不包括索引3
print(L[:3])   # 等价于L[0:3]
print(L[-2:])  # 从倒数第二个元素开始取，直到最后一个元素
print(L[:-2])  # 等价于L[-2]
L = list(range(100))
print(L[:10])  # 从索引0开始取，直到索引10为止，但不包括索引10
print(L[::2])  # 从索引0开始，每次跳过一个元素取一次
print((0, 1, 2, 3, 4, 5)[:3]) # tuple也可以切片，结果仍是tuple
print('ABCDEFG'[:3]) # 字符串也可以切片，结果仍是字符串

# 迭代
for i in L:
    print(i)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表推导式
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

L = [x * x for x in range(1, 11)] # 等价于上面的循环，但更简洁
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0] # 只取偶数平方
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ'] # 多重列表推导式，生成所有可能的组合
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,"=",v)
L = [k + '=' + v for k, v in d.items()] # 生成一个包含键值对的列表
print(L)

# 
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for i in g:
    print(i)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)

# 迭代器
from collections.abc import Iterator
isinstance((x for x in range(10)), Iterator) # 判断是否是迭代器
isinstance([], Iterator) # 判断是否是迭代器
isinstance({}, Iterator) # 判断是否是迭代器
isinstance('abc', Iterator) # 判断是否是迭代器
