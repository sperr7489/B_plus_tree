n = 4
print(n)
n = 6
print(n)

test = [1, 2, 3, 4, 5]
n = test
print(n)

test = [[1, 2], [3, 4], 6]
test += [2, 3, 4]
test.remove([3, 4])
print(test)
print("---------------------------")
for i, name in enumerate(test):
    print(name)

p = [[2, 3], [1], [5, 7]]
p.sort()
print(p)
