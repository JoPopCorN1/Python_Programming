# 불리언
# True or False
a = True
print(a, type(a))
print(1 < a)
print(1 > a)
print(1 == a)
print(1 != a)
print("apple" > "banana")
print("apple" > "apble")
# bool()
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool([10]))
print(bool([]))
# None 자료형
a = None
print(type(a))
print(bool(a))
if a is None:
    print("값이 없습니다")
