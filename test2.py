import random

""" # 랜덤
num = random.randint(1,45)
# num2 = random.randint(1,100)
print("나" + num)
print("컴퓨터" + num2)

if num > num2:
    print("유저 승리" + num + num2)
if num == num2:
    print("비김")
else :
    print("컴퓨터 승")
print(num)
"""

# firstname = ["김", "장", "이", "최", "윤", "변"]
# middle = ["기", "지", "영", "윤", "재", "종", "수", "민", "다"]
# last = ["원", "연", "현", "영", "도", "똥", "순", "숙"]

# a = random.choice(firstname)
# b = random.choice(middle)
# c = random.choice(last)

# print(a,b,c)
""" 
info = [["김기원", "콘샐러드", "시험"], ["이지현","나이","민감"], 
        ["김지연","바람","선생님배꼽찔러봄"], ["장영주", "바르보사", "공통점"],
        ["윤재영", "비니", "강균성"], ["리정수", "군대", "인민군"] ]
 """
# 2차원 리스트
""" 
for i in info: # i 변수에는 info리스트에서 1차원 리스트만 저장 ["리정수", "군대", "인민군"]
    for k in i: # k 변수에는 i에 저장된 ["리정수", "군대", "인민군"] 중에서 하나씩 저장
        print(k)
 """
# 문제 3. 위 info 리스트에는 이름, 특징1, 특징2, 저장되었다
#         특징을 입력받아서 해당 특징을 가진 사람의 이름을 출력하시오
""" 
name = input("특징 : ")
for i in info:
    for k in i: 
        if i.count(name) == 1:
            print(i[0])
            break
"""
"""
name = input("특징 : ")
for i in info:
    for k in i: 
        if k.count(name) == 1:
            result = name + "(이)라는 특징을 가진 사람은 : " + i[0] + "입니다."
        else :
            result = name + "(이)라는 특징을 가진 사람은 없습니다."
print(result)
 """
info = [["김민서", "군인", 28], ["정다현", "디자이너", 45], ["장영주", "트럭기사", 61],
        ["김지연", "밸리댄서", 34], ["윤재영", "수필가", 58], ["최윤도", "모필가", 24],
        ["변수정", "멕시코음식전문점사장", 33], ["이종빈", "프로게이머연습상대", 39],
        ["윤종찬", "파이터only서린", 22], ["이지현", "뒷방...", 69], ["이정수", "초딩", 11],
        ["김민정", "헤어디자이너", 28]]

# 문제 4. 나이대 별로 몇명 인지 구하여 출력
#         30대 사람들의 직업 만 출력
#         가장 나이 많은 사람의 이름과 직업 출력
""" 
# 내가 푼 방식
for i in info:
    if i[2] > 29 and i[2] < 40 :
        print("30대인 사람의 직업은 : " + str(i[1]))
 """
#  선생님
age = [0, 0, 0, 0, 0, 0, 0]
age30 = []
연장자 = ""
max = 0
for 개인 in info:
    age[int(개인[2]/10)] += 1
    if 개인[2] >= 30 and 개인[2] < 40:
        age30.append(개인[1])
    if max < 개인[2]:
        max = 개인[2]
        연장자 = 개인

print(str(age))
print("30대인 사람들의 직업은 : " + str(age30))
print("나이가 가장 많은 사람의 정보 : " + str(연장자))
