#!/usr/bin/env python3

# S=pi*r**2
def S(r):
    return 3.14 * r ** 2

# abs(x) 返回 x 的绝对值
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))


#pass 语句是一个空操作，什么都不做。当语法上需要一个语句，但程序逻辑上又不需要任何操作时，可以使用pass语句。它常用于定义一个空函数或占位符。不仅可以用于函数，还可以用于类和模块中。

# 定义一个空函数
def nop():
    pass
# 定义一个占位符
age = 20
if age >= 18:
    pass

# return语句返回一个值，可以是任何数据类型。可以多个值，用逗号分隔。
import math

def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# None 是一个特殊的值，表示没有值。它是一个对象，类型为NoneType。可以用来表示函数没有返回值，或者变量没有值。
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 调用函数时，如果不传入参数，默认使用None作为参数值。函数内部判断参数是否为None，如果是，则创建一个新的空列表。这样每次调用函数时，都会得到一个新的列表，而不是共享同一个列表。

# 可变参数（*args）和关键字参数在Python中非常有用。它们允许函数接受任意数量的参数，并且可以将这些参数作为元组或字典传递给函数。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


nums = [1, 2, 3]
print(calc(*nums))  # 输出：14
# 关键字参数（**kwargs）允许函数接受任意数量的关键字参数，并且可以将这些参数作为字典传递给函数

# **kwargs 允许函数接受任意数量的关键字参数，并且可以将这些参数作为字典传递给函数。使用 **kwargs 时，函数会将所有未命名的关键字参数收集到一个字典中，参数名作为键，参数值作为值。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30) # 输出：name: Michael age: 30 other: {}

person('Bob', 35, city='Beijing') # 输出：name: Bob age: 35

person('Adam', 45, gender='M', job='Engineer')  # 输出：name: Adam age: 45 gender: M job: Engineer

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra) 

# 可以使用if语句来检查传入的参数是否包含特定的关键字，然后进行相应的处理。例如，在上面的person函数中，我们可以检查是否包含'city'和'job'这两个关键字参数，并根据需要进行处理。
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# 在上面的代码中，我们使用了**kw来接收任意数量的关键字参数，并根据需要进行处理。例如，在上面的person函数中，我们可以检查是否包含'city'

# 可以使用递归函数来计算阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(100))