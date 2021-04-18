# form 태그

### form 태그란?

-   웹 브라우저 상에서 데이터를 입력 -> 서버에 전달 -> 결과를 다시 웹 브라우저에 반환
-   다양한 입력 폼 양식 -> form 태그 이용

### form 구성

1. action : 데이터를 보낼 URL을 지정 (해당 데이터를 처리할 웹 서버 URL)
2. method : 보내는 방식을 지정
    - method = "get"
    - method = "post"

-   **method GET & POST**

    -   기능 - form에 입력한 데이터를 서버로 보내는 것은 동일
    -   보내는 방식에서 차이

-   서버로 데이터를 보낼때 HTTP Request message로 보냄.

    -   [HTTP 메시지란?](https://developer.mozilla.org/ko/docs/Web/HTTP/Messages)
    -   ASCII로 인코딩된 텍스트 정보
    -   개발자가 직접 HTTP 메세지 작성 X -> 소프트웨어, 브라우저, 프록시, 웹 서버가 처리
    -   **프록시란?** - 클라이언트가 자신을 통해 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 컴퓨터 시스템이나 응용 프로그램

-   HTTP 메세지는 Header와 Body로 구분되며 **Header에 목적지 URL이 포함됨**

1. GET 방식

    - form에 입력한 데이터를 URL끝에 붙여 보이도록 서버에 전달.
    - 데이터를 URL 끝에 붙여 눈에 보이게 보냄.

2. POST 방식
    - GET과 다르게 폼에 입력된 데이터를 HTTP메세지의 Body부분에 숨겨서 보냄.
    - 데이터를 URL에 적지 않고 내부에 숨겨서 보냄.

-   구분하여 쓰는 이유
    -   GET - **데이터 조회 만을 목적**으로 할 때 주로 쓰임
        -   예) 검색창
    -   POST - 서버에 있는 데이터를 쓰거나 수정,삭제 할 때 주로 사용
        -   예) 게시물 작성 및 수정

```text
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%95%98%EC%9C%84
```

-   하위라고 검색하자 query="" 변경됨

### input

-   사용자에게 입력을 받기 위해 사용되는 빈 태그
-   input type="text" name="id"
    -   type속성에 의해 타입 결정
    -   name속성을 통해 서버로 데이터를 전송할 때 입력받은 데이터를 구분하기 위해 **name속성을 key로, 입력받은 데이터를 값으로 전달**

*   form - input태그에 데이터 입력 후 제출

```text
http://127.0.0.1:5500/likelion_session/HTML&CSS/form/my-app?id=%EA%B2%BD%EC%A4%80
http://127.0.0.1:5500/likelion_session/HTML&CSS/form/my-app?id_ibbneeda=snow
```

-   id속성 지정한 대로 나타남

-   placeholder -> 아무것도 입력하지 않았을 때 노출되는 텍스트
-   value="경준" -> **실제로 할당되는 값. 초기값으로 이용 가능**

### label 태그 - 태그가 어떤 일을 하는 지에 대한 표시

```html
<label for="userpassword">비밀번호:</label>
<input type="password" id="userpassword" />
```

### div태그

-   태그들을 구분짓기 위한 태그 division

### select

-   선택박스 만들기 - 여러개의 선택지를 제시

```html
<select>
    <option>opt1</option>
    <option>opt2</option>
</select>
```

-   **select태그에 name속성 필수**
    -   input태그의 name속성과 동일하게 작동
-   **option태그에 value속성 필수**
    -   select태그의 name속성과 대응하도록 만들기

### textarea

-   한 번에 많은 글을 입력 받을 때 사용
-   빈 태그 아님 - 텍스트 입력 시에 form태그의 value속성처럼 작동함 (초기값 할당)

### button

-   input type button과 유사하지만, button태그는 빈 태그가 아니므로 html요소를 넣을 수 있음

```html
<button>
    <img src="#" />
</button>
```

```text
http://127.0.0.1:5500/likelion_session/HTML&CSS/form/my-app?id_ibbneeda=snow&password=fef&gender=male&job=student&introduce=efef
```

-   입력한 모든 데이터가 URL상에 노출되어있음을 확인 (GET방식)
