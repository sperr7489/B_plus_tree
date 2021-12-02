# import copy

# babo = [1, 2, 3, 4]
# test = [23, 12, 111]
# test = copy.copy(babo)


# print(test)
# print(babo)
# babo.append(31)
# print(test)
# print(babo)

# a = 3
# b = 5
# temp = a
# a = b
# b = temp
# print(a, b, temp)


# class Node:
#     def __init__(self):
#         # each node can have |order - 1| keys
#         self.keys = []
#         # |order| / 2 <= # of subTree pointers <= |order|
#         self.subTrees = []
#         self.parent = None
#         self.isLeaf = True
#         # leaf node has next node pointer
#         self.nextNode = None


# a = None
# a = Node()
# if a is not None:
#     print("sibal")

# print(5/2)

# babo = [1, 2, 3, 4]

# print(babo)
# babo = [3, 4, 5]
# print(babo)

# good = []
# print(good)

# -*- coding: utf-8 -*-

from __future__ import print_function
import math


babo = [[1, 2], [3, 4, 5], [12, 2, 1, 5, 1]]
test1 = babo[:1]
test2 = babo[1:]
print(test1)
print(test2)

test1 = test2

test1 = [2, 3, 4, 5, 5, 6, 7, 7]
print(test1)
print(test2)
k = 2
test1.remove(k)

for i in test1:
    print(i)


a = int(math.ceil(5.0/2)-1)
print(a)

good = [1, 2, 3, 4]
print(test1, end='-')
print(good)
