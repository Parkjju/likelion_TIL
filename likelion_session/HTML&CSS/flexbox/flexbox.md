# flexbox

-   정렬에 대해 특별한 지정 없이도 편리하게 레이아웃을 구성하게 해주는 프로퍼티

-   flex container에 `display: flex;`추가해야 flexbox사용가능
-   flex item(자식 요소)

-   가로 또는 세로 기준으로 자식 요소들을 정렬

-   flex container에 이용하는 속성
    -   flex-direction: flex 컨테이너 안의 item들의 방향설정
        1. `flex-direction: row;` : 좌->우
        2. `flex-direction: row-reverse;` : 우 -> 좌
        3. `flex-direction: column;`: 상->하
        4. `flex-direction: column-reverse;`: 하->상
    -   flex-wrap: item들이 container를 벗어날 경우에 대한 옵션
        1. `flex-wrap: nowrap;` : item이 container를 벗어나도 그대로 둠
        2. `flex-wrap: wrap;` : item들이 container를 벗어나면 container내의 다음 줄로 옮겨줌
        3. item이 container를 벗어나는 것은 container내에서 item들의 정렬 방식에 있어서 발생할 수 있다는 것을 알아두자
    -   justify-content : flex-direction으로 정해진 방향을 기준으로 수평으로 item들을 정렬하는 옵션을 고름
        -   **수평방향** -> row 또는 column 진행방향을 축으로, 평행한 방향
        -   **수직방향** -> row 또는 column 진행방향을 축으로, 수직의 방향
        1. `justify-content: flex-start;` - 기본값(진행방향 시작점 기준 정렬)
        2. `justify-content: center;` - 중앙정렬
        3. `justify-content: flex-end;` - 진행방향 끝 정렬
        4. `justify-content: space-around;`
        5. `justify-content: space-between;`
    -   align-items : flex-direction으로 정해진 방향을 기준으로 **수직방향 정렬**
        1. `align-items: stretch;` - 기본값
        2. `align-items: flex-start;` - 첫 시작점
        3. `align-items: flex-end;` - 끝점
        4. `align-items: center;` - 수직방향 중앙정렬
        5. `align-items: baseline;` - 글꼴을 기준
    -   align-content : flex-direction으로 정해진 방향을 기준으로 **수직방향으로 여러 줄인 item들을 정렬하는 옵션** - column1, column2, column3 ....
        1. align-content: space-between .. align-items와 동일

*   flex item
    1. flex-grow: flex 아이템의 확장과 관련된 속성
        - 기본 0
        - 단위없는 숫자값 사용
        - flex container에 대하여 숫자 비율만큼 item 크기를 조절
        - 여백에 대한 계산.
    2. flex-shrink: flex아이템 축소와 관련됨
        - 기본 1
        - flex container크기에 따라 flex item의 크기를 조정
    3. flex-basis: flex 아이템의 기본 크기 결정
        - 기본 auto
        - 단위 필수
    4. flex: flex-grow, flex-shrink, flex-basis의 축약형
*   [justify-content정리](https://www.youtube.com/watch?v=b3xhm_2esTM)

    -   space-around vs space-between
        -   space-between은 container끝단에 아이템을 배치한 후 그 사이의 공간을 등분하여 배치
        -   space-around는 space-between으로 계산된 flex item 사이의 공간의 절반을 flex container의 시작점 & 끝점에 미리 할당 후 space-between처럼 배치

*   [align-items정리](https://www.youtube.com/watch?v=b3xhm_2esTM)
    -   align-items: baseline -> **the baseline value for flex items will align flex items along their contents baseline.**
    *   컨텐츠 아이템 내에서 글자가 sit되는 라인을 baseline이라고 하는데, `align-item: baseline;`을 주게되면 이 라인들을 한줄로 이어서 flex item들의 정렬기준으로 만들어준다
