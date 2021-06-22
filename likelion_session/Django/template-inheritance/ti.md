# 템플릿 상속

- 각종 템플릿 전체적으로 공통되는 요소들이 존재하면 base.html (기본이 되는 html파일)을 기준으로 하여 다른 html에 상속해줌으로써 코드의 중복을 해결할 수 있다.

1. 기준이 되는 base.html을 작성한다.
   - html파일의 기본 틀 (DOCTYPE, html태그, body footer navbar..... CSS JS 등등)
   - 경로 : 프로젝트 폴더 하위에 templates폴더 생성하여 해당 폴더에 base.html생성
2. base.html을 settings.py에 등록한다.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['blogProject/templates'], # 이곳!!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

3. 상속받을 html 파일에서 base.html로부터 상속받는 요소들을 모두 지우고, 템플릿 문법을 추가한다.

```html
{% extends 'base.html' %} {% block content %}

<!-- 공통 요소들. base.html로부터 상속받는 요소들 -->
{% endblock %}
```

4. base.html에 가서, div태그 내에 템플릿 문법을 추가한다.

```html
<body>
  <!--  ..... -->
  <div>{% block content %} {% endblock %}</div>
  <!--  ..... -->
</body>
```

- 상속받는 html파일의 공통 요소를 제외한 다른 요소들을 base.html로 가져온다고 생각!

### urls.py 깔끔하게 관리하기

1. app에 urls.py를 만든다.
2. admin path & home path - `path('',home, name="home")` 삭제
3. project 폴더의 urls.py 파일에서 앱의 url을 관리하는 부분 모두 삭제.
4. 이후 include를 통해 app의 url을 가져온다.

```python
# app directory/urls.py
"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', detail, name="detail"),
    path('new/',new,name='new'),
    path('create/', create, name="create"),
    path('edit/<str:id>',edit, name="edit" ),
    path('update/<str:id>', update,name="update"),
    path('delete/<str:id>', delete, name="delete"),
]

```

```python
# project directory / urls.py
"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home" ),
    path('blog/', include('blog.urls'))
]

```

1. django.urls의 include 를 import한다.
2. url을 추가한다. `path('app', include('app.urls'))`
