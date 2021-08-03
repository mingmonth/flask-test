# 점프 투 플라스크

## 가상 환경 설정

```
$ python -m venv myproject
$ ls
myproject/  README.md
```

### 가상 환경 진입하기

```
$ cd myproject/Scripts
$ source ./activate
(myproject)
```

### 가상 환경 벗어나기

```
$ deactivate
```

## Install

### Python

```
$ python --version
Python 3.9.2
```

### Packages

```
$ pwd
/d/work/sp/python/flask-test/myproject/Scripts
(myproject)

$ pip install Flask
WARNING: You are using pip version 20.2.3; however, version 21.2.2 is available.
You should consider upgrading via the 'd:\work\sp\python\flask-test\myproject\scripts\python.exe -m pip install --upgrade pip' command.

$ python -m pip install --upgrade pip
```

## 플라스크 프로젝트 생성하기

### 프로젝트 디렉토리 생성 및 이동하기

```
$ mkdir projects
$ cd projects
$ mkdir project1
$ cd project1
$ cd /d/work/sp/python/flask-test/projects/project1
```

### 프로젝트 디렉토리에서 가상 환경 진입하기

```
$ source /d/work/sp/python/flask-test/myproject/Scripts/activate
```

### 프로젝트 디렉토리에서 가상 환경 벗어나기

```
$ cd /d/work/sp/python/flask-test/myproject/Scripts
$ deactivate
```

## Run

```
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
(myproject)

$ export FLASK_APP=pybo
(myproject)

$ flask run
 * Serving Flask app 'pybo' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

$ export FLASK_ENV=development
(myproject)

$ flask run
 * Serving Flask app 'pybo' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 106-950-093
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## To do

- [x] 플라스크 개발 준비
  - [x] 플라스크 시작하기
  - [x] 파이썬 설치하기
  - [x] 플라스크 개발 환경 준비하기
  - [x] 플라스크 프로젝트 생성하기
  - [x] 파이썬 설치하고 사용해 보기
  - [x] 안녕하세요, 파이보!
- [ ] 플라스크 기초 공사
  - [ ] 플라스크 기초 다지기
  - [ ] 플라스크 애플리케이션 팩토리
  - [ ] 블루프린트로 라우트 함수 관리하기
  - [ ] 모델로 데이터 처리하기
  - [ ] 질문 목록 조회와 질문 상세 조회 기능 만들기
  - [ ] 답변 등록 기능 만들기
  - [ ] 화면 예쁘게 꾸미기
  - [ ] 부트스트랩으로 더 쉽게 화면 꾸미기
  - [ ] 표준 HTML과 템플릿 상속 사용해 보기
  - [ ] 폼 모듈로 데이터 검증 더 쉽게 하기
- [ ] 파이보 서비스 개발
  - [ ] 내비게이션 기능 추가하기
  - [ ] 게시판 페이징 기능 추가하기
  - [ ] 템플릿 필터 직접 만들어 보기
  - [ ] 게시물에 일련번호 추가하기
  - [ ] 질문에 달린 답변 개수 표시하기
  - [ ] 회원가입 기능 추가하기
  - [ ] 로그인과 로그아웃 구현하기
  - [ ] 모델 수정하여 파이보 기능 다듬기
  - [ ] 글쓴이 표시 기능 추가하기
  - [ ] 게시물 수정 & 삭제 기능 추가하기
  - [ ] 댓글 기능 추가하기
  - [ ] 추천 기능 추가하기
  - [ ] 스크롤 초기화 문제점 해결하기
  - [ ] 마크다운 기능 적용하기
  - [ ] 검색, 정렬 기능 추가하기
  - [ ] 도전! 저자 추천 파이보 추가 기능
- [ ] 세상세 선보이는 파이보 서비스
  - [ ] 깃으로 버전 관리하기
  - [ ] 깃허브 사용해 보기
  - [ ] 파이보를 위한 서버 운영 방법 알아보기
  - [ ] AWS 라이트세일 사용해 보기 - 1달 무료
  - [ ] 파이보 세상에 공개하기
  - [ ] 서버 개발 환경을 위한 config 분리하기
  - [ ] MobaXterm으로 서버에 접속하기
  - [ ] 웹 브라우저와 서버, 파이보 동작 방식 이해하기
  - [ ] WSGI 서버 Gunicorn 사용하기
  - [ ] 웹 서버, Nginx 사용해서 파이보에 접속하기
  - [ ] 운영 환경으로 배포하기
  - [ ] 서비스답게 오류 페이지 다듬기
  - [ ] 플라스크에 로깅 적용하기
  - [ ] 파이보에 도메인 적용하기 - 비용 발생
  - [ ] PostgreSQL 데이터베이스 적용하기 - 1달 무료
