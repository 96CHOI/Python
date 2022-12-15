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