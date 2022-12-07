# 출력 - print()
# 입력 - input()
# 변수 - num = 10 그냥 타입없이 변수만
# 타입변환 - str() 문자열, int() 정수, float()실수
# 출력포멧 - print( "{0}".format(10) ), print("{0} {1}".format(10,"변수정"))

# 문제 1.
# 시속 v km/h로 달리고있는 자동차가 반지름 r km인 원형트랙을 달리고 있다면
# 한바퀴 완주하는데 걸리는시간은 몇분인가? 소수점한자리까지 출력
# 자동차 속도와 반지름을 입력하여 구하기

# v = int(input("자동차 속도 : "))
# r = int(input("트랙 반지름 : "))
# result = (2 * 3.14 * r) * 60/v

# print ("완주 시간 : {0:0.1f}분".format(result))

# 문제 2
# 소주 한잔에 수명이 2분 단축된다.
# 지연이가 소주를 20년동안 마셨다.
# 그렇다면 지연이는 수명이 총 몇 분 줄었는가 ?
#                        총 몇 시간 ?
#                        총 몇일?
# 하루에 소주를 몇잔 마시는지 입력하여 세가지 구해 출력
"""
소주 = int(input("하루에 몇잔 마셨냐 : "))
인생 = 소주 * 2 * 365 * 20
print("김지연 단축 수명 : {0:0.0f}분".format(인생))
print("김지연 단축 수명 : {0:0.0f}시간".format(인생/60))
print("김지연 단축 수명 : {0:0.0f}일".format(인생/60/24))
"""


""" x,y,z,a = "김지연","장영주","변수정","이지현"
a=b=c="연하남친"
favorite = ["목발","선인장","19남친"] #리스트
a,b,c = favorite
print(a)
print(b)
print(c)
"""

"""
    같다 -> == , 같지않다 -> !=, >  <   >=  <=
"""
""" num = 19
num1 = 27

if num1 > num :
    print("누난 내 여자니까!")
else :
    print("누난 늙었어...")
    print("여기는 그냥 출력")

if num1 > num :
    print("연하가 좋아")

age = 22

if age > num :
    print ("내가 형이니까 내가 가지겠어 누나!")
elif num > age :
    print ("내가 더 연하야!!")
else : 
    print ("둘다 싫어! 난 이제 연상 좋아")
# elif = else if

name = "김지연"

print("미안합니다.. 그만할게요") if name == "김지연" else print ("농일세") if num1 != 27 else print("뻥인데 계속할껀데")
 """
# 범위 주석 - 드래그 후 alt + shift + a

# 문제 3
# 지연이와 기원이가 오락실에 갔다.
# 둘이 오붓하게 펀치 게임을 하였다.
# 지연이와 기원이의 펀치 점수가 각각 얼마인지 입력 하여 누가 이겼는지 출력하시오

"""
기원 = (input("기원이 펀치 점수 : "))
지연 = (input("지연이 펀치 점수 : "))

if 기원 > 지연 :
    print("기원 점수 : " + 기원 + "점, 지연 점수 : "+ 지연 + "점, 결과 : 기원 승")
elif 기원 < 지연 : 
    print("기원 점수 : " + 기원 + "점, 지연 점수 : "+ 지연 + "점, 결과 : 지연 승")
else :
    print("기원 점수 : " + 기원 + "점, 지연 점수 : "+ 지연 + "점, 결과 : 비김")
"""

# and or not?
# 문제 4
# 영주하고 지연이하고 수정이다
# 시험을 봤다. 세명의 시험점수를 입력하고 세명의 총합 등급이 어떻게 되는지 출력하기
# 90점 이상은 A, 80점 이상은 B, 70점이상은 C, 나머지점수는 "쯧쯧 ...." 출력하기


"""
young = int(input("영주 점수 : "))
ji = int(input("지연 점수 : "))
soo = int(input("수정 점수 : "))
# 변수 이름은 맨 앞글자 숫자이면 안됨 단 _(언더바)만 허용

result = (young + ji + soo) / 3


if result >= 90 :
    print("세명의 등급은 ? : A 등급")
elif result >= 80 :
    print("세명의 등급은 ? : B 등급")
elif result >= 70 :
    print("세명의 등급은 ? : C 등급")
else :
    print("쯧쯧 .... 어쩌다....")
"""

# while(반복문)
""" 
i = 1
while i <= 10 :
    print(i)
    i += 1
 """
# 구구단 4단 출력 해보세요
# 4 * 1 - 4 => 이렇게 출력하기
""" 
a = 1
while a <= 9 :
    # 방법 1 print("4 * "+ str(a)+ " = " + str(a*4))
    # 방법 2 print("4 * {0} = {1}".format(a, a * 4))
    print("4 * "+ str(a)+ " = " + str(a*4))
    a += 1
 """

""" 
i = 1
while i < 5 :
    print(i)
    i+=1
else :
    print("5보다 크면 반복문 종료됨")
 """
""" 
i = 1
while True :
    print(i)
    if i == 100 : break
    i += 1
 """

"""
# while 문 마지막 문제
# 배꼽지연이가 연하 남친을 만나려고 교통카드 10000원 충전하였다
# 지연이가 버스를 몇번 탈 수 있는가? 잔액은 얼마인가?
# 버스요금은 1200원
# 반드시 while문을 사용할 것

# 방법 1 (True)
ji = 10000
count = 0
result = 0
while True :
    if ji < 1200 : break
    ji -= 1200
    count+=1

print("버스를 탈 수 있는 횟수 : "+str(count) +"번" + ", 잔액" +str(ji)+"원")

# 방법 2
card = 10000
bus = 1200
count = 0
while card >= bus :
    card -= bus
    count+=1
print("버스를 탈 수 있는 횟수 : "+str(count) +"번" + ", 잔액" +str(ji)+"원")
"""

# range(10) = 반복횟수 0부터 10번 (반복횟수)
# range(1, 10) = 반복 1부터 시작하여 10전까지 (시작 값, 종료값)
# range(1, 10, 3) = 1부터 10전까지 3씩 증가해라 (시작 값, 종료 값, 증가 값)
"""
for i in range(1, 10, 3) :
    print(i)
"""
""" 
a = 1
for i in range(8, 79, 8) :
    a+=1
    print("8 * " + str(a) + " = "+str(i))

for i in range(1, 10) :
    print("8 * {0} = {1}".format(i, i * 8))
 """

"""
# 45부터 109까지 출력하시오

for i in range(45, 110) :
    print(i)
 """

