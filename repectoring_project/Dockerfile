# Ubuntu LTS 버전 사용
FROM python:3.9.0

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 프로젝트 파일을 컨테이너로 복사
COPY . .

# requirements.txt에 있는 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# Python 스크립트를 실행하도록 설정
CMD ["python", "run.py"]
