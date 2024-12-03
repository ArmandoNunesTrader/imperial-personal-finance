#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   database_sqlite3_connector.py
@Created :   02/12/2024 22:58:31
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de conexão com o banco de dados SQLite3
    ============================================================================
"""

import sqlite3

import init.db.database_connector as db
import init.db.sqlite3.database_sqlite3_config as cfg

import src.utils.directory_utils as fdu

from init.db.sqlite3.database_sqlite3_utils import (
    sqlite3_create_connection,
    sqlite3_msg_error,
    sqlite3_check_exist_database,
)


class SQLite3Connector(db.DatabaseConnector):
    # --------------------------------------------------------------------------
    # Construtor
    # --------------------------------------------------------------------------
    def __init__(self, verify: bool = False):
        super(SQLite3Connector, self).__init__()
        # super().__init__()

        self.__config = cfg.load_config()
        self.__db_name = self.get_db_name()

        self.create_dir_and_db(verify)

    # --------------------------------------------------------------------------
    # Métodos herdados
    # --------------------------------------------------------------------------
    def get_db_name(self) -> str:
        result = fdu.file_real_full_path(fdu.get_bd_path(), self.__config["database"])
        return result

    def create_db(self) -> bool:
        try:
            return sqlite3.connect(self.__db_name) is not None
        except:  # noqa E722
            return False

    def create_functions(self) -> bool:
        return True

    def create_dir_and_db(self, verify: bool = False) -> None:
        # Verifica se o database existe e cria se não existir
        if sqlite3_check_exist_database(self.__db_name) is False:
            if self.create_db():
                if self.create_functions() is False:
                    raise Exception("Erro na criação das funções no Banco de Dados!")
            else:
                raise Exception("Erro na criação do Banco de Dados!")

    def connect_db(self) -> any:
        self.__conn, msg_error = sqlite3_create_connection(self.__db_name)
        if msg_error is not None:
            self.__conn = None
            raise Exception(sqlite3_msg_error(msg_error))
        else:
            return self.__conn

    def desconnect_db(self) -> None:
        try:
            self.__conn.close()
        except sqlite3.Error:
            pass
