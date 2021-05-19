# mac OS 세팅

1. chrome다운
2. python다운 (3.7XX이상)
3. git 설치
    - homebrew이용 - (mac에서 필요한 프로그램들을 다운받게 도와주는 프로그램)
    - homebrew사이트에서 install homebrew 명령어 복사하여 터미널상에 입력
    - `brew install git`입력하여 git설치
    - `brew install python`을 통해 파이썬도 설치 가능
    - `git --version`명령어를 통해 깃 설치 버전 확인
    - git 설치 이후 기본설정
        1. `git config --global user.name "git이름"`
        2. `git config --global user.email "email주소"`
        3. `git config --list`를 통해 설정파일 확인
4. vscode 설치
    1. korea language pack(필수 아님) - CTRL+shift+K -> `configure display language - ko`를 통해 한국어 설정 가능
    2. python extension(설치완료)

-   [How to set Python3 as a default python version on Macos?](https://dev.to/malwarebo/how-to-set-python3-as-a-default-python-version-on-mac-4jjf)
    1. `brew install python` - brew를 통해 파이썬 설치
    2. `ls -l /usr/local/bin/python*` - 설치 확인
    3. `ls -s -f /usr/local/bin/python3.X /usr/local/bin/python` - python3.X버전으로 바꾸기
    4. 터미널 껐다 키기
    5. `python -V` 또는 `python --version`으로 버전 확인
