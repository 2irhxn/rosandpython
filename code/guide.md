---
tags:
  - guide
  - python基础
---
> Python 基础索引：按 `pyN.py` / `pyN.ipynb` 对应主题整理语法点，便于快速定位示例代码。

# Python 基础索引

## py1: 输入输出

- `print('hello, world')`: 使用 `print()` 向终端输出固定字符串。
- `input('请输入你的名字：')`: 使用 `input()` 从终端读取用户输入，并把输入结果赋值给变量 `name`。
- `print(f'你好，{name}！')`: 使用 f-string 在字符串中嵌入变量，完成带变量内容的输出。

## py2: 数据类型、变量、常量、运算

- 整数 `int`: 包含十进制 `10`、二进制 `0b1010`、八进制 `0o12`、十六进制 `0x1A`。
- 浮点数 `float`: 包含普通小数 `3.14`、负数和科学计数法 `-1.5e-2`。
- 字符串 `str`: 包含单引号字符串、双引号字符串、多行字符串。
- 转义字符: `\'` 表示单引号，`\n` 表示换行，`\t` 表示制表符，`\\` 表示反斜杠。
- 布尔值 `bool`: `True`、`False`。
- 布尔运算: `and` 表示逻辑与，`or` 表示逻辑或，`not` 表示逻辑非。
- 空值 `None`: 用 `None` 表示没有具体值。
- 动态类型: 同一个变量 `a` 可以先指向整数 `123`，再指向字符串 `'ABC'`。
- 常量命名: `PI = 3.14159`，用大写变量名表达“常量”语义。
- 除法 `/`: 结果是浮点数，例如 `10 / 3`、`9 / 3`。
- 地板除 `//`: 只保留整数部分，例如 `10 // 3`。
- 取模 `%`: 获取余数，例如 `10 % 3`。

## py3: 字符编码、bytes、字符串格式化

- Unicode 字符串: `print('包含中文的str')` 展示 Python 字符串可以包含中文。
- `ord('A')`、`ord('a')`、`ord('中')`: 把字符转换成对应编码值。
- `chr(66)`、`chr(25991)`: 把编码值转换成字符。
- `'\u4e2d\u6587'`: 使用 Unicode 转义表示中文字符。
- `bytes`: `b'ABC'` 表示字节串。
- `str`: `'ABC'` 表示字符串。
- `type(x)`、`type(y)`: 查看对象类型，区分 `bytes` 和 `str`。
- `x == y`: `bytes` 和 `str` 内容看起来相同也不是同一种类型。
- `decode('ascii')`: 把 ASCII 编码的 `bytes` 解码为 `str`。
- `decode('utf-8')`: 把 UTF-8 编码的 `bytes` 解码为 `str`。
- `encode('ascii')`: 把 `str` 编码为 ASCII `bytes`。
- `decode(..., errors='ignore')`: 解码时忽略错误字节。
- `len('ABC')`、`len('中文')`: 统计字符串字符数量。
- `len(b'ABC')`、`len(b'\xe4\xb8\xad\xe6\x96\x87')`: 统计 `bytes` 字节数量。
- `'中文'.encode('utf-8')`: 中文字符串转 UTF-8 字节。
- `'中文'.encode('gbk')`: 中文字符串转 GBK 字节。
- `'Hello, %s' % 'world'`: 使用 `%s` 格式化字符串。
- `'Hi, %s, you have $%d.' % (...)`: 同时格式化字符串和整数。
- `'%2d-%02d' % (3, 1)`: 整数宽度和补零格式化。
- `'%.2f' % 3.1415926`: 浮点数保留两位小数。
- `'Hello, {0}, 成绩提升了 {1:.1f}%'.format(...)`: 使用 `format()` 格式化字符串。
- `f'The area of a circle with radius {r} is {s:.2f}'`: 使用 f-string 和格式说明保留两位小数。

## py4: list、tuple、索引、增删改查

