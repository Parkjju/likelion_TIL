# 장고와 데이터베이스

- ORM - Object Relation Mapping
  - python만으로 데이터베이스에 데이터와 관련된 작업이 가능. -> models.py
  - 데이터베이스의 테이블을 파이썬 크래스로 구현한다.

```python
class Blog:
    id = num
    제목 = 문자
    #...
```

# Model 실습

- 데이터베이스 테이블을 만드는 과정 - 실습절차

  1. 가상환경 및 장고 개발환경 세팅
  2. models.py - 파이썬 클래스 생성
     - 테이블 각 속성에 맞게 자료형 지정
     - import 되어있는 models모듈 `models.CharField(max_length=200)` ... 다양한 자료 성격과 파라미터 존재
  3. models.py 수정 후 `python manage.py makemigrations`
     - 앱 내에 migration 폴더를 만들어서 models.py의 변경사항 저장
     - [no changes detected 오류 관련](https://stackoverflow.com/questions/36153748/django-makemigrations-no-changes-detected)
     - makemigrations 명령어는 models.py의 변경사항을 인식 -> 테이블을 해당 형식으로 만들어주겠다는 뜻
     - 정상적으로 진행 뒤 `migrations for appname` 뜸.
  4. `python manage.py migrate`
     - migration 폴더를 실행시켜 데이터베이스에 적용

- 데이터베이스에 대한 권한을 가지는 슈퍼유저 만들기 (런서버는 꺼져있어야함)
  1. `python manage.py createsuperuser`
  2. user name & email address입력 & 패스워드 입력
  3. django 서버의 admin으로 들어가서 로그인해도 테이블 적용이 안됨 -> admin.py에 자신의 앱 등록

```python
from django.contrib import admin
from .models import Blog
# Register your models here.
admin.site.register(Blog)
```
