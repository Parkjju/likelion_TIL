# 상속

-   부모요소의 프로퍼티를 자식 요소가 자동으로 물려받아 스타일을 적용
-   모든 프로퍼티가 상속되는 것은 아님.
-   [w3.org - full property table](https://www.w3.org/TR/CSS21/propidx.html)

-   상속되지 않는 프로퍼티에 대해서 `margin: inherit;`옵션을 지정하면 상속됨.

### 우선순위

-   CSS 적용 순서
    1. 중요도
        1. head 태그 내의 style태그
        2. head 태그 내의 style태그 내의 import
        3. link태그로 연결된 CSS
        4. link태그로 연결된 CSS 내의 import
        5. 브라우저 디폴트 스타일시트
    2. 명시도
        1. !important - 최우선 적용
        2. 인라인 스타일
        3. 아이디
        4. 클래스, 속성, pseudo selector
        5. type selector
        6. universal selector
        7. inherit
    3. 선언 순서
        - Cascading 속성에 대한 이해!!