- `list`: `classmate = ['Michael', 'Bob', 'Tracy']` 创建列表。
- 正向索引: `classmate[0]` 访问第一个元素。
- `len(classmate)`: 获取列表长度。
- 负向索引: `classmate[-1]` 访问最后一个元素。
- `append('Adam')`: 在列表末尾追加元素。
- `insert(1, 'Jack')`: 在指定位置插入元素。
- `pop()`: 删除列表最后一个元素。
- `pop(1)`: 删除指定索引位置的元素。
- `remove('Bob')`: 按值删除元素，多个相同值时删除第一个。
- `classmate[1] = 'Bob'`: 修改指定索引位置的元素。
- `clear()`: 清空整个列表。
- 混合类型列表: `L = ['Apple', 123, True]`，列表元素可以是不同类型。
- 嵌套列表: `s = ['python', 'java', ['asp', 'php'], 'scheme']`。
- `len(s[2])`: 获取嵌套列表的长度。
- `s[2][0]`: 访问嵌套列表中的元素。
- `tuple`: `classmates = ('Michael', 'Bob', 'Tracy')` 创建不可变序列。
- 单元素 `tuple`: `t = ('a',)`，只有一个元素时逗号不能省略。
- `tuple` 中的 `list`: `p = ('a', 'b', ['A', 'B'])`。
- `p[2][0] = 'X'`: `tuple` 的元素指向不变，但其中的 `list` 内容可以修改。

## py5: 条件判断、match-case、循环控制

- `if age >= 6`、`elif age >= 18`、`else`: 使用 `if-elif-else` 做多分支判断。
- `birth < 2000`: 用条件判断区分 00 前和 00 后。
- `score == 'A'`、`score == 'B'`、`score == 'C'`: 用多个 `elif` 判断成绩等级。
- `match score`: 使用 Python 3.10 的 `match-case` 做模式匹配。
- `case 'A'`、`case 'B'`、`case 'C'`: 匹配固定值。
- `case _`: 使用下划线匹配其他所有情况。
- `case x if x < 10`: 在 `case` 中绑定变量，并使用 `if` 守卫条件。
- `case 11 | 12 | ... | 18`: 使用 `|` 匹配多个可能值。
- `match args`: 对列表结构进行模式匹配。
- `case ['gcc']`: 匹配只包含 `gcc` 的命令参数。
- `case ['gcc', file1, *files]`: 匹配 `gcc` 加至少一个文件，并用 `*files` 收集剩余文件。
- `case ['clean']`: 匹配 `clean` 命令。
- `for name in names`: 遍历列表中的每个元素。
- `for x in [1, 2, ...]`: 遍历固定整数列表求和。
- `range(101)`: 生成从 `0` 到 `100` 的整数序列。
- `range(1, 101, 2)`: 生成指定起点、终点和步长的整数序列。
- `while n > 0`: 使用 `while` 按条件循环。
- `break`: 在循环中满足条件时提前结束循环。
- `continue`: 跳过当前这一轮，直接进入下一轮循环。

## py6: dict、set、集合运算

- `dict`: `d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}` 创建字典。
- `d['Michael']`: 通过 `key` 获取对应 `value`。
- `d['Adam'] = 67`: 新增键值对。
- `d['Jack'] = 90`、`d['Jack'] = 88`: 同一个 `key` 再次赋值会覆盖旧值。
- `d.pop('Bob')`: 删除指定 `key` 对应的键值对。
- `set([1, 2, 3])`: 通过列表创建集合。
- `s.add(4)`: 向集合添加元素。
- `s.remove(2)`: 删除集合元素，元素不存在时会报错。
- `s.discard(5)`: 删除集合元素，元素不存在时不报错。
- `{1, 1, 2, 2, 4, 3, 3}`: 集合会自动去除重复元素。
- `s & p`: 求两个集合的交集。
- `s | p`: 求两个集合的并集。
- `set` 中的混合类型: `p = {1, 2, 6, 'apple', 'banana', 'cherry'}`。

## py7: 函数定义、参数、返回值、递归

