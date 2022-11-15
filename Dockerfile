FROM python:alpine

WORKDIR /app

COPY ./app /app

RUN pip install Flask
RUN pip install flask_login

CMD ["python", "index.py"]


