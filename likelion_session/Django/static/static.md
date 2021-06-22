# static

- 장고에서 다루는 파일

  1. 정적파일 : 미리 서버에 저장되어 있는 파일 - 서버에 저장된 그대로를 서비스해주는 파일
  2. 동적파일 : 서버의 데이터들이 어느정도 가공된 후 보여지는 파일

- 정적파일 구분

  1. static : 개발자가 서버를 개발할 때 미리 넣어놓은 파일 (html, css, js..img.. etc)
  2. media : 사용자가 업로드 할 수 있는 파일

- static파일 다루기
  1. app디렉토리에 static 폴더 생성
  2. 파일들 삽입
  3. settings.py의 static files 부분으로 이동
     - `import os` 먼저 진행후 STATIC 관련 코드 추가
  4. 이후 collectstatic 진행. `python manage.py collectstatic`

```python
# settings.py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' # 기본적으로 제공하는 코드

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog', 'static')
]# 현재 static 파일들이 어디있는지

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# static 파일을 어디에 모을건지
```

- html파일 상에서 static file들 가져오기
  1. body태그 상단부에 `{% load static %}` 추가 - static 폴더 내의 파일들을 로드하겠다는 뜻
  2. `<img src="{% static 'img.png' %}" />` 링크형식은 현재 디렉토리를 static폴더를 현재 디렉토리로 하여 작성
