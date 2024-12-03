#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   database_mysql_connector.py
@Created :   02/12/2024 23:05:34
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de conexão com o banco de dados MySQL 8.0.30
    ============================================================================
"""

import mysql.connector as mysql_connector

import init.db.database_connector as db
import init.db.mysql.database_mysql_config as cfg

import src.utils.directory_utils as fdu

from init.db.mysql.database_mysql_utils import (
    # mysql_create_connection,
    mysql_msg_error,
    mysql_check_exist_database,
)


class MySQLConnector(db.DatabaseConnector):
    # --------------------------------------------------------------------------
    # Construtor
    # --------------------------------------------------------------------------
    def __init__(self, verify=False):
        super().__init__()

        self.__create_dir_and_db(verify)

        # Monta os parâmetros de configuração
        config = cfg.load_config()
        db_name = config["database"]
        self.check = verify

        # Verifica se o database existe e cria se não existir
        if mysql_check_exist_database(config) is False:
            if self.__create_db() is None:
                print(f"Banco de dados < {db_name} > criado com sucesso!")
                fdu.get_ok_option()
                if self.__create_functions() is not None:
                    raise Exception("Erro na criação do Bancod e Dados!")
            else:
                raise Exception("Erro na criação do Bancod e Dados!")

        # Conecta ao servidor do MySQL
        self.conn, db_error = self.connect_db()
        if self.conn is None:
            msg_error = self._mysql_msg_error(db_error)
            raise Exception(msg_error)

        return self.conn

    # --------------------------------------------------------------------------
    # Funções privadas utilitárias
    # --------------------------------------------------------------------------
    def __create_db(self):
        config = cfg.load_config()
        db_name = config["database"]
        config_db = config
        config_db.pop("database")

        # Tenta conectar ao servidor de banco de dados
        try:
            # Tenta a conexão
            with mysql_connector.connect(**config_db) as self.conn:
                create_db_query = (
                    """
                        CREATE DATABASE """
                    + db_name
                    + """
                            DEFAULT CHARACTER SET = utf8mb4
                            DEFAULT COLLATE = utf8mb4_unicode_ci;
                    """
                )
                with self.conn.cursor() as cursor:
                    cursor.execute(create_db_query)
        except mysql_connector.DatabaseError as db_error:
            msg_error = self._mysql_msg_error(db_error)
            raise Exception(msg_error)

        return None

    def __create_functions(self):
        # Tenta conectar ao servidor de banco de dados
        config = cfg.load_config()
        try:
            # Tenta a conexão
            with mysql_connector.connect(**config) as self.conn:
                create_db_functions = """
                        CREATE FUNCTION IF NOT EXISTS F_NOW() RETURNS TIMESTAMP
                        BEGIN
                            DECLARE MY_NOW TIMESTAMP;
                            SELECT (UTC_TIMESTAMP()) INTO MY_NOW;

                            RETURN MY_NOW;
                        END
                    """
                with self.conn.cursor() as cursor:
                    cursor.execute(create_db_functions)
        except mysql_connector.DatabaseError as db_error:
            msg_error = mysql_msg_error(db_error)
            raise Exception(msg_error)

        return None

    def __create_dir_and_db(self, verify=False):
        # Monta os parâmetros de configuração
        config = cfg.load_config()
        db_name = config["database"]
        self.check = verify

        # Verifica se o database existe e cria se não existir
        if mysql_check_exist_database(config) is False:
            if self.__create_db() is None:
                print(f"Banco de dados < {db_name} > criado com sucesso!")
                fdu.get_ok_option()
                if self._create_functions() is not None:
                    raise Exception("Erro na criação do Bancod e Dados!")
            else:
                raise Exception("Erro na criação do Bancod e Dados!")

        # Conecta ao servidor do MySQL
        self.conn, db_error = self.connect_db()
        if self.conn is None:
            msg_error = self._mysql_msg_error(db_error)
            raise Exception(msg_error)

        return self.conn
