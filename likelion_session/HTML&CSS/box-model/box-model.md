# 박스모델

-   HTML의 모든 요소는 박스의 형태로 이루어진다.
-   브라우저에 출력되는 형태가 박스형태.
-   브라우저에 올바르게 배치하기 위해 박스에 대한 이해가 필요!!

### 구성요소

1. 내용 (Content) - 실제 내용을 담고 있음
2. 경계선(Border) - 내용을 감싸는 경계
3. 패딩(Padding) - 내용과 경계선 사이의 공간
4. 마진(Margin) - 경계선 밖의 공간.

-   content
    -   내용이 박스의 크기를 넘어서는 것에 주의
    -   `overflow: hidden;`, overflow 프로퍼티 이용하면 박스를 넘어선 컨텐츠에 대해 작업가능
-   border
    -   `border-solid: dashed solid dotted double;` - 적용하는 값 개수에 따라서 다르게 적용됨(깃에 정리해놓은 내용 참조)
    -   `border: style size color`
    -   `border-radius: 15px;` -> 경게를 둥굴게 (모서리 반지름길이)
    -   `border-top-left-radius:30px 10px`-> 왼쪽상단 모서리를 타원형으로 ..
    -   `border-bottom-left-radius` - 왼쪽 하단 모서리 지정

*   padding&margin

    -   상하좌우 따로 또는 한번에 지정 가능
    -   둘은 유사하지만 위아래로 박스 요소를 배치할 때에 **마진병합 이슈가 발생함**
    -   큰쪽 마진을 따라간다(상단 박스 마진:10px, 하단 박스 마진:20px -> 마진은 30px가 아닌 20px로 됨)

*   box-sizing
    -   박스 내의 컨텐츠 크기를 조정하기 편하게 해줌(width)
    -   `box-sizing: content-box;` -> 컨텐츠 박스의 크기를 기준
    -   `box-sizing: border-box;` -> 컨텐츠width + border두께
    -   child container가 parent container의 크기를 넘어서게 되는 경우를 방지할 때 이용
        > border-box는 테두리와 안쪽 여백의 크기도 요소의 크기로 고려합니다. 너비를 100 픽셀로 설정하고 테두리와 안쪽 여백을 추가하면, 콘텐츠 영역이 줄어들어 총 너비 100 픽셀을 유지합니다. 대부분의 경우 이 편이 크기를 조절할 때 쉽습니다.
