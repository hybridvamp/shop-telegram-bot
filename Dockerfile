FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get install python3.10 python3-pip
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install

CMD ["bash", "devserver.sh"]