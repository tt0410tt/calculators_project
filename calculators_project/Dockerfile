# Anaconda 이미지를 베이스로 사용
FROM continuumio/anaconda3

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 프로젝트 파일을 컨테이너로 복사
COPY . .

# Python 3.12.4 설치
RUN conda install -y python=3.12.4

# requirements.txt에 있는 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# Python 스크립트를 실행하도록 설정
CMD ["python", "Test_Calculators_pack.py"]
