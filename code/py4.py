#usr/bin/env python3

#list
classmate = ['Michael', 'Bob', 'Tracy']
print(classmate[0]) # 访问列表中的第一个元素，索引从0开始
len(classmate) # 获取列表的长度
classmate[-1] # 访问列表中的最后一个元素，索引从-1开始
classmate.append('Adam') # 在列表末尾
print(classmate) # 打印列表内容
classmate.insert(1, 'Jack') # 在列表中插入元素，索引从0开始
print(classmate) # 打印列表内容
classmate.pop() # 删除列表中的最后一个元素
print(classmate) # 打印列表内容
classmate.pop(1) # 删除列表中的指定
print(classmate) # 打印列表内容
classmate.remove('Bob') # 删除列表中的指定元素，如果存在多个相同的元素，删除第一个出现的元素
classmate[1] = 'Bob' # 修改列表中的指定元素
print(classmate) # 打印列表内容
classmate.clear() # 清空列表内容
print(classmate) # 打印列表内容
L = ['Apple', 123, True] # list可以包含不同类型的数据，包括字符串、数字和布尔值等。
s = ['python', 'java', ['asp', 'php'], 'scheme'] # list可以包含其他list，形成嵌套结构。
print(L[2]) # 打印列表中的指定元素
print(len(s)) # 计算列表的长度
print(len(s[2])) # 计算嵌套列表中元素的数量
print(s[2][0]) # 访问嵌套列表中的元素

#tuples是不可变的数据类型，一旦创建就不能修改。可以使用()或tuple()函数来创建一个元组。
classmates = ('Michael', 'Bob', 'Tracy') # 创建一个元组
t = ('a',) # 创建一个包含单个元素的元组，注意逗号
p = ('a', 'b', ['A', 'B']) # 元组可以包含其他数据类型，包括列表
p[2][0] = 'X' # 修改嵌套列表中的元素
p[2][1] = 'Y' # 修改嵌套列表中的元素
print(p) #tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

