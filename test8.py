#함수
#자바의 메소드
# 반환타입 메소드이름(매개변수){ 메소드 실행내용; 반환타입있다면 return; }
#자바스크립트 함수
# function 함수이름(매개변수){   함수 실행 내용; 반환값있다면 return;    }

#파이썬 함수
# def 함수이름(매개변수):

#정의된 함수 실행방법 → 함수이름()
"""
def sum(a,b):
    return a+b

res = sum(10,20)
print(res)

def func():
    print("나 함수다")

func()

def func1(word):
    print(word+"이다.")

func1("난 바보")

def minus(num1,num2):
    print(num1-num2)

minus(30,15)

def whoami(name,what):
    if name == "장영주":
        print(name+"는(은)"+what+"이다.")
    else:
        print(name+"는(은)"+what+"가 아니다.")

whoami("장영주","바보")
whoami("김지연","바보")

def count(i):
    return i+1

cnt=0
while cnt<10:
    cnt=count(cnt)

print(cnt)

cnt1=0 # 전역변수 count2 보다 먼저 생성한다.

def count2():
    global cnt1 # 파이썬의 전역변수 - count2 함수에서 cnt1을 사용하고자 한다면 global 붙여서
                # 전역변수임을 알려주고 사용한다.
                # 전역변수는 최소함으로만 사용 - 코드의 유지보수를 어렵게한다.
                # 전역변수를 마구 생성하여 사용하면 정신적인 데미지를 입는다.
    cnt1+=1

while cnt1<10:
    count2()
print(cnt1)

# 문제
# 정수 하나를 입력받아서 함수를 통해 해당 정수의 값을 100증가 시키고 줄력하기

def add100(n): # 100이 증가하는 함수 정의 지정된 값 100증가해야 하니까 매개변수 필요
    print (n + 100) # 증가시키고 출력하기 

num = int(input("정수입력 : ")) # 정수 입력받기
add100 (num) #  100증가 시켜주는 함수 호출하여 입력받은 숫자를 함수에 넘겨주기
"""
"""
# 첫번째 할것 . 정수 두개 입력받기 (변수 두개)
# 두번째 할것 . 정수 입력받는 코드 위에 함수 만들기
#              함수의 내용은 두숫자를 곱해서 출력하는 내용
# 세번째 할것 . 정수 입력받는 코드 밑에 함수호출하기

def x(n1, n2):
    print(n1 * n2)

n1 = int(input("정수1 입력 : "))
n2 = int(input("정수2 입력 : "))
x(n1 , n2)

# 첫번째. 리스트 만들기
# 두번째. 리스트에 1~50까지 짝수만 저장하기
# 세번째. 리스트만들기 코드 위에 함수 만들기
#         함수내용은 함수에 입력된숫자에 +1 해서 출력하기
# 네번째. 리스트를 반복문 이용하여 함수 호출하기 , 함수에 리스트값 입력

def add1(n):
    print(n+1)

li = [i for i in range(1, 50) if i % 2 == 0]

for i in li:
    add1(i)
"""


# 세과목 점수를 입력받아서 총점과 평균을 구할것이다.
"""
def score_input(subj):
    scr=[] # 함수 내부에서 입력한 점수를 리스트에 저장해야하기에 리스트 만든것 함수꺼다.
    for sub in range(len(subj)):
        scr.append( int(input(subj[sub])) )
    return scr # for문으로 입력한 점수가 저장된 리스트src를 돌려 보내야 한다.
    # 그래야 실 사용하고자 하는곳에서 값을 사용하니까

def total(점수들): # 총점 계산하기 용 함수
    tot = 0 
    for i in 점수들:
        tot += i# 입력한점수 전부 더하기
    return tot

def avg(총점): # 평균 계산하기 용 함수
    평균 = 총점 / 3
    print("총점 : {0}, 평균 : {1}".format(총점, 평균))

score = []
subj = ("국어 점수 : ","영어 점수 : ","물리치료 : ")

score = score_input(subj) # 튜블로 만든 subj를 함수에 보낸다. subj의 주소를 보내는것

tot = total(score)

avg(tot)
"""

