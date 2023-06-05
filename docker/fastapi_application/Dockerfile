# Образ.
FROM python:3

# Настройки окружения.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Установка рабочего каталога.
WORKDIR /code

# Копирование файлов в контейнер.
COPY ../../applications/fastapi_application /code/app
COPY ../../requirements.txt /code/

# Установка зависисмостей. И обновление pip.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