- `def S(r)`: 定义计算圆面积的函数。
- `return 3.14 * r ** 2`: 使用 `return` 返回表达式结果。
- `def my_abs(x)`: 自定义绝对值函数。
- `if x >= 0`、`else`: 在函数内部使用条件判断。
- `def nop(): pass`: 使用 `pass` 定义空函数或占位逻辑。
- `if age >= 18: pass`: 在条件分支中使用 `pass` 占位。
- `import math`: 导入标准库 `math` 模块。
- `def move(x, y, step, angle=0.0)`: 定义带默认参数的函数。
- `math.cos(angle)`、`math.sin(angle)`: 调用 `math` 模块函数。
- `return nx, ny`: 返回多个值，实际返回的是 `tuple`。
- `x, y = move(...)`: 对多个返回值进行解包赋值。
- `def add_end(L=None)`: 使用 `None` 作为默认参数。
- `if L is None`: 避免默认可变参数共享同一个 `list`。
- `def calc(*numbers)`: 使用可变参数接收任意数量的位置参数。
- `for n in numbers`: 遍历可变参数。
- `calc(*nums)`: 使用 `*` 对列表进行参数解包。
- `def person(name, age, **kw)`: 使用关键字参数接收额外信息。
- `person('Bob', 35, city='Beijing')`: 传入关键字参数。
- `extra = {'city': 'Beijing', 'job': 'Engineer'}`: 使用字典保存关键字参数。
- `person('Jack', 24, **extra)`: 使用 `**` 对字典进行关键字参数解包。
- `'city' in kw`、`'job' in kw`: 判断关键字参数中是否包含指定 `key`。
- `def fact(n)`: 定义递归函数。
- `return n * fact(n - 1)`: 使用递归计算阶乘。

## py8: 切片、迭代、列表推导式、生成器、迭代器

- `L[0:3]`: 从索引 `0` 开始切片，到索引 `3` 结束但不包含 `3`。
- `L[:3]`: 省略起始索引，等价于从 `0` 开始。
- `L[-2:]`: 使用负数索引从倒数第二个元素切到末尾。
- `L[:-2]`: 从开头切到倒数第二个元素之前。
- `list(range(100))`: 生成 `0` 到 `99` 的列表。
- `L[:10]`: 取前 `10` 个元素。
- `L[::2]`: 每隔一个元素取一次。
- `tuple` 切片: `(0, 1, 2, 3, 4, 5)[:3]`，结果仍是 `tuple`。
- 字符串切片: `'ABCDEFG'[:3]`，结果仍是字符串。
- `for i in L`: 遍历列表元素。
- `for x, y in [(1, 1), (2, 4), (3, 9)]`: 遍历由 `tuple` 组成的列表并解包。
- 普通循环生成列表: 先创建空列表，再 `append(x * x)`。
- `[x * x for x in range(1, 11)]`: 列表推导式生成平方列表。
- `[x * x for x in range(1, 11) if x % 2 == 0]`: 带条件过滤的列表推导式。
- `[m + n for m in 'ABC' for n in 'XYZ']`: 多重循环列表推导式。
- `d.items()`: 遍历字典的 `key` 和 `value`。
- `[k + '=' + v for k, v in d.items()]`: 用字典条目生成字符串列表。
- `(x * x for x in range(10))`: 生成器表达式。
- `for i in g`: 遍历生成器。
- `def fib(max)`: 定义斐波那契函数。
- `a, b = b, a + b`: 使用多变量赋值更新斐波那契状态。
- `return 'done'`: 函数循环结束后返回结果。
- `from collections.abc import Iterator`: 导入 `Iterator` 类型。
- `isinstance((x for x in range(10)), Iterator)`: 判断生成器是否是迭代器。
- `isinstance([], Iterator)`、`isinstance({}, Iterator)`、`isinstance('abc', Iterator)`: 判断 `list`、`dict`、`str` 是否是迭代器。

## py9: 高阶函数、闭包、匿名函数、装饰器、偏函数

