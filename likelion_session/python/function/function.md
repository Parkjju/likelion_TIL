# 함수

-   함수란? 코드를 기능으로 묶은 단위

```python
def function_name(parameter):
    print(parameter)
    return parameter+1
```

-   함수의 존재 목적에 대한 이해! -> Bigger problem -> smaller program => 유지보수

    -   Divide & Conquer

-   인자 -> def function(**x,y**):

-   리턴값 -> def function(x,y): **return x+y**

    -   하나만 존재해야함
    -   없을 수는 있음. (기능에따라..)

-   변수의 범위
    -   지역 vs 전역변수
    -   지역변수 : 함수 안에서만 영향력을 가짐
    -   전역변수 : 코드 전체 영역에서 영향력을 갖는 함수 -> global num - global 키워드를 사용
    -   전역변수는 지양!
    -   함수의 정의는 **코드를 기능별로 정리**하기 위함. 전역변수의 주된 사용은 함수의 존재 목적을 해침
