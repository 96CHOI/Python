
# 미니 시험
# 문제. (문제는 하나)
# 문제를 모두 다 풀면 소정의 관심 나갑니다.
# 

# (c:/test 폴더에 txt 문서에 다음과 같은형태로 데이터 20개 작성하기 
# 번호 이름 연락처 이메일 성별 주소(동, 읍, 면까지만 입력)

# 위 txt 파일을 읽어오기
# 딕셔너리에 저장하기 (키, value 알아서)
# 1. 이메일의 도메인 몇개이고 무엇무엇있는지 출력하기 (중복없이) - 도메인은 naver.com, google.com 요런거
# 2. naver.com 도메인의 이메일을 사용하는 사람들이 사는 도시이름 만 출력하기
# 3. 성별이 여자인 사람중에서 대전 중구에 사는 사람은 누구인가? 모두출력

# 함수
# - 파일읽기 함수
# - 파일읽어서 딕셔너리에 저장하는 함수
# - 1. 함수 - 이메일에서 도메인 분리하는 함수, 중복제거하고 출력하는 함수
# - 2. naver.com인 사람 찾는 함수
# - 3. 성별로 찾는 함수 (꼭 여자만 찾을수 있으면 안됨, 남자를 찾고싶으면 찾기 되야한다. , 코드 수정없이)
def qwe(qus):
    # 이메일 뭐뭐있는지
    for i in qus:
        print(qus[i]["이메일"].split("@")[1])
    for x in qus:
        if (qus[x]["이메일"].split("@")[1] == "naver.com"):
            print(qus[x]["이름"] + qus[x]["이메일"])
    # 성별
    search = input("성별을 입력하세요 : ")
    for a in qus:
        for search in qus[a]["성별"]:
            if search == "여":
                print(qus[a]["이름"] + qus[a]["성별"] + qus[a]["여"])
            else:
                print(qus[a]["이름"] + qus[a]["성별"] + qus[a]["남"])
def save(file):
    key = ['번호','이름','연락처','이메일','성별','주소']
    qus = dict()
    for i in range(len(file)):
        qus[i+1] = dict(zip(key, file[i]))
    qwe(qus)
def read():
    file = []
    with open("c:/test/name.txt", "r", encoding="utf-8") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i][:len(file[i])-1]
        file[i] = file[i].split(" ")
    save(file)

read()

        