- `def f(x): return x * x`: 定义函数作为 `map()` 的参数。
- `map(f, [1, 2, ...])`: 对可迭代对象中的每个元素应用函数。
- `list(r)`: 把 `map` 返回的迭代结果转换成列表。
- `map(str, [1, 2, ...])`: 把列表元素转换为字符串。
- `from functools import reduce`: 导入 `reduce`。
- `reduce(add, [1, 3, 5, 7, 9])`: 使用 `reduce` 累积计算。
- `def fn(x, y): return x * 10 + y`: 把数字序列合成为整数。
- `def char2num(s)`: 使用字典把字符数字转换为整数。
- `reduce(fn, map(char2num, '13579'))`: 把字符串 `'13579'` 转成整数 `13579`。
- `DIGITS`: 使用常量字典保存字符到数字的映射。
- `def str2int(s)`: 封装字符串转整数逻辑。
- `filter(is_odd, [...])`: 过滤出奇数。
- `filter(not_empty, [...])`: 过滤空字符串、`None` 和空白字符串。
- `yield`: 在 `_odd_iter()`、`primes()` 中生成惰性序列。
- `next(it)`: 获取迭代器下一个值。
- `filter(_not_divisible(n), it)`: 构造新的过滤序列。
- `for n in primes()`: 遍历素数生成器。
- `sorted([...])`: 默认排序。
- `sorted(..., key=abs)`: 按绝对值排序。
- `sorted(words, key=len)`: 按字符串长度排序。
- `sorted(words, key=str.lower)`: 忽略大小写排序。
- `sorted(students, key=lambda x: x[1])`: 按 `tuple` 的第二个元素排序。
- `sorted(students, key=lambda x: x[0])`: 按 `tuple` 的第一个元素排序。
- `sorted(students, key=lambda x: x['score'])`: 按字典中的 `score` 排序。
- `sorted(nums, key=abs, reverse=True)`: 使用 `reverse=True` 降序排序。
- `from typing import Callable`: 导入函数类型标注。
- `def calc_sum(*args)`: 直接计算可变参数求和。
- `def lazy_sum(*args)`: 返回内部函数 `sums`，实现延迟计算。
- `f: Callable[[], int] = lazy_sum(...)`: 用类型标注表示 `f` 是无参返回 `int` 的函数。
- `def count()`: 返回多个闭包函数。
- 闭包变量问题: 内部函数引用循环变量 `i` 时，最终结果会受 `i` 的最终值影响。
- `def f(j): def g(): return j*j`: 通过立即传参固定闭包变量。
- `nonlocal x`: 在内部函数中修改外层函数变量。
- `lambda x: x * x`: 匿名函数。
- `map(lambda x: x * x, [...])`: 把匿名函数传给 `map`。
- `def log(func)`: 定义装饰器函数。
- `def wrapper(*args, **kw)`: 在装饰器内部包裹原函数调用。
- `func.__name__`: 获取被装饰函数名。
- `@log`: 使用装饰器语法装饰 `now()`。
- `int('12345', base=8)`、`int('12345', base=16)`: 使用 `int()` 的 `base` 参数转换进制。
- `def int2(x, base=2)`: 固定默认 `base` 为 `2` 的转换函数。
- `import functools`: 导入 `functools` 模块。
- `functools.partial(int, base=2)`: 创建偏函数，固定 `int()` 的 `base` 参数。

## py10: 模块、命令行参数、私有函数、入口判断

- `# -*- coding: utf-8 -*-`: 声明源文件编码。
- `' a test module '`: 模块文档字符串。
- `__author__ = 'Michael Liao'`: 模块作者信息变量。
- `import sys`: 导入 `sys` 模块。
- `def test()`: 定义测试函数。
- `sys.argv`: 获取命令行参数列表。
- `len(args) == 1`: 没有额外命令行参数时输出 `Hello, world!`。
- `len(args) == 2`: 有一个额外命令行参数时输出带名字的问候。
- `else`: 参数过多时输出 `Too many arguments!`。
- `def _private_1(name)`: 使用下划线开头表示内部使用函数。
- `def _private_2(name)`: 另一个内部辅助函数。
- `def greeting(name)`: 对外提供问候函数。
- `if len(name) > 3`: 根据名字长度选择不同内部函数。
- `if __name__ == '__main__'`: 判断当前模块是否作为脚本直接运行。
- `test()`: 直接运行模块时调用测试函数。
- `print(greeting('Sen'))`: 直接运行模块时输出 `greeting()` 的结果。

