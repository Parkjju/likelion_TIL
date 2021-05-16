# 딕셔너리 (내장함수)

gyeongjun = {"이름": "박경준", "나이": 24, "안경": "씀"}

# key-value쌍 추가법

# dict[new_key] = value
gyeongjun["음악"]="좋아함"

print(gyeongjun)

# 특정 key-value쌍 삭제법 : del함수
del gyeongjun["음악"]
print("삭제 후 경준 딕셔너리 : ", gyeongjun)

# key로 value 얻기
print("경준 딕셔너리의 이름 값: ", gyeongjun.get("이름"))