# 장영순, 김지연, 이지형의 키를 입력하여 평균키를 구하시오
# 평균키보다 작은 사람은 누구인지 출력하기
# 평균키 계산하는 함수
# 작은키 누구야
"""
hei = []
hlist = ("장영순 : ", "김지연 : ", "이지형 : ") 

def res_input(hlist):
    res = []
    for hei in range(len(hlist)):
        res.append( int(input(hlist[hei])) )
    return res
def total(k):
    tot = 0
    for i in k:
        tot += i
    return tot
def avg(x):
    a = x / 3
    print("키 총합 : {0}, 평균 : {1}".format(x, a))
hei = res_input(hlist)
tot = total(hei)
avg(tot)
# hei (키 3명)
# avg(총합)
"""

"""
cutegirls = ("장영순 ", "김지언 ", "이지형 ")

def small(avg, tall):
    global cutegirls
    for i in range(len(tall)):
        if avg > tall[i]:
            print("평균보다 작은 사람 : {0}".format(cutegirls[i]))

def tall_avg(tall):
    sum = 0
    for k in tall: sum += k
    avg = sum/len(tall)
    print("평균 키는 : " + str(avg))
    small(avg, tall)

def tall_input():
    global cutegirls
    tall = []
    for a in cutegirls:
        tall.append( int(input(a)))
    tall_avg(tall)

tall_input()
"""

# 간단한거
# 리스트에 1부터 50까지 저장하기
# 리스트에 저장된 숫자 중에서 5의 배수만 출력하기
# 5의 배수를 찾아서 출력하는 함수 만들서 하기
"""
li = []
for i in range(1, 51):
    li.append(i)

def five(li):
    for i in li:
        if i % 5 == 0:
            print("5의 배수 : " + str(i))
five(li) #function 값 불러오는 것 처럼 반드시 써줘야함 (print 아님)
"""
"""
#=======================

def func(a,b,c):
    print(a)

func(a="abc", b="b",c= "c")

#==========================

def func1( national="계림국" ):
    print(national)

func1("대한민국")
func1()

#===============================
# key로 value 값을 넣어줘야 출력 가능 (여러개도 가능)
def func2(**info):
    print(info["name"])
    print(info["상태"])

func2(name="장영주",상태="천재,아름다움,귀여움")
"""
# 첫번째 리스트에는 이순신, 장영실, 정몽주, 이성계, 이방지의 키를 입력
# 두번째 리스트에는 이순신, 장영실, 정몽주, 이성계, 이방지의 몸무게를 입력
# 키가 가장 작은 사람 찾는 함수
# 몸무게 가장 높은 사람 찾는 함수


# kgli = ["이순신","장영실","정몽주","이성계","이방지"]

cm = []
cmli = ["이순신 ","장영실 ","정몽주 ","이성계 ","이방지 "]

def cm_input(cmli):
    res=[]
    for i in range(len(cmli)):
        res.append(int(input(cmli[i])))
    return res

def result(cmli, small):
    a = cmli[0]
    min = small[0]; 
    for i in range(len(small)):
        if min > small[i]:
            min = small[i]
            a = cmli[i] 
    print("가장 작은 사람 : " + a, min)
cm = cm_input(cmli)
a = result(cmli, cm)

kg = []
kgli = ["이순신 ","장영실 ","정몽주 ","이성계 ","이방지 "]

def kg_input(kgli):
    res = []
    for i in range(len(kgli)):
        res.append(int(input(kgli[i])))
    return res

def result(kgli, pig):
    x = cmli[0]
    big = pig[0]
    for i in range(len(pig)):
        if big < pig[i]:
            big = pig[i]
            x = kgli[i]
    print("가장 무거운 사람 : " + x, big)

kg = kg_input(kgli)
x = result(kgli, kg)