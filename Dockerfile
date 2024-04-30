FROM python:3

WORKDIR /app

COPY . /app

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install

CMD ["bash", "devserver.sh"]