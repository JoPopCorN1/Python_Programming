# 문자열
# "" , ''
a = "python"
print(a, type(a))
b = "python"
print(a, type(a))
# I'll be back
print("I'll be back")
print("I'll be back")
multiline = """
Life is short
You need Python
"""
# docstring
print(multiline)


def func():
    # a=1 docstring 은 첫 줄이여야 만 한다
    """이 함수는 테스트용입니다"""
    pass


print(func.__doc__)
# 문자열 연결
print("hello" + "python")
# 문자열 반복
print("Hello " * 10)
print("-" * 100)
# print("Hello" + 10)
print("hello" + str(10))
print("10" + "2")
print(int("10") + int("2"))
# 문자열 포맷팅 (f-string)
name = "pororo"
age = 23
print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이: {age+1}살")
print(f"{name.upper()}")
pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")
num = 123456789
print(f"{num:,}")
print(f"{num:15,d}")
print(f"{num:<15,d}")
print(f"{num:015,d}")