# CSS 기초

### CSS란? - Cascading Style Sheets

-   예시)

```css
p {
    font-family: "font";
    font-size: 18px;
    color: black;
}
```

-   p -> 선택자(Selector) : 스타일을 적용하고자 하는 HTML 요소를 선택하는 역할
-   color, font-size - 속성(Property) : 지정할 스타일의 속성명에 해당함.
    -   `property : value;` 가 한 단위
    -   세미콜론(;) 이용하여 각 속성 구분
-   black, 18px .. - 값(Value) : 키워드나 특정 단위를 이용하여 원하는 스타일을 적용함. 프로퍼티와 쌍을 이룸

-   CSS - 선택자, 속성, 값으로 이루어짐
-   선택자 뒤의 중괄호로 묶인 블록을 **선언 블록이라고 함**
-   속성과 값을 한 쌍으로 **선언(Declaration)**이라고 함.

### HTML에 CSS를 적용하는 방법

1. Link style
    - HTML 외부에 있는 CSS파일을 불러옴.
    - head 태그 내부에 link 태그로 불러옴
    - `<link rel="stylesheet" href="CSS 경로 및 파일.css" />`
2. Embedding style
    - HTML의 head태그에 style태그 이용하여 직접 CSS 작성
3. Inline style
    - HTML 요소에 직접 stlye 속성을 이용하여 CSS 작성
    - `<h1 style="color: red;">,,,</h1>`
    - 적용할 HTML요소 하나에만 스타일을 적용하기 때문에 동일한 HTML 요소이더라도 적용이 안됨.
