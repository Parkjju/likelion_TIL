# 제어문(2) - 반복문

-   for, while

```python
lst = [1,2,3]
for a in lst:
    print(a)
```

-   a -> 반복제어변수
-   lst -> 반복대상 -> 리스트, 튜플, 문자열 등
-   print("A") -> 반복대상 코드

-   range함수 - range(x,y) -> x부터 y-1까지 리스트로 반환, range(x) -> 0부터 x-1까지 리스트로 반환

-   while문 -> 조건을 만족하는 동안 코드의 수행을 명령

    -   `while condition: print("A")`
    -   `while True: print("무한루프")`

-   반복문을 중지 -> break
    -   예외처리
    -   무한루프 탈출
