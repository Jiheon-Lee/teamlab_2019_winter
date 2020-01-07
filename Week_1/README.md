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
### 리눅스란?
리눅스(Linux)는 리누스 토발즈가 커뮤니티 주체로 유닉스(UNIX) 운영체제를 기반으로 만들어진 컴퓨터 운영체제입니다. 리눅스(Linux)는 유닉스(UNIX)와 마찬가지로 다중 사용자, 다중 작업(멀티태스킹), 다중 스레드를 지원하는 네트워크 운영 체제(NOS)입니다. 현재는 상당수의 웹 서버와 모바일 장치(안드로이드 등)를 구동하는 운영체제로도 많이 이용이 되고 있습니다.
- LINUX (Linux is Not Unix)  : '리눅스는 유닉스가 아니다'의 약자
- NOS (Network Operation System) : 사람이 컴퓨터를 사용할 수 있도록 하는 프로그램 중 하나

### 리눅스를 사용해야하는 이유
1. 모든 소스가 오픈되어 있어 광범위하게 사용된다.
2. 다중사용자, 다중작업을 지원하기 때문에 시스템적으로 서버를 운영하기에 적합하다.
3. 리눅스는 무료이며 개발 환경이 풍부하다.

### 리눅스 실습 환경 만들기
1. 설치가 필요없는 CodeOnWeb <https://codeonweb.com>
2. 직접 운영체제 설치
3. 가상머신(Virtual box)

