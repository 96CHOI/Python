city = ("서울","대전","대구","광주","부산","울산","세종")
age = ("신생아","초등학생","중학생","고등학생","대학생","노년층")
# 각 도시의 신생사, 초등학생, 중학생, 고등학생, 대학생, 노년층의 인구수를 입력하시오
# 딕셔너리에 저장하시오
# 어떤것이 키이고 어떤것이 calue로 들어가야할지 생각해보기
""" 방법 1
info = []
for i in city:
        data = []
        for x in age:
            data.append(input(i + "의 " + x + " : "))
        info.append(data)
dic = dict()
for i in range(len(city)):
    dic[city[i]]=dict( zip(age, info[i]))

for i in dic:
    print("{0} : {1}".format(i, dic[i]))
"""

population=dict()
for cname in city:
    temp=dict()
    print("===={0} 지역 인구수 ====".format(cname))
    for k in kind:
        i=random.randint(1000,30000)
        print("{0}:{1}명".format(k,i))
        temp[k]=i# 신생아, 초등학생, 중학생... 인구수를 딕셔너리에 저장
        #키 - 아가, 초딩, 중딩...,value -인구수
    population[cname]=temp # 위에서 만들어진 딕셔너리를 value로, 도시이름은 key

for k in population:
    print("{0}:{1}".format(k,population[k]))

