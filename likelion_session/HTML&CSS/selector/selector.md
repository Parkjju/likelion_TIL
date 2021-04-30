# 선택자

### 선택자 기초

-   스타일을 적용하고자 하는 HTML을 선택하는 역할

-   여러 개의 선택자를 콤마(,)를 통해 여러 요소 동시에 선택 가능.

```css
h1 {
    color: red;
}
p {
    color: red;
}
```

```css
h1,
p {
    color: red;
}
```

-   단순 선택자
    -   타입(Type)
    -   클래스 (Class)
    -   아이디 (id)
    -   전체 (Universal)
    -   속성(Attribute)

1. 타입 선택자 : 해당 태그를 가지는 **모든** 요소에 스타일을 적용
    - `p { color: red; }`
2. 아이디 선택자 : id로 스타일을 적용함. 해당 id 하나에 적용 (id는 **unique해야함!!!**)
    - id attribute : HTML 문서 내에서 동일한 아이디 X , 다른 요소와 구분되는 점을 만들어준다
    - `<h2 id="jun">hy</h2>`
    - CSS에서 호출 시 #이용
3. 클래스 선택자 : 클래스 이름으로 스타일을 적용, 같은 클래스 이름이면 모두 적용
    - html attribute로써, 비슷한 요소들을 묶어주는 역할
    - . 이용하여 css에서 호출
4. 전체 선택자 : **모든 요소**에 스타일을 적용. -> 모든 요소에 적용하기 때문에 속도 저하 가능성이 존재.
    - `*{ color: red; }`
5. 속성 선택자 : 특정 속성을 소유하는 모든 요소에 스타일을 적용
    - `selector[attribute = "value"]{ property: value; }`

-   복합 선택자
    -   부모-자식요소 관계로 이루어진 HTML요소들이 있다고 가정

```html
<span>
    <h1></h1>
    <p>
        <h2></h2>
    </p>
</span>
```

-   span은 부모, h1,p는 span의 자식요소, h1,p,h2는 span의 후손(Descendant)

-   자식 선택자 (Child selector)

    -   선택자 A의 모든 자식 요소중 선택자 B와 일치하는 모든 요소를 선택
    -   `span > h1 { color: red; }`

-   후손 선택자

    -   선택자 A의 모든 **후손** 중 선택자 B와 일치하는 요소를 선택 (자식과 후손 개념 헷갈리지 않기)
    -   `span p { color: blue;}`
    -   띄어쓰기로 구분

-   pseudo 클래스 : 요소의 특별한 상태를 지정할 때 사용
    -   `selector:pseudo-class{ prop: value;}`
    -   link - 방문하지 않은 링크 상태
    -   hover - 마우스를 올려놓은 상태
    -   visited - 방문한 상태
    -   위와같은 상태들을 슈도 클래스를 통해 지정하여 스타일을 적용할 수 있다
