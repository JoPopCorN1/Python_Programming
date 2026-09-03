# 반복문: while, for
# while문
# 1~10 까지 반복 출력
i=1
while i<=10:
    print(i)
    i+=1
    if i==6:
        break
else:
    print("End")
# with while ~ else
nums=[1,3,5,7,9]
target=2
i=0
while i<len(nums):
    if nums[i]==target:
        print(f"{target} exist!")
        break
    i+=1
else:
    print(f"{target} does not exist")
# without while ~ else
flag=False
nums=[1,3,5,7,9]
target=2
i=0
while i<len(nums):
    if nums[i]==target:
        flag=True
        break
    i+=1
if flag==True:
    print(f"{target} exist!")
else:
    print(f"{target} does not exist")
# 1~10까지의 합
i=0
tot=0
while i<=10:
    i+=1
    if i%2==1:
        continue
    tot+=i
print(f"sum: {tot}")