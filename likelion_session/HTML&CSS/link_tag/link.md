# 링크태그

-   a태그의 필수적인 속성(Attribute) -> 링크주소(키), 실제주소(값)

```html
<a href="URL"></a>
```

-   href = hypertext reference

### 경로(path)

-   주소 + 경로 = URL (uniform Resource Locator)
    -   인터넷에서 HTML페이지, CSS문서, 이미지 등 자원(Resource)의 위치를 나타냄
-   절대 URL(Absoulute URL) - 접근하는 최초 시작점부터 경유한 경로를 모두 기록. 리소스의 위치 나타냄
-   상대 URL(Relative URL) - 기준점을 기준으로 상대적인 경로 기록

-   https://myblog.com/

    -   main.html
    -   about
        -   myface.jpg

-   myface의 경로?
-   위의 예시에서 절대 URL -> https://myblog.com/about/myface.jpg
-   상대 URL -> about/myface.jpg

### target속성

-   클릭으로 링크를 열때 어디에 오픈 할 것인지 정하는 속성
-   target = "\_self" -> 현재 탭에서 링크 열기
-   target = "\_blank" -> 새 탭에서 링크 열기
