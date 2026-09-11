from functools import reduce
li = [[1, 20], [3, 4], [5, 0.1]]
# print(*map(lambda x: x**2, li))

# for i in range(len(li)):
#     print(li[i]**2, end=" ")

# # res = reduce(lambda x, y:x + y, li)
# mylist = ['appleeeeeeeeeeeeeeeeee', 'banana', 'cherryyyy']
# mylist2 = sorted(mylist, key=len)
# print(mylist2)
li2 = sorted(li, key=lambda x: x[0]*x[1])
print(li2)
a = [1, 2, 3, 4, 5]
dic = {"a":1, "b":2, "c":4}
b = (1, 2, 3)
print(*a)
print(*dic.values())
print(*b)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li=[1]
# *head, tail = li
head = li[0]
tail = li[1:]

li = head, *tail
print(f"head={head}\ntail={tail}")