# 🐼 핑크판다 개발 작업실

## 1. Ubuntu 터미널 기본 조작

### 1-1. 최초 작업 위치 확인

**실행 명령어**

```bash
pwd
```

**실제 실행 결과**

```text
/mnt/c/Windows/system32
```

### 1-2. 홈 디렉터리 이동

**실행 명령어**

```bash
cd ~
pwd
```

**실제 실행 결과**

```text
/home/soonjin4105185
```

### 1-3. 프로젝트 폴더 생성 및 이동

**실행 명령어**

```bash
mkdir -p ~/pink-panda-workspace
cd ~/pink-panda-workspace && pwd
```

**실제 실행 결과**

```text
/home/soonjin4105185/pink-panda-workspace
```

### 1-4. 숨김 파일을 포함한 홈 디렉터리 목록 확인

**실행 명령어**

```bash
ls -la ~ | tee home-directory-log.txt
cat home-directory-log.txt
```

**실행 결과**

Ubuntu 홈 디렉터리의 파일과 숨김 파일 목록이 정상적으로 출력되었다.
실제 출력 결과는 아래 로그 파일에 저장했다.

[홈 디렉터리 목록 실행 로그](home-directory-log.txt)

**검증 방법:** `cat home-directory-log.txt`로 저장된 목록을 다시 확인했다.

### 1-6. 파일에 문자열 저장 및 출력 확인

**실행 명령어**

```bash
echo 'Hello Pink Panda!' > practice.txt
cat practice.txt
```

**실제 출력 결과**

```text
Hello Pink Panda!
```

**검증 결과:** practice.txt 파일에 문자열을 저장하고, 새 Bash에서 cat 명령어로 정상 출력되는 것을 확인했다.

**문제 해결 기록:** 기존 Bash에서 일반 출력이 보이지 않았으나, /bin/bash --noprofile --norc 명령어로 새 Bash를 실행한 후 출력이 정상적으로 표시되었다. 기존 Bash의 정확한 문제 원인은 확인되지 않았다.

### 1-7. 파일 복사 실습

**실행 명령어**

```bash
cp practice.txt practice-copy.txt && ls -l practice-copy.txt
cat practice-copy.txt
```

**실제 확인된 출력 결과**

```text
Hello Pink Panda!
```

**검증 결과:** cp 명령어로 practice.txt 파일을 practice-copy.txt로 복사했다. ls -l 명령어로 복사 파일의 생성을 확인하고, cat 명령어로 원본과 동일한 문자열이 저장된 것을 확인했다.

### 1-8. 파일 이름 변경 실습

**실행 명령어**

```bash
mv -n practice-copy.txt practice-renamed.txt && ls -l practice-renamed.txt
cat practice-renamed.txt
```

**실제 확인된 출력 결과**

```text
Hello Pink Panda!
```

**검증 결과:** mv 명령어로 practice-copy.txt 파일의 이름을 practice-renamed.txt로 변경했다. ls -l 명령어로 변경된 파일의 존재를 확인하고, cat 명령어로 파일 내용이 유지된 것을 확인했다.

### 1-9. 파일 이동 실습

**실행 명령어**

```bash
mkdir -p backup && ls -ld backup
mv -n practice-renamed.txt backup/ && ls -l backup/practice-renamed.txt
cat backup/practice-renamed.txt
```

**실제 확인된 출력 결과**

```text
Hello Pink Panda!
```

**검증 결과:** mkdir 명령어로 backup 폴더를 생성했다. mv 명령어로 practice-renamed.txt 파일을 backup 폴더로 이동했으며, ls -l 명령어로 이동한 파일의 존재를 확인했다. cat 명령어로 파일 내용이 유지된 것을 확인했다.

### 1-10. 파일 삭제 실습

**실행 명령어**

```bash
touch delete-practice.txt && ls -l delete-practice.txt
rm -i delete-practice.txt
```

**삭제 확인 과정**

rm 명령어 실행 후 삭제 여부를 묻는 질문이 표시되어 y를 입력했다.

**삭제 여부 검증 명령어**

```bash
test ! -e delete-practice.txt && echo 'DELETE_OK' || echo 'FILE_STILL_EXISTS'
```

**실제 출력 결과**

```text
DELETE_OK
```

**검증 결과:** 연습용 파일을 생성한 뒤 rm -i 명령어로 삭제했다. test 명령어를 사용해 파일이 더 이상 존재하지 않는 것을 확인했다.

### 1-11. 리눅스 파일 권한 변경 실습

**실행 명령어**

```bash
ls -l practice.txt
chmod u+x practice.txt && ls -l practice.txt
```

**실제 확인된 권한 변경 결과**

```text
변경 전: -rw-r--r--
변경 후: -rwxr--r--
```

**검증 결과:** chmod u+x 명령어로 practice.txt 파일 소유자에게 실행 권한(x)을 추가했다. ls -l 명령어로 권한이 정상적으로 변경된 것을 확인했다.

### 1-12. Bash 스크립트 작성 및 실행 실습

**작성한 파일: hello.sh**

```bash
#!/bin/bash
echo 'Hello Pink Panda!'
echo 'I am learning Bash scripting!'
```

