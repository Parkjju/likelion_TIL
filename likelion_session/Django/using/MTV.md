# MTV 패턴 이해하기

-   개발은 혼자 하지 않는다 + 보안 + 개발자는 반드시 실수를 한다 -> 해당 문제점들을 방지하기 위해 MTV패턴을 이용

    -   Front end - Back End의 구분으로 작업 + 프레임워크를 이용하면 동시적으로 개발할 수 있어 훨씬 효율적
    -   장고는 이를 세 파트로 나누어 진행
    -   MTV - Model & Template & View (T -> Front end, MV -> Back end)

-   Template

    -   사용자가 보이는 영역
    -   HTML
    -   CSS
    -   템플릿 언어
    -   JS를 통해 인터랙티브하게 디자인까지..

-   Model

    -   DataBase(DB)
    -   데이터가 저장되는 곳 - 사용자 계정 & 광고 & 게시물 등

-   View

    -   데이터를 처리하는 곳
    -   MTV중 핵심
    -   사용자로부터 요청을 받고 받은 요청을 위해 모델에서 가져온 데이터를 가공 -> 템플릿에게 넘겨줌

-   당근마켓 예시
    -   검색창에 당근을 입력 -> 템플릿에 표시됨
    -   엔터쳐서 요청 -> View로 당근이라는 데이터가 넘어가 처리됨.
    -   View가 model로부터 당근이라는 이름을 가진 게시물을 검색 후 다시 view로 가져옴
    -   이후 템플릿에게 넘겨 화면상에 표시