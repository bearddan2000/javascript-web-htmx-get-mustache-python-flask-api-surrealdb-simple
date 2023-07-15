
FROM python:latest

COPY bin/ /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV WAIT_VERSION 2.7.2

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD ["python", "app.py"]