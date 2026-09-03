# for문
# for (int i=0; i<10; i++) (C)
# for i in iterable객체:
for i in range(5):
    print(i,end=" ")
print()
a=range(5)
print(a.start,a.stop,a.step)
# 1~5
for i in range(1,6):
    print(i,end=" ")
print()
# 1~10, 2씩 띄워서
for i in range(1,10,2):
    print(i,end=" ")
print()
# 5 4 3 2 1
for i in range(5,0,-1):
    print(i,end=" ")
print()
# 1~10 까지의 합
# sum=0 변수 선언은 가능하나 충돌가능성 있으니 주의
tot=0
for i in range(1,11):
    tot+=i
print(f"sum: {tot}")
print(sum(range(1,11)))
s="hi안녕12@@😊❤️💕👍🙌"
for c in s:
    print(c,end=" ")
print()
print(len(s))
# 구구단 출력
# 2 * 1 = 2 ....
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j:<5d}",end="")
    print()
else:
    print("End")