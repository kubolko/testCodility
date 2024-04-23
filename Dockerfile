FROM postgres:latest

ENV POSTGRES_DB=testdb
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=mysecretpassword

EXPOSE 5432

COPY ./init.sql /docker-entrypoint-initdb.d/
