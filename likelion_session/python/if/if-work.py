# 제어문 - 문기문
# if(조건)
# 들여쓰기 주의
score = int(input("점수를 입력하세요: "))
if score>=85:
    print("PASS")
else:
    print("FAIL")

activity = input("동아리 명을 입력하세요: ")
if activity == "멋사":
    print("나두")
else:
    print("FAIL")

# 5000이상 : 아웃백 / 3000이상 : 학식 / 1000이상 : 컵라면 / 나머지 : 공기밥
money = int(input("잔액을 입력하세요: "))

if money >= 5000:
    print("아웃백")
elif money>=3000:
    print("학식")
elif money >= 1000:
    print("컵라면")
else:
    print("공기밥 가즈아ㅏㅏ") 