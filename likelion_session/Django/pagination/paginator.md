# Paginator

- 블로그 객체를 잘라서 보내주는 기능을 수행
- paginator 기능을 적용할 앱 디렉토리의 views.py에 paginator객체를 생성해준다.

```python
# blog/views.py
# import 먼저
from django.core.paginator import Paginator

# import ...
def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,3)
    page= request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs})

```

- 쪼갤 페이지 숫자와 함께 모든 정보를 담았던 객체를 파라미터로 전달한다. `paginator = Paginator(blogs,3)`
- request.GET.get 메소드를 사용한 이유 -> 실제 GET방식의 호출이 전달되지 않더라도 정보가 넘어가게끔 하기위해
- paginator 객체에 GET.get으로 받은 페이지 정보를 생성된 paginator 객체의 get_page메소드의 파라미터로 전달한 뒤 렌더링할 html파일에 객체로 저장하여 전달한다.

- html파일 내에서는 객체가 paginator된 상태이므로 형식에 맞게 구조를 짜야한다. -> if조건문 템플릿 문법 활용

```html
{% if blogs.has_previous %}
<a href="?page=1">처음</a>
<a href="?page={{blogs.previous_page_number}}">이전</a>
{% endif %}
<span>{{blogs.number}}</span>
<span>of</span>
<span>{{blogs.paginator.num_pages}}</span>
{% if blogs.has_next %}
<a href="?page={{blogs.next_page_number}}">다음</a>
<a href="?page={{blogs.paginator.num_pages}}">마지막</a>
```

1. a태그의 href에 **?page=number** 형식을 이용하여 페이지네이팅 한 부분을 지정한다.
2. paginator 객체에 접근하는 템플릿 메소드를 이용하여 링크를 구성한다
   - `object.previous_page_number` -> paginator 객체의 현재 페이지의 이전페이지
   - `objects.next_page_number` -> paginator 객체의 다음 페이지
   - `objects.paginator.num_pages` -> paginator 객체의 분할 수 (끝페이지로 바로 이동할때 이용)
