#!/usr/bin/env python3

# 高阶函数
# map函数接受两个参数：一个函数，一个可迭代
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

l = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # 将列表中的元素转换为字符串
print(l)

# reduce函数接受三个参数：一个函数，一个可迭代对象，初始值（可选）
# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce

def add(x, y):
    return x + y

r = reduce(add, [1, 3, 5, 7, 9]) # 1+3+5+7+9=25
print(r)

# str --> int
from functools import reduce
def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

r = reduce(fn, map(char2num, '13579'))
print(r)

# 上面代码中，map函数把字符串'13579'转换成一个整数序列1, 3, 5, 7, 9，reduce函数把这个序列转换成一个整数13579。  
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('13579'))
# 上面的代码定义了一个str2int函数，可以把字符串'13579'转换成整数13579。



# filter函数接受两个参数：一个函数，一个可迭代对象
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

# 用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

# sorted函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序:
print(sorted([36, 5, -12, 9, -21]))
# key=abs表示根据元素的绝对值进行排序，如果元素的绝对值相同，则按照原来的顺序排列。
print(sorted([36, 5, -12, 9, -21], key=abs))

# key=len表示根据元素的长度进行排序。
words = ['banana', 'cat', 'apple', 'dog']
print(sorted(words, key=len))

# key= str.lower表示根据元素的小写字母进行排序，这样就可以忽略大小写的差异。
words = ['bob', 'About', 'Zoo', 'apple']
print(sorted(words, key=str.lower))

# key=lambda x: x[1]表示根据元组的第二个元素进行排序。如果元组的第二个元素相同，则按照原来的顺序排列。
students = [
    ('Tom', 80),
    ('Jack', 95),
    ('Bob', 70)
]

print(sorted(students, key=lambda x: x[1]))

# key=lambda x: x[0]表示根据元组的第一个元素进行排序。如果元组的第一个元素相同，则按照原来的顺序排列。

students = [
    ('Tom', 80),
    ('Jack', 95),
    ('Bob', 70)
]

print(sorted(students, key=lambda x: x[0]))

# key=lambda x: x['score']表示根据字典的'score'键进行排序。如果字典的'score'键相同，则按照原来的顺序排列。
students = [
    {'name': 'Tom', 'score': 80},
    {'name': 'Jack', 'score': 95},
    {'name': 'Bob', 'score': 70}
]

print(sorted(students, key=lambda x: x['score']))

# reverse=True表示按照降序排列。如果元组的第一个元素相同，则按照原来的顺序排列。
nums = [36, 5, -12, 9, -21]
print(sorted(nums, key=abs, reverse=True))

from typing import Callable

# 返回函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args: int) -> Callable:
    def sums() -> int:
        ax = 0
        for n in args:
            ax += n
        return ax
    return sums

f: Callable[[], int] = lazy_sum(1, 3, 5, 7, 9)
print(f())

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

# nonlocal
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # 1
print(f()) # 1

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2


# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))) # lambda x: x * x 是一个匿名函数，表示输入参数x，返回x * x的值。匿名函数可以用在需要函数对象的地方，比如map()函数的第一个参数。匿名函数的语法是：lambda 参数: 表达式。匿名函数可以有任意多个参数，但只能有一个表达式，表达式的结果就是函数的返回值。匿名函数不能直接调用，但可以赋值给一个变量，然后通过变量来调用匿名函数。

# 装饰器
from typing import Callable

f: Callable[[], None]


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now() -> None:
    print('2015-3-25')
    
now()

# 偏函数
int('12345') # 12345
int('12345', base=8) # 5349
int('12345', base=16) # 74565


def int2(x, base=2):
    return int(x, base)
int2('1000000') # 64
int2('101010101') # 341

import functools
intt2 = functools.partial(int, base=2)
intt2('1000000') # 64
intt2('101010101') # 341

