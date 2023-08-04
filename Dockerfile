FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY watch_next.py /app/watch_next.py
COPY movies.txt /app/movies.txt

CMD ["python", "watch_next.py"]
