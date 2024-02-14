
FROM python:3.8-slim-buster

WORKDIR /python-docker

RUN pip3 install flask

COPY . .

ENV PORT=8000

ENV FLASK_APP="server.py"
ENV FLASK_ENV="development"
ENV FLASK_RUN_HOST="127.0.0.1"
ENV FLASK_RUN_PORT=$PORT

CMD [ "python3", "-m" , "flask", "run"]
