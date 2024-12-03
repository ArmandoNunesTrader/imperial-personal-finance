#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   dataabse_mysql_utils.py
@Created :   02/12/2024 23:07:11
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Utilitários de tratamento do banco de dados MySQL 8.0.30
    ============================================================================
"""

import logging
import time
import mysql.connector

import src.utils.directory_utils as fdu

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler(
    fdu.file_fullpath(fdu.get_logs_path(), "mysql_8_0_30.log")
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# Trata as mensagens de erro do MySQL
def mysql_msg_error(db_error):
    msg = (
        "Ocorreu o seguinte erro: \n"
        + "\tError Code: {0}\n"
        + "\tSQLSTATE: {1}\n"
        + "\tError Message: {2}\n"
    ).format(db_error.errno, db_error.sqlstate, db_error.msg)

    return msg


# Efetua a conexão ao servidor do MySQL com gerenciamento de logs para os erros
def mysql_create_connection(config, attempts=3, delay=2):
    attempt = 1
    # Implementa a rotina com reconexão
    while attempt < attempts + 1:
        try:
            return [mysql.connector.connect(**config), None]
        except (mysql.connector.Error, IOError) as db_error:
            if attempts is attempt:
                # Tenta reconectar, se der erro sai devolvendo a mensagem de erro
                msg_error = mysql_msg_error(db_error)
                logger.info("Erro ao conectar, saindo se uma conexão: %s", msg_error)
                return [None, db_error]
            logger.info(
                "Erro na conexão: %s. Tentando novamente (%d/%d)...",
                db_error,
                attempt,
                attempts - 1,
            )
            # Delay para tentar a reconexão
            time.sleep(delay**attempt)
            attempt += 1

    return [None, None]


# Verifica se um database existe
def mysql_check_exist_database(config):
    try:
        # Tenta criar a conexão com o servidor MySQL
        config_db = config
        db_name = config["database"]
        del config_db["database"]
        my_db = mysql.connector.connect(**config_db)

        # Cria um cursor para executar os comandos MySQL
        my_cursor = my_db.cursor()

        # Check se um database existe
        my_cursor.execute("SHOW DATABASES")
        databases = my_cursor.fetchall()

        database_exists = False
        for database in databases:
            if db_name in database:
                database_exists = True
                break
    except mysql.connector.Error:
        database_exists = False

    return database_exists
