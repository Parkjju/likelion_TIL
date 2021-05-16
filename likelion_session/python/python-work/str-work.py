# 문자열 (내장함수)

# 덧셈
str1 = "멋사"
str2 = "는 멋진 동아리입니다"

print(str1+str2)

# 곱셈
print(str1*3)

# 인덱싱
print(str1[0])

# 슬라이싱
# str[x:y] == str문자열의 x번째부터 y-1번째까지
print(str1[0:3])


# 파이썬 문자열 내장함수
# 1. len() - 문자열 길이 반환
print(len(str1))

# 2. str.count("문자") - str내에 특정 문자가 몇번 등장하는지 계산하여 횟수 반환
str3 = "멋멋쟁이사자"
print(str3.count("멋"))

# 3. 문자열을 기준에 따라 나누기 : str.split()
# default => 공백
str4 = "멋 쟁이 사 자 처 럼입니다"
print("split 함수입니다 : ", str4.split())

# 4. 문자열 내 특정 문자의 인덱스 찾기 - str.find("문자")
str5 = "멋쟁이사자처럼"
print("find함수 : ", str5.find("자"))
print("find함수 - 해당 문자 없을떄?", str5.find("A"))
