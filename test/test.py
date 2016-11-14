#!/usr/bin/python
# -*- coding: UTF-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']

print len(classmates)

print classmates.append('Adam')

print classmates.insert(1, 'Jack')

print classmates.pop()

classmates = ('Michael', 'Bob', 'Tracy')

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

d = set([1, 2, 3])


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print map(char2num, '12345')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print f1()
print f2()
print f3()
print range(1, 4)
f3 = count

if __name__ == '__main__':
    count()
