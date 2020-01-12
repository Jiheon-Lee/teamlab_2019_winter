1주차 Linux Bootcamp, Git & Github
================================

Github 페이지 형성 후 README.md에 프로젝트 명과 기간 등 필요 내용 추가하기 2020.01.02 ~ 2020.01.08

Courses
-------
### Linux Bootcamp
- [생활코딩 리눅스 강좌](https://www.inflearn.com/course/%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B0%95%EC%A2%8C)
, 생활코딩, 2017
- [리눅스 커맨드라인 툴](https://www.inflearn.com/course/command-line/), 인프런, 2019

### Git & Github
- [지옥에서 온 Git](https://www.inflearn.com/course/%EC%A7%80%EC%98%A5%EC%97%90%EC%84%9C-%EC%98%A8-git#curriculum), 생활코딩, 2018
- [버전 관리 시스템 git](https://www.inflearn.com/course/git-2#), 생활코딩, 2018
- [Git과 Github](https://www.inflearn.com/course/git-and-github#), 생활코딩, 2018

학습 내용 정리
-----------
### 리눅스 명령어 정리
- **디렉토리와 파일**
  - **PWD**<br>
  현재 경로 보기
  <pre>$ pwd</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71870559-af3bbe80-3159-11ea-94dc-cf828b629c1a.PNG"></img>
  <pre>현재 경로는 /root 라고 표시되어 있다.</pre><br>

  - **CD**<br>
  해당 디렉토리 이동하기
  <pre>$ cd {인자값}
      cd . : 현재 디렉토리로 이동
      cd .. : 상위 디렉토리로 이동
      cd ~ : 홈 디렉토리로 이동
      cd - : 이전 작업 디렉토리로 이동</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71871481-a7314e00-315c-11ea-80b1-6691f79b4c04.PNG"></img>
  <pre>~/workspace 로 이동하였다.</pre><br>

  - **LS**<br>
  파일 내역 출력
  <pre>$ ls {옵션} {디렉토리/파일}
      -a: 모든 파일과 디렉토리 표시
      -l: 자세히 출력</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71872085-af8a8880-315e-11ea-9f8e-c26bdee9cb30.PNG"></img>
  <pre>/workspace 폴더의 모든 파일과 디렉토리를 자세히 출력</pre><br>

  - **CP**<br>
  파일, 디렉토리 복사
  <pre>$ cp {옵션} {복사파일} {복사위치}
      -f: 강제로 복사
      -r: 하위 경로 포함하여 복사
      -v: 복사 진행 상황 출력</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71872088-b0bbb580-315e-11ea-9525-c601a8fb11f2.PNG"></img>
  <pre>test1.txt 파일의 내용을 복사하여 test2.txt 파일을 생성함</pre><br>

  - **MKDIR**<br>
  디렉토리 생성
  <pre>$ mkdir {옵션} {이름}
      -m: 디렉토리 생성 시 기본 권한 설정
      -p: 상위 디렉토리 생성
      --help: 도움말</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874138-7fde7f00-3164-11ea-8d77-0385432db14c.PNG"></img>
  <pre>mv_test 디렉토리가 생성된 것을 확인</pre><br>

  - **MV**<br>
  파일, 디렉토리 이동
  <pre>$ mv {옵션} {이동소스} {이동타겟}
      -f: 강제로 이동
      -v: 이동 진행 상태 출력</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874141-810fac00-3164-11ea-975b-baeac4c0fbe8.PNG"></img>
  <pre>test1.txt를 mv_test 디렉토리로 이동한 것을 확인</pre><br>

  - **RM**<br>
  파일, 디렉토리 삭제
  <pre>$ rm {옵션} {디렉토리/파일}
      -f: 강제삭제
      -r: 디렉토리 삭제 시 하위 경로와 파일 삭제
      -v: 파일 삭제 정보를 자세히 보여줌</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874251-cb912880-3164-11ea-885d-0a566b4e9b48.PNG"></img>
  <pre>mv_test 디렉토리가 삭제된 것을 확인</pre><br>

  - **CAT**<br>
  텍스트 파일 내용 출력
  <pre>$ cat {옵션} {파일 이름}
      >: 내용 덮어 씌우기
      >>: 기존 파일 내용 추가</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874592-abae3480-3165-11ea-9f50-1190b9799d2b.PNG"></img>
  <img src="https://user-images.githubusercontent.com/48443734/71874598-ae108e80-3165-11ea-8c9b-ff04354e1433.PNG"></img>
  <pre>test2.txt 파일에 내용이 출력된 것을 확인</pre><br>

  - **TOUCH**<br>
  비어있는 파일 생성
  <pre>$ touch {파일이름}</pre><br>
  <img src="https://user-images.githubusercontent.com/48443734/72221195-a56fec00-359b-11ea-8a7b-b747cac85da5.PNG"></img>
  <pre>test1.txt가 생성됨</pre><br>

  - **HEAD**<br>
  파일 내용 중 처음부터 10줄 출력
  <pre>$ head {파일이름}</pre><br>

  - **TAIL**<br>
  파일 내용중 마지막부터 10줄 출력<br>
  <pre>$ tail {파일이름} </pre><br>

  - **CHOWN**<br>
  chown(change the owner of a file) 파일의 소유권을 바꾸기 위해 사용<br>
  <pre>$ chown {옵션} {변경할유저이름:변경할그룹이름} {파일이름}
      -R : 하위 디렉토리에도 모든 권한 변경
    - chown {변경할유저이름} – 소유자만 변경
    - chown {:변경할그룹이름} – 그룹만 변경
    - chown {변경할유저이름:} – 소유자와 그룹 모두 동일한걸로 변경
    - chown {변경할유저이름:변경할그룹이름} – 소유자와 그룹을 서로 다른걸로 변경</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71878313-ad302a80-316e-11ea-95bb-b588dcc5ba66.PNG"></img><br>
  <per>빨간색 선 기준으로 왼쪽은 소유자, 오른쪽은 그룹</per><br>

  - **CHMOD**<br>
    - 파일의 권한을 변경
    - 8진수 형태와 심볼릭 형태로 사용 가능
    - 심볼릭이 기능적인 면으론 좋지만 조금 복잡
    - 쉽게 쓸려면 8진수 형태
  <pre>$ chmod {옵션} {8진수Permission} {파일명} – 8진수 형태
  $ chmod {옵션} {대상}{+/-/=}{rwx} {파일명} – 심볼릭 형태
      -R : 하위 디렉토리에도 모든 권한 변경
      -c : 권한 변경 파일내용을 출력</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71878246-7e19b900-316e-11ea-9046-7167cbb3fbbe.PNG"></img><br>
  <per>d는 디렉토리, -는 파일<br>
  3칸 기준으로<br>
  첫번째는 owner
  두번째는 group
  세번째는 other</per>
  <pre>chmod 명령어 8진수<br>
  8진수 0~7은 아래와 같이 2진수로 표현이 가능
  0 : 000
  1 : 001
  2 : 010
  3 : 011
  4 : 100
  5 : 101
  6 : 110
  7 : 111
  위 2진수 세자리는 rwx 세자리와 일치하며 2진수가 1이면 해당 권한을 부여, 0이면 해당 권한을 제거</pre>

  <pre>chmod 명령어 심볼릭<br>
  - 대상<br>
  u : user의 권한
  g : group의 권한
  o : other의 권한
  a : 모든 사용자 권한

  - +/-/=<br>
  + : 해당 권한을 추가
  – : 해당 권한을 제거
  = : 해당 권한을 설정한데로 변경

  - rwx<br>
  r : 읽기 권한
  w : 쓰기 권한
  x : 실행 권한

- **검색**
  - **FIND**<br>
  파일 찾기<br>

    **- 파일명검색 <-name>**
         <pre>파일 명에 'test'가 들어간 파일 검색 : # $ find .-name '*test'</pre>
    **- 파일 형식 <-type>**
         <pre>- f : 일반파일
          - d : 디렉토리
    디렉토리이면서 이름중에 git이 들어간 것을 검색 : # $ find .-type d -name '*git'</pre>
    **- 파일의 소유자 <-user>**
         <pre>소유자가 root인 파일 검색 : # $ find .-user root</pre>
  - **GREP**<br>
  텍스트 검색 기능을 가짐
  <pre>$ grep {검색어} {파일이름}</pre>
  <img src="https://user-images.githubusercontent.com/48443734/72221491-9a6a8b00-359e-11ea-88d5-eaba8285ec82.PNG"></img>
  <pre>test2.txt 파일의 내용에서 TEAM을 검색</pre><br>

- **프로세스**
  - **PS**<br>
  ps(process status) 시스템에서 현재 수행되고 있는 프로세스를 확인<br>
  <pre>$ ps aux</pre>
  <img src="https://user-images.githubusercontent.com/48443734/72221565-81160e80-359f-11ea-814d-503f52fbf36a.PNG"></img><br>

  - **Kill**<br>
  프로세스를 종료<br>
  <pre>$ kill {SIGNAL} {프로세스명}
  $ kill -9 {프로세스명}   # 응답없어도 강제종료
  $ kill -15 {프로세스명}  # 일반적 종료</pre>

  - **TOP**<br>
  시스템의 운용사항을 실시간으로 모니터링할 수 있는 유틸리티로, 윈도우의 작업관리자를 연상하면 된다. CPU, 메모리, 프로세스등을 확인할 수 있다.
  <pre>$ top</pre>
  <img src="https://user-images.githubusercontent.com/48443734/72221604-c9cdc780-359f-11ea-861d-b02ebf993bf0.PNG"></img><br>

  - **Daemon**<br>
  데몬 실행 및 종료
  <pre>$ sudo service {데몬이름} start # 데몬 실행
  $ sudo service {데몬이름} stop # 데몬 중지
  $ sudo service {데몬이름} restart # 데몬 재시작</pre><br>

- **SSH(원격제어)**
  - **SSH**<br>
  SSH server 설치 (sever 컴퓨터, client 컴퓨터)<br>
  <pre>$ sudo apt-get install openssh-server
  $ sudo apt-get install openssh-client</pre>

  SSH server 실행<br>
  <pre>$ sudo service ssh start</pre>

  Client 컴퓨터로 server 컴퓨터 원격제어하기<br>
  <pre>$ ssh {서버사용자이름}@{ip address}</pre><br>

  - **SSH-Keygen**<br>
  rsa라는 암호화 방식으로 키를 생성<br>
  <pre>$ ssh-keygen -t rsa</pre>

    키를 확인<br>
  <pre>$ ls -al ~/.ssh/</pre>

  파일|설명
  ----|-----
  id_rsa|private key, 절대로 타인에게 노출되면 안된다.
  id_rsa.pub|public key, 접속하려는 리모트 머신의 authorized_keys에 입력한다.
  authorized_keys|리모트 머신의 .ssh 디렉토리 아래에 위치하면서 id_rsa.pub 키의 값을 저장한다.<br>

### Git & Github
### Git이란?
리누스 토발즈에 의해 개발된 Git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한  **분산 버전 관리 시스템**이다. 또한 소프트웨어를 개발하는 기업의 핵심 자산인 소스코드를 효율적으로 관리할 수 있게 해주는 **형상 관리 도구**라고도 한다. Git은 무료이며 공개소프트웨어이다.<br>

### Git을 사용해야하는 이유
1. 소스코드를 주고 받을 필요 없이, 같은 파일을 **여러 명이 동시에 작업하는 병렬 개발이 가능**하다.
2. 분산 버전관리이기 때문에 인터넷이 연결되지 않은 곳에서도 개발을 진행할 수 있으며, 중앙 저장소가 날라가버려도 다시 **원상복구**할 수 있습니다.
3. 다른 사람과 함께 일하는 경우, **여러명과 함께 코드 공유를 공유**하고 변경사항에 대해 충돌하는 일이 발생하지 않는다.
4. 팀 프로젝트가 아닌, 개인 프로젝트일지라도 Git을 통해 버전 관리를 하면 **체계적인 개발이 가능**하다.
5. 개발 환경에서 **실수를 할 수 있기 때문**이다.<br>

### Git 명령어 정리
- **환경 설정**<br>
전역 사용자명/이메일 설정
<pre>$ git config - -global user.name “Your name” 
$ git config - -global user.email “Your email address”
    --global 옵션은 전역 설정에 대한 옵션</pre><br>
    
- **기본 명령어**<br>
현재 git의 버전을 확인
<pre>$ git --version</pre>
현재 디렉토리에 git 저장소를 생성
<pre>$ git init</pre>
파일은 수정했지만 아직 stage area에 올라가지 않은 파일들을 staging area에 올림
<pre>$ git add {파일이름}</pre>
staging area에 올라가 있는 파일들을 commit
<pre>$ git commit {옵션} {파일이름}
       -a : 기존에 add를 하지 않아도 바로 staging area에 올려서 commit 함
       -m : editor없이 commit의 메시지를 입력 # $ git commit -m test.txt "Version1"</pre>
파일들의 변경사항을 조회
<pre>$ git status</pre>
이전에 어떠한 작업을 했는지 조회
<pre>$ git diff</pre>
두 개의 버전에서 소스코드의 차이점을 보여줌
<pre>$ git diff {commit 고유번호}..{다른 commit 고유번호}</pre><br>

- **Branch와 Merge**<br>
  - **Branch**<br>
  현재 존재하는 브랜치를 조회
  <pre>$ git branch
         -r : 원격저장소의 브랜치를 확인</pre>
  브랜치 생성
  <pre>$ git branch {branch명}
           - master가 기본 branch</pre>
  다른 브랜치로 변경
  <pre>$ git checkout <branch명></pre><br>
  - **Merge**<br>
  현재 브랜치에서 입력한 브랜치와 merge(합치다)
  <pre>$ git merger {branch명}</pre><br>
  
- **로그 관리**<br>
  변경된 사항의 기록들을 확인
  <pre>$ git log
         -p : 더 자세하게 보여줌</pre>
  기존의 commit에서 변경한 내용을 취소해서 새로운 commit을 만듬
  <pre>$ git revert
         -n : 바로 commit 하지 않기 때문에 여러번한 다음에 commit이 가능</pre>
  예전 버전으로 돌아감
  <pre>$ git reset {commit 고유번호} --hard</pre><br>
  
- **원격저장소 :remote repository**<br>
  원격저장소 만들 때는 수정이 불가한 저장소의 역할만 하는 디렉토리를 만들어야 한다.
  <pre>$ git init --bare {디렉토리명}</pre>
  현재 저장소에 원격저장소를 add(연결)한다. 경로 앞에 origin이라 하면 경로는 origin을 가르킴, 원격저장소의 기본 이름은 origin
  <pre>$ git remote add origin {경로}</pre>
  추가한 원격저장소의 목록을 확인
  <pre>$ git remote
         -v : 자세하게 보여줌</pre>
  원격저장소를 제거
  <pre>$ git remote remove origin</pre>
  현재 브랜치를 연결시킨 지역저장소에서 원격저장소에 푸쉬, 즉 업로드
  <pre>$ git push origin</pre>
  원격저장소의 파일들을 지역저장소로 가져옴
  <pre>$ git pull</pre>
  원격저장소의 파일들을 디렉토리를 생성하여 안에 다운로드
  <pre>$ git clone {원격저장소 주소} {디렉토리명}</pre>
