import random

name = ["김유신", "이순신", "어영담", "이성계", "장영실", "홍길동", "김지연", "김춘추"]
job = ["군인", "국회의원", "과학자", "도둑", "건설업자", "밸리댄서", "변호사"]
age = [24, 35, 37, 21, 28, 41, 29, 35, 42]

info = []


for i in range(10):
    info.append([random.choice(name), random.choice(job),random.choice(age)])
   
    # if info[2] >= 20 and info[2] < 30:
    #     age20.append(info[0])
    #     print("20대인 사람은 : " + info)

# info 리스트로 작업하기
# 1. 직업이 군인 인 사람은 누구인지 이름출력
# 2. 작업이 과학자인 사람들의 평균 나이 출력
# 3. 나이가 이십대인 사람들의 직업은 무엇인지 출력하기
""" 
print("======군인인 사람은?======")
a = []
x = []
age20 = []
for i in info:
    # 군인인 사람 구하기 방법1
    if i[1] == job[1]:
        x.append(i[0])
if x != 0:
    print("군인인 사람은? : " + str(x))
else:
    print("군인아저씨는 없습니다.")

# 군인인 사람 구하기 방법2
for i in info:
    if "군인" in i:
        print("직업이 군인인 사람 ==> " + str(i[0]))
print("======과학자 평균나이======")
age = 0
cnt = 0
for i in info:
    if "과학자" in i:
        age += i[2]
        cnt+=1
if cnt != 0:
    print("과학자 평균 나이 : " + str(age/cnt) + "세")
else:
    print("과학자는 없습니다.")
print("======20대의 직업군======")
for i in info:
    if i[2] >= 20 and i[2] < 30:
        age20.append(i[1])
print("20대인 사람의 직업은? : " + str(age20))
 """
# 랜덤 사용방법
# random.randint(1, 40) => 1 ~ 40중에서 랜덤
a = [] # 랜덤범위 1 ~ 30
b = [] # 랜덤범위 10 ~ 50
c = [] # 랜덤범위 1 ~ 100

num = []
# a,b,c 리스트에 각각 15개씩 랜덤 범위에 맞춰서 저장
# a,b,c 리스트에 값중에서 중복인 값만 찾아서 num리스트에 저장하기
# 중복값이 하나도 없다면 중복 없다 라고 출력

""" for i in range(1, 16):
    a.append(random.randint(1, 31))
    b.append(random.randint(10, 51))
    c.append(random.randint(1, 101))
print(a)
print(b)
print(c)

for x in a: # a리스트의 값을 하나씩 하나씩 x 변수에 저장
    if x in b: # x변수의 값이 리스트 b에 있냐
        if x in c: # x변수의 값이 리스트 b에는 있는데 리스트 c에도 있냐
            num.append(x)
if len(num) != 0: #len(num) -> num리스트의 크기값 0이라면 없다. , not num -> num이 비었다면 false
    print("셋다 중복인 값은 : " + str(num))
else:
    print("중복값은 없습니다.") """


word = ["boy", "table", "book", "girl", "interest", "limit", "endless", "mission",
    "hopi", "tigerprint"
]

eng = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
"w","x","y","z"]

# eng 리스트의 알파벳을 무작위 조합해서 word 리스트의 단어 중 1개이상 나오는 경우
# 몇 번째 조합에서 나오는지 출력

res = ""
cnt = 0

while(True):
    cnt += 1
    l = random.randint(3,10)
    for i in range(l):
        res += random.choice(eng)
    if res in word:
        break
    res=""

print(res+"가 생성되기 까지의 횟수 : "+str(cnt))

