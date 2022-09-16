# Gimmunity README.md
- 기숙사생들의 활발한 소통을 위한 커뮤니티
- 수민외3(공도윤, 김수민, 전유리, 홍해인)
- 미림 스타트업 창업발표회 대상 수상작
- ---
- [기획서](https://bit.ly/3Tq5i80)
  - 미림계정 로그인, 기숙사생 전용 질문을 통과해야 가입 가능
  - 게시물 조회
  - 게시물 추가
  - 댓글
  - 기숙사 공지사항, 생활규칙 전달 (관리자만 추가 가능)
-----
1. **startproject** 시작하기(복붙복붙ㄱ 최신버전 설치 후 복붙  2번 띄고> . <필수 안나오면 성공)
   1. python -m pip install django~=3.2
   2. django-admin startproject Gimmunity .
   3. python manage.py runserver
   4. [참고](https://dog-sugar-f98.notion.site/django-47dc37c1206441b8892350f722bdd376)
   5. VCS > 맨위 >git
2. **startapp notice** 앱추가
   1. python ./manage.py startapp notice
   2. shift*2번 클릭 > installed_apps > settings로 와서 밑에 'notice', 추가
   3. models -> admin -> views -> templates -> urls
   4. **models** 작업!
      1. Notice 추가 (DB화..?)
      2. python manage.py makemigrations notice
      3. python manage.py migrate notice
   5. **admin** 작업 (pw: 미림과학고)
      1. NoticeAdmin
      2. python manage.py createsuperuser
   6. **views**
      1. NoticeListView
   7. **templates**
      1. notice_list.html
   8. **urls**
      1. notice:list