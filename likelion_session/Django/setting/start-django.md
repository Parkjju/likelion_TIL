# Django 시작하기

-   Django? - framework 중 하나

    -   framework - 개발하는데 자주 사용되거나 반복적으로 사용되는 것들을 미리 만들어둔 것
    -   framework == 라이브러리? (개발의 자유도에 있어서 차이 - 프레임워크를 사용하면 개발 속도가 빠르다는 장점)

-   Django 시작하기
    1. vscode - 새 터미널
    2. git bash 선택
    3. 가상환경 켜기 - 개발 환경에 따라 달라지는 파이썬 버전을 통합된 환경에서 관리하기 위함
        - Windows - `python -m venv virtual-name` : python -m venv + 가상환경 이름
        - MacOS - `python -m venv name` 명령어에 오류 발생시 `python3 -m venv name`으로 진행 (나는 안뜸)
    4. myvenv폴더 확인
        - windows - myvenv/Scripts/activate 파일
        - mac - myvenv/bin/activate 파일
    5. activate 실행
        - `source myvenv/Scripts/activate`
    6. Django 다운 - `pip install django`
        - pip - Python install package : 파이썬 패키지 다운받아주는 시스템
    7. myvenv/lib 내에 장고 관련 파일들이 생성됨.
    8. Django 프로젝트 생성
        - `django-admin startproject projectname` -> projectname으로 프로젝트 폴더 생성됨
    9. 프로젝트 서버 실행하기 (manage.py - 프로젝트 실행을 위해 필수적인 파일로, 서버 기동이 기능 중 하나)
        - cd명령어 이용하여 프로젝트 폴더로 이동
        - manage.py는 파이썬 파일이므로 파이썬 인터프리터로 실행 `python manage.py runserver`
        - 주소 클릭시 django서버로 이동할 수 있음
