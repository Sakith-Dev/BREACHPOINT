FROM php:8.2-fpm-alpine

RUN apk add --no-cache nginx supervisor sqlite-dev \
    && docker-php-ext-install pdo pdo_sqlite

RUN adduser -D -u 1001 nexauser

COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /usr/share/nginx/html

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
