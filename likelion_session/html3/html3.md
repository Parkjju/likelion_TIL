# html 3

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>안녕하세용</title>
    </head>
    <body>
        <h1>박경준을 소개합니다</h1>
        <h2>박경준을 소개해요</h2>

        <form action="전송받을 대상">
            아이디 : <input type="text" name="id" /> 비밀번호 :
            <input type="password" name="pw" />
            <input type="submit" />
        </form>
    </body>
</html>
```

-   form 태그 내에서 input태그를 통해 여러가지 정보를 주고받는데, **URL로써 주고받는다**
-   input내에서 name 지정을 통해 어떠한 데이터를 주고 받는 지에 대해 알린다.

```text
http://127.0.0.1:5500/likelion_session/html3/%EC%A0%84%EC%86%A1%EB%B0%9B%EC%9D%84%20%EB%8C%80%EC%83%81?id=%E3%85%94%E3%85%81%EA%B0%80&pw=arka
```

-   id=.... pw=.... , input 내에서 지정한 name 옵션으로 정보를 전달하는 것을 확인

```text
ol>li*3
ul>li*4
```

-   리스트 생성 단축키
