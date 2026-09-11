# for

# C
# for(int i=0;i<10;i++) {
    
# }

# Python
# for i in iterable객체:

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

for i in range(1,6):
    print(i, end=" ")
print()

for i in range(0, 11,2):
    print(i, end=" ")
print()

for i in range(5,0,-1):
    print(i, end=" ")
print()

tot=0
for i in range(1,11):
    tot+=i
else:
    print(f"tot={tot}")
    
print(sum(range(1,11)))

s="hi12한글韓字🔪 🥷 🔪"

for c in s:
    print(c, end=" ")
    
print("\n",len(s))

for i in range(2,10):
    for j in range(1,9):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()