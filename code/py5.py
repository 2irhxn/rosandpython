#!/usr/bin/env python3

# 条件判断if-elif-else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


birth = 2003
if birth < 2000:
    print('00前')
else:
    print('00后')

score = 'B'
if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')

# Python 3.10引入了match语句，可以更简洁地实现多分支判断。
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

# match语句还可以使用if条件来进行更复杂的判断。
age = 3

match age:
    case x if x < 10: # x是一个变量，匹配到的值会赋给x，可以在case后面加上if条件来进行更复杂的判断。
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')


# match语句还可以匹配列表等复杂的数据结构。
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

# for x in iterable: # for循环可以遍历任何可迭代对象，包括列表、字符串、字典等。
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101): # range()函数可以生成一个整数序列，默认从0开始，步长为1，可以指定起始值、结束值和步长。
    sum = sum + x
print(sum)

sum = 0
for i in range(1, 101 ,2): # 可以使用range()函数生成一个奇数序列或偶数序列，步长为2。
    sum = sum + i
print(sum)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
