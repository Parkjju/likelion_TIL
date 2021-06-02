# CRUD

- database에 대한 Create, Read, Update, Delete

- template생성, views.py, urls.py수정

- views.py에는 models.py에 정의했던 앱 클래스를 import한 뒤 데이터를 가져와야함 - app.**objects.all()**

```python
from .models import Appclass
def home(request):
    apps = Appclass.objects.all()
    return render(request,'home.html')
```

## Read

- 템플릿 언어를 통해 템플릿에서 (admin에서 작성했었던 테이블들) 객체를 표기
- views.py에서 .objects.all()로 객체를 반환받는중 - 객체 내의 컬럼들을 받고싶다면 콤마를 통해 접근
- 내용에 대한 요약이 필요한 경우 models.py에 슬라이싱 연산을 통해 적당한 수의 데이터만 받기

```python
def summary(self):
    return self.instance_var[:10]
```

- Path-converter
  - 원래는 테이블에 대해 각 id마다 페이지를(디테일 페이지) 생성해주어야 하지만, path-converter를 통해 id값을 이용하여 단순작업 간소화 (views.py)

```python
from django.shortcuts import get_object_or_404
# 없는 객체를 요청받을 경우 HTTP상태코드 404를 표시
def detail(request,id):
    blog = get_object_or_404(table_class, pk = id)
# pk 는 테이블의 각 row를 구분해주는 식별자
```

- views.py에 detail페이지에 대한 함수를 정의했으면 urls.py로 넘어가 path converter를 이용

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home" ),
    path('<str:id>', detail, name="detail"),
]
```

- paramter 1 : 서버에서 페이지로의 이동을 할 때 슬래시를 통해 터미널 경로처럼 이동하는데, 해당 이름을 id로 지정한다는 것 (id값에 따라 페이지가 다르게 보임 + **views.py의 매개변수로 들어감**)
- parameter 2 : views.py에서 정의한 함수 이름
- parameter 3 : name

## Create

- new함수 : new.html을 보여줌
- create함수 : 데이터베이스에 저장

* GET vs POST

  - GET : 데이터를 얻기 위한 요청 - 데이터가 url에 보임
  - POST : 데이터 생성을 위한 요청 - 데이터가 url에 안보임 & csrf공격 방지 - form action="method"태그 안에 `{%csrf_token%}`추가

* 실습 흐름 정리
  1. views.py에 두 함수를 정의. - 게시글을 작성하는 페이지 render할 함수 + 실제 기능을 할 함수(create함수)
  2. create함수는 게시글 작성 페이지에서 넘어오는 데이터를 받아야함. (POST 방식으로 받는다. ) `request.POST['instance_var']`
     - 날짜를 받고싶다면 `from django.utils import timezone` 추가 후 `date = timezone.now()`로 받는다.
     - 변수 저장 및 렌더링 페이지로 넘겨주는 방식을 객체지향을 기반으로 !!
  3. 데이터 모두 저장후 `objName.save()`메소드 호출하여 저장
  4. 저장한 객체를 다시 페이지에 넘겨줘야함 (render가 아닌 redirect함수를 통해) `return redirect('pageName', obj.id)`
     - redirect 이용 전 **django.shortcuts의 redirect import해야함**

## update
* edit & update함수 적용 - edit에서 수정할 데이터의 id값을 받아와야함 (path converter이용)


## delete
