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
""" 
# 1부터 100까지 출력되는데
# 3의 배수에서는 윤재영 출력
# 5의 배수에서는 바보 출력

for i in range(1, 101):
    if i % 3 == 0 :
        print("윤재영", end="")
    if i % 5 == 0 :
        print("바보")
 """
""" 
# 파이썬 데이터 타입
# 리스트, 튜플, 딕셔너리, 셋, 배열

# list는 대괄호 []
name = [ "장영주", "김지연19", "윤재영"]
print(name)

# 논리 타입도 가능
data1 = ["김기원", 100, 3.14, True]
print(data1)

# 이렇게도 만들 수 있다.
data2 = list(("최윤도", "변수정", 100))
print(data2)

print(data2[0])

# 파이썬은 인데스 -1을 하면 오류가 아님
# -1을 하면 역행하여 마지막 인덱스가 출력됨.
print(data2[-1])

data3 = ["이종빈", "윤종찬", "이지현", "장영주"]
# 범위를 지정하여 출력 가능함 (1부터 3전까지 범위 출력)
print(data3[1:3])
# 범위지정 (0번 ~ 3번전 까지)
print(data3[:3])
# 범위지정 (2번 ~ 마지막 까지)
print(data3[2:])

# 데이터 추가
# append
data3.append("김지연")
data3.append("윤재영")
print(data3)
# 1. 데이터 지우기
# remove
data3.remove("장영주")
print(data3)
# 2. 데이터 지우기
# pop - 마지막 순서 데이터 지우기
data3.pop()
print(data3)
# 3. 데이터 지우기
# del - 인덱스를 통해 삭제
del data3[2]
print(data3)
# 4. 데이터 지우기
# clear 리스트 완전 삭제
data3.clear()
print(data3)
"""
""" 
memo = ["나", "김지연", "은", "19세 남친을", "원한다"]
for me in memo:
    print( me, end="" )

# 데이터 변경
memo[3] = "대머리 남친을"
print()
for me in memo:
    print(me, end="")

# 범위를 지정해서 데이터 변경 가능
memo[1:4] = ["장영주", "는", " 목발을 "]
print()
for me in memo:
    print(me, end="")

# 원하는 위치에 새로운 데이터 추가
memo.insert(3, "드러운 어그와")
print(memo)

# 리스트 합치기
# 첫번째리스트.extend(두번째리스트)
memo1 = ["이종빈", "윤재영", "변수정"]
memo2 = ["장영주부", "김지연세많음", "이지현왕언니"]
memo1.extend(memo2)
print(memo1)

# 리스트 안에 데이터 수 구하기
# len(리트스명)
print( len(memo1) )
"""

# 리스트 생성
# 1. memo = ["a", "b", "c"]
# 2. memo = list(("짱","영","주","땡"))
# 데이터 추가 memo.append("리정수")
# 데이터 삽입 memo.insert(2, "김민정수리")
# 데이터 삭제
# 삭제데이터 지정 memo.remove("땡")
# 마지막데이터삭제 memo.pop()
# 인덱스로 삭제 del memo[3]
# 리스트합치기 memo.extend(리스트)
# 리스트 크기 len()
# 갯수 구하기 memo.count("장")  -   장 이라는 데이터가 몇개있냐?
# 인덱스 찾기 memo.index("영") - 영 이라는 데이터는 몇번 인덱스냐?
# 정렬  memo.sort() - 오름차순   ,   memo.sort(reverse=True) - 내림차순
# 반전  memo.reverse()
# 

info501 = ["장영주는 폭력적이다.", "김지연은 연하만좋아한다.", "윤재영은 옆반쌤좋아한다.",
            "최윤도는 영주불행이 행복이다.", "수정이는 생일이라 코딩이싫데...", "종빈이는 지금 게임한다."]

# 501호 딸기반 학생 이름 을 input으로 입력받기
# info501에 해당 학생 이름이 있다면 학생의 정보를 출력하시오
""" 
name = input("딸기반 학생 이름 : ")


for i in info501:
    if i.count(name) == 1 :
       result = "학생정보: " + str(i)
       break
    else:
        result = "없는 정보입니다 다시입력해주세요."
print(result)
 """
# 문제 2. info501에서 좋아한다 문구가 있는 정보들 모두 출력
# 1번째 방법
""" 
a = "좋아한다"
for i in info501:
    if i.count(a) == 1 :
        print(i)
 """
# 2번째 방법
""" 
word = "좋아한다"
for info in info501 :
    if word in info:
        print(info)
 """

num = [x for x in range(10)]
print(num)