### 리눅스 명령어 정리
- **디렉토리와 파일**
  - **PWD**<br>
  현재 경로 보기<br>
  <img src="https://user-images.githubusercontent.com/48443734/71870559-af3bbe80-3159-11ea-94dc-cf828b629c1a.PNG"></img><br/>
  <pre> 현재 경로는 /root 라고 표시되어 있다. </pre>
  
  - **CD**<br>
  해당 디렉토리 이동하기<br>
  <pre>cd {인자값}
       cd . : 현재 디렉토리로 이동
       cd .. : 상위 디렉토리로 이동
       cd ~ : 홈 디렉토리로 이동
       cd - : 이전 작업 디렉토리로 이동</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71871481-a7314e00-315c-11ea-80b1-6691f79b4c04.PNG"></img><br/>
  <pre> ~/workspace 로 이동하였다. </pre>
  
  - **LS**<br>
  파일 내역 출력<br>
  <pre>ls {옵션} {디렉토리/파일}
       -a: 모든 파일과 디렉토리 표시 
       -l: 자세히 출력 
       -d: 디렉토리 정보 출력 
       -n: UID, GID 출력 
       -R: 하위 경로와 모든 파일 나열</pre>
  <img src="https://user-images.githubusercontent.com/48443734/71872085-af8a8880-315e-11ea-9f8e-c26bdee9cb30.PNG"></img><br/>
  <pre> /workspace 폴더의 모든 파일과 디렉토리를 자세히 출력 </pre>
  
  - **CP**<br>
  파일, 디렉토리 복사<br>
  <pre>cp {옵션} {복사소스} {복사위치}
       -f: 강제로 복사 
       -r: 하위 경로 포함하여 복사 
       -v: 복사 진행 상황 출력 
       -s: 링크 정보 유지하여 복사 </pre>
  <img src="https://user-images.githubusercontent.com/48443734/71872088-b0bbb580-315e-11ea-9525-c601a8fb11f2.PNG"></img><br/>
  <pre> test1.txt 파일의 내용을 복사하여 test2.txt 파일을 생성함 </pre>
  
    - **MKDIR**<br>
  디렉토리 생성<br>
  <pre>mkdir {옵션} {이름}
       -m: 디렉토리 생성 시 기본 권한 설정 
       -p: 상위 디렉토리 생성
       --help: 도움말 
       --version: 버전 표시 </pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874138-7fde7f00-3164-11ea-8d77-0385432db14c.PNG"></img><br/>
  <pre> mv_test 디렉토리가 생성된 것을 확인 </pre>
  
  - **MV**<br>
  파일, 디렉토리 이동<br>
  <pre>mv {옵션} {이동소스} {이동타겟}
       -i: 이동에 대한 실행 여부 물음 
       -f: 강제로 이동 
       -u: 이동 대상 위치보다 최근 파일 시 이동 
       -v: 이동 진행 상태 출력 
       -b: 대상 파일이 이미 있어 백업 파일 생성  </pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874141-810fac00-3164-11ea-975b-baeac4c0fbe8.PNG"></img><br/>
  <pre> test1.txt를 mv_test 디렉토리로 이동한 것을 확인 </pre>
  
  - **RM**<br>
  파일, 디렉토리 삭제<br>
  <pre>rm {옵션} {디렉토리/파일}
       -f: 강제삭제 
       -r: 디렉토리 삭제 시 하위 경로와 파일 삭제 
       -v: 파일 삭제 정보를 자세히 보여줌 </pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874251-cb912880-3164-11ea-885d-0a566b4e9b48.PNG"></img><br/>
  <pre> mv_test 디렉토리가 삭제된 것을 확인 </pre>
  
  - **CAT**<br>
  텍스트 파일 내용 출력<br>
  <pre>cat {옵션} {파일 이름}
       >: 내용 덮어 씌우기 
       >>: 기존 파일 내용 추가 </pre>
  <img src="https://user-images.githubusercontent.com/48443734/71874592-abae3480-3165-11ea-9f50-1190b9799d2b.PNG"></img><br/>
  <img src="https://user-images.githubusercontent.com/48443734/71874598-ae108e80-3165-11ea-8c9b-ff04354e1433.PNG"></img><br/>
  <pre> test2.txt 파일에 내용이 출력된 것을  </pre>
  
  - **TOUCH**<br>
  파일 생성 및 시간 정보 변경<br>
  <pre>touch {옵션} {파일이름}
       -r: 시간 동기화
       -t: 지정 시간으로 변경 </pre>
  
  - **HEAD**<br>
  파일 내용 중 처음부터 10줄 출력<br>
  <pre>head {파일이름} </pre>
  
  - **TAIL**<br>
  파일 내용중 마지막부터 10줄 출력<br>
  <pre>tail {파일이름} </pre>
  
  - **FILE**<br>
  파일 종류 확인<br>
  <pre>file {파일이름} </pre>
  
  - **CHOWN**<br>
  chown(change the owner of a file) 파일의 소유권을 바꾸기 위해 사용<br>
  <pre>chown {옵션} {변경할유저이름:변경할그룹이름} {파일이름}
         -R : 하위 디렉토리에도 모든 권한 변경<br>
    - chown {변경할유저이름} – 소유자만 변경
    - chown {:변경할그룹이름} – 그룹만 변경
    - chown {변경할유저이름:} – 소유자와 그룹 모두 동일한걸로 변경
    - chown {변경할유저이름:변경할그룹이름} – 소유자와 그룹을 서로 다른걸로 변경 </pre>
  
  - **CHMOD**<br>
    - 파일의 권한을 변경
    - 8진수 형태와 심볼릭 형태로 사용 가능
    - 심볼릭이 기능적인 면으론 좋지만 조금 복잡
    - 쉽게 쓸려면 8진수 형태<br>
  <pre>chmod {옵션} {8진수Permission} {파일명} – 8진수 형태
  chmod {옵션} {대상}{+/-/=}{rwx} {파일명} – 심볼릭 형태
           -R : 하위 디렉토리에도 모든 권한 변경
           -c : 권한 변경 파일내용을 출력<br></pre>
  
  <pre>chmod 명령어 8진수<br>
  777 : 일반적인 8진수 형태
  4777 : SetUid 설정, 4000을 더함
  2777 : SetGid 설정, 2000을 더함
  1777 : Sticky bit 설정, 1000을 더함<br>
  8진수 7은 2진수 111
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
  + : 해당 권한을 추가한다.
  – : 해당 권한을 제거한다.
  = : 해당 권한을 설정한데로 변경한다.

  - rwx<br>
  r : 읽기 권한
  w : 쓰기 권한
  x : 실행 권한
  
### Git & Github
