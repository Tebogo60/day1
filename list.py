# append works like push in javascript
arr = ["c", "b", "a"]
arr.append("d")
arr.sort()
print(arr)

arr.append(["e", "f"])
print(arr)
print(arr[4][0])

# extend works like a += operator
arr2 = [1, 2, 3]
arr2.extend([4, 5])
print(arr2)

arr3 = ["z", "x"]
arr3.insert(1, "y")
print(arr3)

arr3.remove("x")
print(arr3)

# pop works almost the same as remove but with pop you specify the position of the value you want to remove
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.pop()
a.pop(0)
print(a)