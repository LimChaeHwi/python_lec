# 문자열 포맷팅 
age = 20
name = 'Swaroop'

print '{0} was {1} years old when he wrote this book'.format(name, age)
print 'Why is {0} playing with that python?'.format(name)
# 변수에 값 대입 
i = 5
print i
i = i+1
print i
# 문자열 연결하기 두줄
s = '''This is a multi-line string.
This is the second line.'''
print s
# 문자열 연결하기 한줄
s = 'This is a multi-line string. \
This continues the string.'
print s
# 문자열 한줄로 붙이기
print 'a',
print 'b'
# + 덧셈 연산자
print 3+5
print 'a'+'b'
# - 뺄셈 연산자
print -10
print 50-27
# * 곱셈 연산자
print 3*2
print 3**2
# /나눗셈 연산자
print 6/3
# %나머지 연산자
print 13%3
# lamda 람다 수식
# if - else 조건 수식
# or, and, not x, in ,not in, is, is not

# (,) 한칸 띄우면서 문자열 연결 
length = 5
breadth = 2
area = length * breadth
print 'Area is',area
print 'Perimeter is',2*(length+breadth)
