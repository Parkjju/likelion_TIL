# 리스트 (내장함수)

li = [1,2,"박경준", 4,"입니다", 51]
num_list = [1,5,3,4,7]
# 인덱싱 & 슬라이싱
print(li[1])
print(li[0:2])

# 리스트 길이를 반환 : len()
print("리스트의 길이 : ", len(li))

# 리스트 원소를 오름차순으로 정렬 : 변수.sort()
# sort함수는 리스트를 반환하지 않으므로, print를 해도 아무것도 출력하지 않는다
print("정렬 전: ", num_list)
num_list.sort()
print("정렬 후: ", num_list)

# 리스트 내의 특정 원소 인덱스를 반환 : lst.index()
print("박경준 위치 : ", li.index("박경준"))

# 리스트 내 특정 원소 등장횟수 : lst.count()
print("박경준 등장 횟수 : ", li.count("박경준"))