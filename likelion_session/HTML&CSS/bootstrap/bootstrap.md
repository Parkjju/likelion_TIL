# 부트스트랩 소개

-   간편하게 웹을 생성할 수 있게 해줌.
-   오픈소스 프론트엔드 프레임워크
-   [bootstrap](https://getbootstrap.com/)
-   클래스 이름의 변경으로 요소들을 쉽게 바꿀 수 있다.

### 그리드 시스템

-   부트스트랩을 통해 그리드를 쉽게 구현할 수 있게 해줌
-   container와 row가 필요함
-   col-1 : 12개로 나눈것 중 1개의 너비

```html
<div class="container">
    <div class="row">
        <div class="col">col</div>
        <div class="col">col</div>
        <div class="col">col</div>
        <div class="col">col</div>
    </div>
    <div class="row">
        <div class="col-8">col-8</div>
        <div class="col-4">col-4</div>
    </div>
</div>
```

-   부트스트랩은 **반응형 웹을 지원해줌**
-   grid option
-   .col-lg-4
    -   lg : 반응형 웹 기준이 되는 화면의 사이즈 (예제에서 sm, md, lg기준에 해당하는 화면사이즈가 될때 각 클래스 스타일에 맞게 적용됨)
    -   12등분 중 차지할 비율