**실행 명령어**

```bash
bash hello.sh
```

**실제 출력 결과**

```text
Hello Pink Panda!
I am learning Bash scripting!
```

**검증 결과:** hello.sh 파일을 작성하고 bash hello.sh 명령어로 실행했다. 두 문장이 정상적으로 출력되는 것을 확인했다.

## 2. Docker 실습

### 2-1. Docker 설치 및 실행 상태 확인

**실행 명령어**

```bash
docker --version
docker info
```

**실제 확인 결과**

```text
Docker version 29.9.2, build a82e528
Server Version: 29.9.2
Operating System: Docker Desktop
Containers: 4
Images: 6
```

### 2-2. hello-world 컨테이너 실행

**실행 명령어**

```bash
docker run hello-world
```

**실제 확인된 출력**

```text
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

**오류 및 해결 과정**

최초 실행 시 Docker Desktop Linux 엔진에 연결할 수 없다는 npipe 오류가 발생했다.
Windows 11에서 Docker Desktop의 Engine running 상태를 확인했다.
docker info 명령어로 Docker 서버 연결을 다시 검증한 후 docker run hello-world를 재실행하여 성공했다.

**검증 결과:** Docker 29.9.2 환경에서 hello-world 컨테이너가 정상 실행되었다.

### 2-3. Ubuntu 컨테이너 실행 및 파일 복사

**실행 명령어**

```bash
docker run -it --name panda-ubuntu-practice ubuntu:latest bash
pwd
mkdir -p /panda-study && ls -ld /panda-study
cd /panda-study && pwd
echo 'Hello from Pink Panda Docker!' > hello.txt
cat hello.txt
exit
```

**컨테이너에서 호스트로 파일 복사**

```bash
docker cp panda-ubuntu-practice:/panda-study/hello.txt ~/pink-panda-workspace/docker-hello.txt
cat ~/pink-panda-workspace/docker-hello.txt
```

**실제 확인된 출력 결과**

```text
Hello from Pink Panda Docker!
```

**검증 결과:** Ubuntu 컨테이너 안에서 /panda-study/hello.txt 파일을 생성했다. docker cp 명령어로 파일을 호스트의 pink-panda-workspace 폴더에 복사하고, cat 명령어로 내용이 동일한 것을 확인했다.

### 2-4. Dockerfile 이미지 빌드 및 웹서버 실행

**Dockerfile 내용**

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```

**실행 및 검증 명령어**

```bash
docker build -t pink-panda-web:1.0 ~/pink-panda-workspace
docker images pink-panda-web
docker run -d --name pink-panda-web-test -p 8080:80 pink-panda-web:1.0
docker ps
docker exec pink-panda-web-test cat /usr/share/nginx/html/index.html
curl -s http://localhost:8080/
```

**실제 확인 결과**

- Docker 이미지 빌드: FINISHED
- 생성된 이미지: pink-panda-web:1.0
- 컨테이너 이름: pink-panda-web-test
- 컨테이너 상태: Up
- 포트 연결: 8080:80
- 웹브라우저 접속 주소: http://localhost:8080
- 웹페이지 제목: 핑크판다 개발 작업실
- 웹페이지 표시: 분홍색 배경과 핑크판다 문구 정상 출력

**오류 및 해결 기록**

- 문제: 웹브라우저에서 Welcome to nginx! 기본 화면이 표시됨
- 확인: docker exec 및 curl 명령어로 핑크판다 HTML이 정상 제공되는 것을 확인함
- 해결: 브라우저에서 Ctrl+Shift+R로 강력 새로고침
- 최종 결과: 핑크판다 웹페이지 정상 표시

### 2-5. Docker 바인드 마운트 실습

- 사용 이미지: nginx:alpine
- 컨테이너 이름: pink-panda-bind
- 포트 연결: 8081:80
- 마운트 방식: bind (읽기 전용)
- 원본 파일: ~/pink-panda-workspace/index.html
- 컨테이너 파일: /usr/share/nginx/html/index.html
- 검증 명령어: docker exec pink-panda-bind grep -n "Docker Bind Mount" /usr/share/nginx/html/index.html
- 검증 결과: Docker 컨테이너에서 수정된 HTML 문장 확인 성공
- 웹브라우저: http://localhost:8081 접속 및 새 문장 표시 성공
- 문제 해결: sed -i 실행 후 파일이 교체되어 컨테이너를 다시 생성함

### 2-6. Docker 볼륨 실습

- 볼륨 이름: pink-panda-data
- 볼륨 생성: docker volume create pink-panda-data
- 볼륨 목록 확인: docker volume ls
- 첫 번째 컨테이너: pink-panda-volume-test
- 볼륨 연결 위치: /panda-data
- 저장 파일: /panda-data/hello.txt
- 저장 내용: Hello Pink Panda Volume!
- 검증 명령어: cat /panda-data/hello.txt
- 기존 컨테이너 삭제: docker rm pink-panda-volume-test
- 새 컨테이너: pink-panda-volume-check
- 검증 결과: 새 컨테이너에서도 기존 파일 내용 확인 성공
- 결론: 컨테이너 삭제 후에도 Docker 볼륨 데이터 유지 확인
