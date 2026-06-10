#!/usr/bin/env python3

#dict
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d)
d['Jack'] = 90
d['Jack'] = 88 #覆盖Jack原来的值
print(d)
d.pop('Bob') #删除Bob的键值对
print(d)

#set
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
s.discard(5) #不报错，如果不存在则不会报错
print(s)

s = set([1, 2, 3])
print(s)
s = {1, 1, 2, 2, 4, 3, 3,}
print(s)

p = {1,2,6,'apple', 'banana', 'cherry'}
print(s & p) #交集
print(s | p) #并集
