FROM python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 8080

CMD adk web --port $PORT
