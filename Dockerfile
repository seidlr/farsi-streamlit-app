# app/Dockerfile

FROM python:3.9-slim

RUN mkdir -p /usr/src/app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt --upgrade

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "Top_Cognates.py", "--server.port=8501", "--server.address=0.0.0.0"]