## py11.ipynb: NumPy 数组、dtype 与形状

- `import numpy as np`: 导入 NumPy，并使用 `np` 作为常用别名。
- `np.array([1, 2, 3])`: 从列表创建一维数组。
- `np.array([[1, 2], [3, 4]])`: 从嵌套列表创建二维数组。
- `np.array(..., ndmin=2)`: 指定最小维度，强制生成二维数组。
- `np.array(..., dtype=complex)`: 创建指定元素类型的数组。
- `np.dtype(np.int32)`: 使用 NumPy 标量类型创建 dtype。
- `np.dtype('i4')`: 使用字符串简写表示 32 位整数类型。
- `np.dtype('<i4')`: 使用字节顺序标注 dtype。
- `np.dtype([('age', np.int8)])`: 创建单字段结构化数据类型。
- `a['age']`: 通过字段名访问结构化数组中的列。
- `np.dtype([('name', 'U10'), ('age', np.int8), ('height', np.float32)])`: 创建多字段结构化数组类型。
- `np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])`: 使用字节字符串、8 位整数和 32 位浮点数组合结构化 dtype。
- `np.arange(24)`: 创建连续整数数组。
- `a.ndim`: 查看数组维度数量。
- `a.reshape(2, 4, 3)`: 返回调整形状后的数组。
- `a.shape`: 查看或设置数组形状。
- `x.itemsize`: 查看数组中单个元素占用的字节数。
- `x.flags`: 查看数组内存布局、连续性和可写性等属性。

## py12.ipynb: NumPy 常用数组创建函数

- `np.empty([3, 2], dtype=int)`: 创建未初始化的指定形状数组。
- `np.zeros(5)`: 创建元素全为 `0` 的数组，默认 dtype 为浮点数。
- `np.zeros((5,), dtype=int)`: 创建整数类型的全零数组。
- `np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])`: 使用结构化 dtype 创建全零数组。
- `np.ones(5)`: 创建元素全为 `1` 的数组。
- `np.ones([2, 2], dtype=int)`: 创建整数类型的全一二维数组。
- `np.zeros_like(arr)`: 创建与已有数组形状和类型相同的全零数组。
- `np.ones_like(arr)`: 创建与已有数组形状和类型相同的全一数组。
- `np.asarray([1, 2, 3])`: 把列表转换为 ndarray。
- `np.asarray((1, 2, 3))`: 把元组转换为 ndarray。
- `np.asarray([(1, 2, 3), (4, 5)], dtype=object)`: 用 `object` 类型保存不规则嵌套序列。
- `np.asarray([1, 2, 3], dtype=float)`: 转换数组时指定浮点类型。
- `np.frombuffer(b'Hello World', dtype='S1')`: 从字节缓冲区创建数组。
- `np.fromiter(iter(range(5)), dtype=float)`: 从迭代器创建数组。
- `np.arange(5)`: 创建从 `0` 到 `4` 的整数数组。
- `np.arange(5, dtype=float)`: 创建浮点类型的连续数组。
- `np.arange(10, 20, 2)`: 按起点、终点和步长创建数组。
- `np.linspace(1, 10, 10)`: 在闭区间内创建等间隔数组。
- `np.linspace(10, 20, 5, endpoint=False)`: 创建不包含终点的等间隔数组。
- `np.linspace(..., retstep=True)`: 同时返回数组和步长。
- `np.linspace(...).reshape([10, 1])`: 将等间隔结果调整为列向量。
- `np.logspace(1.0, 2.0, num=10)`: 按默认底数 `10` 创建对数等间隔数组。
- `np.logspace(0, 9, 10, base=2)`: 按指定底数 `2` 创建对数等间隔数组。
