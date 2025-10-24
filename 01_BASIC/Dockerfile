FROM python:3.11-slim
WORKDIR /app
# / : 리눅스 최상위 경로 (윈도우의 C드라이브)

# 의존성 먼저 설치
COPY requirements.txt .
# 리눅스 컨테이너의 기본경로 /app에 requirements를 복사하는 코드
RUN pip install --no-cache-dir -r requirements.txt
# pip install을 통해 캐시메모리를 사용하지 않고 바로 읽어온다

# 앱 파일 복사
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

