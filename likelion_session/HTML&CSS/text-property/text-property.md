# 텍스트와 관련된 프로퍼티

-   font-family

    -   폰트명에 띄어쓰기가 있으면 따옴표로 묶기. 한 단어면 그냥 작성해도됨
    -   컴퓨터 내에 내장되어 있지 않을 수 있음 -> 여러개 작성하여 앞에서부터 없으면 넘어가는 방식..
    -   web font - google font이용
    -   [font 적용법](https://github.com/Parkjju/TIL/blob/master/CSS/css_additional/CSS_additional.md)

-   font-style

    -   normal - 일반값
    -   italic - 이탤릭체
    -   oblique - 글자 기울이기
    -   font에 따라 italic체가 디자인 되어 있어야 적용됨

-   font-weight

    -   폰트의 굵기를 지정

-   font 프로퍼티 하나만으로도 동시에 적용 가능
    -   `font : oblique 900 35px 'Noto Sans KR', sans-serif;`

### 텍스트 정렬

-   text-align - 텍스트 좌,우,중앙정렬

    -   텍스트의 정렬은 **자기 자신을 기준으로 정렬이 이루어진다**

-   line-height : 문장 사이 간격을 조정

    -   해당 요소의 폰트사이즈를 기준으로
    -   font-size의 value만큼 곱한 크기
    -   `font-size:10px;`, `line-height:2;` -> 20px만큼 문장 하단에서 하단 길이만큼 확보? No
    -   line간의 높이가 아니라, **line의 높이임** -> line은 해당 text요소의 line을 말하는 것

-   letter-spacing

    -   글자와 글자 사이의 간격을 조정 -> 자간

-   text-indent
    -   들여쓰기. `text-index: 15px;`
