# 반복문
i = 0
while i<10:
    i+=1
    print(i)
    # if i==5:
    #     break
else:       # 조건식이 false로 인해 빠져 나갔을 때 실행
    print("END")
    
nums = [1,3,5,7,9]
target =3
i=0
while i < len(nums):
    if nums[i]==target:
        print("찾음")
        break
    i+=1
else:
    print("못찾음")
    
i=1
tot=0
while i<=10:
    tot +=i
    i+=1
print(tot)
i=0
tot=0
while i<=10:
    if i%2:
        pass
    else:
        tot +=i
    i+=1
    
print