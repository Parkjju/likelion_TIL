# 위치와 관련된 프로퍼티

-   HTML요소 - block or inline요소로 나눌 수 있음
    -   block -> 너비 지정 없어도 width="100%"가 default값 (width, height, margin, padding 모두 지정 가능)
    -   inline -> 새로운 줄에서 시작하지 않고, content 크기만큼 너비를 가짐 (width, height, margin-top, margin-bottom 지정 불가)

*   display프로퍼티

    -   block
    -   inline
    -   inline-block - inline에서 지정 불가능했던 속성들을 지정할 수 있게해줌
    -   none - 브라우저에 해당 요소를 출력하지 않게해줌.

*   position 프로퍼티

    -   static : 기본값
    -   relative : 기본 위치를 기준으로 좌표값 사용
        -   기본 위치 기준? - position: static기준.
    -   absolute : 부모나 조상중 relative, absolute, fixed가 선언된 곳을 기준으로 적용
    -   fixed - 보이는 화면 기준으로 좌표 프로퍼티를 통해 고정

*   z-index
