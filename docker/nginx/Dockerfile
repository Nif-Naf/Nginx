# Указывает какой использовать официальный образ.
FROM nginx
# Заменяем дефолтный файл конфигурации, на наш кастомный.
COPY ../../nginx.conf /etc/nginx/nginx.conf
# Копирование шаблонов в контейнер.
COPY ../../templates/nginx.html /etc/nginx/templates/index.html
COPY ../../templates/not_found.html /etc/nginx/templates/not_found.html
# Копирование картинок в контейнер.
COPY ../../images/cat.jpg /etc/nginx/images/
COPY ../../images/sea.jpg /etc/nginx/images/
COPY ../../images/mountains.jpg /etc/nginx/images/
