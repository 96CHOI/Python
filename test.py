x = 9
print("output : " + str(x))
print("output : {0}".format(x) )

a = 3.14
print("float : {0}".format(a))
print("float : {0:.1f}".format(a))
## .1f = 소숫점 한자리 표현 (.)

print(type(a) )
# type : 데이터 타입을 알 수 있다.

name="이정수"
print("이름 : {0:s}".format(name))
print("이름 : "+name)
memo="를 김민정이 때렸다."

result = name + memo
print(result)

res_len = len(result)
print(res_len)
# len : 문자열의 총 길이

temp1 = result.split()
print(temp1)

# split() : 기준없이 사용하게되면 띄어쓰기를 기준으로 나눔.
temp2 = result.split(" ", 1)
print(temp2)
# split(" ", 1) : 띄어쓰기 기준으로 딱 한번만 나누도록 설정.

print(" {0}".format(",".join(temp1)))
# join : 문자열 배열을 합치는 함수 "%".join(배열) 하면 각배열의 요소사이사이에 %가 붙은상태로 합쳐진다.
""" 이것도 주석으로 사용하기도 함(따옴표 3개) alt + shift + a """

num = int(input("숫자를 입력하세요 : ")) # input은 입력함수이다.  결과는 문자열로 반환한다.
# int 타입으로 변환하고 싶을 시 int()로 감싸줘야함.
print( type(num))

# 정수타입변환 int() - 정수(1, 2 ,3 ,4)
# 실수타입변환 float() - 소숫점
# 문자열 타입 변환 str()

""" 문제 1.  국어,  수학,  영어 세과목 점수 입력받아서  평균을 구하여 출력"""


kor = int(input("국어 점수 : "))
mat = int(input("수학 점수 : "))
eng = int(input("영어 점수 : "))
total = kor + mat + eng
print("국어 : " + str(kor) + " 수학 : " + str(mat) + " 영어 : " + str(eng))
result = total / 3
print("평균 : " + str(result) + "점")
print("평균 : {0}".format(result) + "점")
