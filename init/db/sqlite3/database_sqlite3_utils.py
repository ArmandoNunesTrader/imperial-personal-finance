#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   database_sqlite3_utils.py
@Created :   03/12/2024 09:53:34
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Utilitários para tratamento do banco de dados SQLite3
    ============================================================================
"""

import logging
import time
import os
import sqlite3

import src.utils.directory_utils as fdu

# Configura o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Configura o log no console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Adiciona o log para arquivo
log_name = fdu.file_real_full_path(fdu.get_logs_path(), "sqlite3.log")
file_handler = logging.FileHandler(log_name)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# Trata as mensagens de erro do SQLite3
def sqlite3_msg_error(db_error: sqlite3.Error) -> str:
    msg = (
        "Ocorreu o seguinte erro:"
        + "\tError Code: {0}"
        + "\tSQLSTATE: {1}"
        + "\tError Message: {2}"
    ).format(db_error.sqlite_errorcode, "", db_error.sqlite_errorname)

    return msg


# Efetua a conexão ao servidor do SQLIte3L com gerenciamento de logs para os erros
def sqlite3_create_connection(
    db_full_name: str, attempts: int = 3, delay: int = 2
) -> any:
    attempt = 1
    # Implementa a rotina com reconexão
    while attempt < attempts + 1:
        try:
            msg_log = f"Banco de dados conectado em: {db_full_name}"
            conn = sqlite3.connect(db_full_name)
            logger.info(msg_log)
            return [conn, None]
        except sqlite3.Error as db_error:
            if attempts is attempt:
                # Tenta reconectar, se der erro sai, devolvendo a mensagem de erro
                logger.info(sqlite3_msg_error(db_error))
                return [None, db_error]
            logger.info(
                "Conexão ao banco de dados %s: %s. Tentando novamente (%d/%d)...",
                db_full_name,
                sqlite3_msg_error(db_error),
                attempt,
                attempts - 1,
            )
            # Delay para tentar a reconexão
            time.sleep(delay**attempt)
            attempt += 1

    return [None, None]


# Verifica se um database existe
def sqlite3_check_exist_database(db_full_name: str) -> bool:
    return os.path.isfile(db_full_name)
