import copy

babo = [1, 2, 3, 4]
test = [23, 12, 111]
test = copy.copy(babo)


print(test)
print(babo)
babo.append(31)
print(test)
print(babo)

a = 3
b = 5
temp = a
a = b
b = temp
print(a, b, temp)


class Node:
    def __init__(self):
        # each node can have |order - 1| keys
        self.keys = []
        # |order| / 2 <= # of subTree pointers <= |order|
        self.subTrees = []
        self.parent = None
        self.isLeaf = True
        # leaf node has next node pointer
        self.nextNode = None


a = None
a = Node()
if a is not None:
    print("sibal")

print(5/2)

babo = [1, 2, 3, 4]

print(babo)
babo = [3, 4, 5]
print(babo)
