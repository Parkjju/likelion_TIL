# git submodule 사용법

-   [참고 자료](https://ohgyun.com/711)

-   서브모듈이란? git repository 아래에 다른 하위 git repository를 관리하기 위한 도구

### 초기화

```bash
# $git submodule add organization이름 <path - 생략가능>
$git submodule add likelion_organiztion
```

-   서브모듈 명령어 수행시

    1. 자식 폴더에 organization을 클론한다
    2. .gitmodules 파일이 신규생성됨.
    3. .git/config 파일에 서브모듈 관련 내용이 추가됨

```bash
[submodule "likelion9th"]
        url = https://github.com/hufslion9th/likelion9th.git
        active = true
```

### 커밋

```bash
$git commit -m "Message"
```

-   커밋을 하면 서브모듈로 저장한 organization 저장소의 최신 커밋이 내 저장소의 현재 커밋에 포함되게 된다

```bash
$git submodule init
$git submodule update
```

## 정리

1. organization 공유 레포를 git clone한다.
2. clone한 폴더로 이동한다. (cd 명령어 이용)
3. 해당 폴더에 나의 github repository URL로 submodule을 추가한다.
4. 커밋 - 로그 확인 후 push하면 공유 폴더에 repository연결완료

-   [submodule 최종 정리본 - 생활코딩](https://github.com/Parkjju/TIL/blob/master/Git/git_submodule.md)
