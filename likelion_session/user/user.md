# User 확장과 인증

## 이론

- 서비스 이용자 각각이 서비스에 진입하자마자 보이는 폼이 다름.
- 각 서비스 이용자마다 가지고있는 모델 (데이터테이블)이 다름

- django에서는 유저 데이터 저장을 위한 모델을 이미 제공하고 있다.

  - myvenv > Lib > django > contrib > auth > models.py > class User
  - 하지만, 장고에서 제공하는 유저 데이터에 대한 컬럼이 부족한 경우가 대다수 (서비스 특성에 따라 저장할 유저의 정보가 다양함)
  - User클래스의 부모클래스인 AbstractUser에서 정의중인 컬럼들을 확인할 수 있음. (이들을 포함하면서 서비스 특성에 따라 개발자가 추가적으로 컬럼들을 정의하면 됨)

- User 데이터에 대한 인증 -> Authentication기능을 장고에서 제공

  - authenticate, login, logout함수를 통해 유저 관리 (토큰 발행은 장고에서 자체적으로 제공)

- authenticate : 유저 아이디와 패스워드를 가진 데이터 테이블이 User테이블에 존재하는지 확인
- login : 유저 테이블에서 온 데이터를 통해 유저가 인증된 상태로 유지할 수 있게해주는 함수 -> request에 user정보가 포함되어 넘어가게됨
- logout : 인증된 상태를 풀어달라고 서버에 요청

## 실습 1

1. 로그인 관련 기능을 담당할 app만들기 - `python manage.py account` + settings.py에 등록
2. model의 확장은 실습1에서 다루지 않음.
3. views.py 코드 추가 - `from django.contrib.auth.forms import AuthenticationForm, UserCreationForm`

```python
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
```

4. urls.py 생성 (Account app 내에)

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view, name="login"),
]
```

5. project폴더의 urls.py에 등록

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home" ),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')), # new code
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

6.  base.html수정 및 login.html생성

```html
{% extends 'base.html' %} {% block content %}
<h1>Login</h1>
<form action="" method="post">
  {%csrf_token%} {{form.as_p}}
  <button type="submit">submit</button>
</form>
{% endblock %}
```

7. login.html의 action
   - account app의 views.py - login함수를 구현함에 있어서 `if request.method == 'POST':`와 같은 조건문을 통해 데이터베이스에 접근할 때는 POST 방식으로, 또 다른 경우에는 GET방식으로 로직을 다르게 한 함수에서 처리할 수 있음.

- 만들어진 login_view함수 - auth에서 가져오는 login함수와 이름이 겹치지 않게 조심

```python
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(reuqest=request, data = request.POST) # 데이터 요청받음
        if form.is_valid(): # 유효성검사
            username = form.cleaned_data.get("username") # cleaned -> 문제없는 데이터
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password) # user에 저장
            if user is not None:
                login(request, user)
            return redirect("home")

    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("home")
```

- logout_view함수도 account app의 url에 등록

* **로그인 여부 확인하기**

```html
{% if user.is_authenticated %} {{user.username}} {% endif %}
```

## 실습2 - User 확장과 인증

- 회원 인증

```python
# account/views.py
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})

# account/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="signup"), # new
]
```

- 회원 데이터 확장하기
- account app의 models.py에 AbstractUser상속받아서 유저 테이블 생성

```python
# account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
```

- project폴더의 settings.py에 내가 만든 CustomUser라는 유저 데이터테이블 모델을 이용하겠다고 등록해야함.

```python
# settings.py
AUTH_USER_MODEL = 'account.CustomUser' # add
```

- 추가 후 `python manage.py makemigrations`

* `python manage.py migrate`는 오류가 발생
* django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency account.0001_initial on database 'default'.

* -> admin 관련해서 오류가 발생함을 확인. -> settings.py의 INSTALLED_APPS의 `django.contrib.admin`을 주석처리

  - 프로젝트 폴더의 urls.py의 admin path를 주석처리
  - 주석처리 후 오류 해결됨 (Running migrations: Applying account.0001_initial... OK)
  - 주석처리 다시 풀 것 !!

* 모델 변경을 완료했으면 해당 모델에 맞게끔 forms도 변경해줘야함. -> forms.py이용

```python
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','nickname', 'location', 'university']
```

- user확장 이후 admin에 들어가도 등록한 유저가 적용되지 않음 -> admin.py에 모델을 등록해야됨

```python
# account/admin.py
from django.contrib import admin
from .models import CustomUser
# Register your models here.

admin.site.register(CustomUser)
```
