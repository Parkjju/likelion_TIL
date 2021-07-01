# 배포 사전준비

- 환경변수

  - 시스템에 저장되어 있는 변수

- requirements

  - 장고 앱을 실행하기 위해 설치되어야 하는 패키지들
  - `pip freeze` -> 해당 환경에 설치된 모든 패키지 확인하는 명령어
  - `pip freeze > requirements.txt`로 requirements.txt에 패키지 정보 저장

- IAM

  - Identity and Access Management
  - IAM에서 계정을 만든 후 해당 계정의 로그인 정보를 이용하여 AWS의 API 활용

- S3
  - Simple Storage Service
  - AWS판 구글드라이브같은 것
  - 용량지정 없이 사용한 만큼만 과금
  - 여러 서버에서 동시 접속 가능

1. AWS 로그인 - 지역설정
2. IAM검색 - Add user - 사용자 이름은 자유롭게, access유형 ->프로그래밍 방식 액세스 체크
3. 권한 - 검색창에 s3 -> amazonS3FullAccess체크
4. 태그(메모) 생략 후 시크릿 키 csv파일형태로 받아서 보관 (중요)

### s3와 연동하기

- `pip install django-stoarges`패키지 다운 & `boto3` 패키지도 다운
- django-storages 공식문서 참조하여 아마존 S3관련 변수들 설정.
  - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME 기본 설정

```python
# 추가적으로 region성격에 따른 변수선언
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_S3_CUSTOM_DOMAIN = 'd37gx43o3Int1n.cloudfront.net'
```
