FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD saucisse
ENV MYSQL_DATABASE classicmodels
ENV MYSQL_USER moi
ENV MYSQL_PASSWORD iom

EXPOSE 3306

COPY bdd.sql /docker-entrypoint-initdb.d
