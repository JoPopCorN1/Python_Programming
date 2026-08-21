# 변수
# 동적 타이핑 언어
a=2
b=3
print(a,end="")
print(b)
print(a,b,sep="")
# a=2,b=3 -> a=(2,b)=3 튜플화 되어 오류남
a=2,3
print(a)
print(type(a))
a=3; b=4
print(a,b)
x=y=z=0
a,b=4,5 # == (4,5)라는 튜플을 언패킹하여 각각 변수에 저장
# 값 swap
temp=a
a=b
b=temp
print(a,b)
# swap 파이썬 스타일
a,b=b,a
print(a,b)
# 변수명 규칙 (C와 동일)
# 문자, 숫자, 언더바만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가
name2="pororo"
# 2name="pororo"
_name="crong"
# class=123
# name!="hello"
# C와 차이점: 다국어 변수명 가능 (비추천)
이름="뽀로로"
print(이름)
student_name="크롱" # snake (주로)
studentName="크롱" # camel
MAX_COUNT=100 # 대문자로만 이루어지면 상수