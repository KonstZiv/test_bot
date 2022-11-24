FROM python:3.8-slim-buster AS base
LABEL maintainer="Kostuantyn Zivenko <kos.zivenko@gmail.com>"
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
RUN apt-get update && apt-get install -y curl
RUN useradd -m -u $UID docker_user
USER docker_user
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/home/docker_user/poetry python3 -

ENV PATH="/home/docker_user/poetry/bin:/home/docker_user/.cache/pypoetry/virtualenvs/test-bot-gO1Yu1FF-py3.8/bin:${PATH}"

# Инициализация проекта
WORKDIR /home/docker_user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY poetry.lock pyproject.toml ./
RUN  poetry install --no-interaction --no-ansi
COPY . .
CMD ["python3", "./testbot/echo_bot.py"]
