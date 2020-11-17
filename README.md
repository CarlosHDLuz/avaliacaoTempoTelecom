# README #

## Introdução

Esta é uma solução para a avaliação da Tempo Telecom.

## Como executar?

### Setup enviroment

#### Setup de enviroment para solução da avaliação da Tempo Telecom

0. Baixar e instalar Python3 [- versão 3.9.0 -](https://www.python.org/downloads/)
*Passo necessário em sistema Windows

1. Baixar e instalar PostgreSQL [- versão 13.1 -](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

2. Instalar a framework Django3 [- versão 3.1.3 -](https://www.djangoproject.com/)
```
pip install Django==3.1.3
```

3. Instalar psycopg2 [- versão 2.8.6 -](https://www.psycopg.org/), adapter de PostgreSQL para a linguagem Python
```
pip install psycopg2
```

4. Criar GROUP ROLE no PostgreSQL como superuser
```
CREATE ROLE "avaliacao-tempo-db-user" WITH
	LOGIN
	SUPERUSER
	CREATEDB
	CREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 's+}/!;>wB_9\S43L';
```

5. Criar banco de dados no PostgreSQL
```
CREATE DATABASE "avaliacao-tempo-db"
    WITH 
    OWNER = "avaliacao-tempo-db-user"
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
```

### Executar

0. Vá ao diretório do projeto onde se encontra 'manage.py'.

1. Execute:
```
py manage.py runserver
```
