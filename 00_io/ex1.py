a = input()
print(a, end="")
print(type(a))
print(100, type(a), sep=",")

a = int(a)
print(a, type(a))

a = int(input())
print(a, type(a))

b=float(input())
print(b, type(b))

a = input().split()
print(a, type(a))

a, b, c = map(int, input().split())
print(a, b, c)

a = list(map(int, input().split()))
print(a, type(a))