#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   database_sqlite3_config.py
@Created :   03/12/2024 10:06:42
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Tratamento das configurações do SQLite3
    ============================================================================
"""

from configparser import ConfigParser

import src.utils.directory_utils as fdu

from src.utils.definitions import ROOT_PATH


# Carrega a configuração
def load_config(section="sqlite3"):
    # Nome do arquivo de configuração
    filename = fdu.file_exists_fullpath(
        fdu.file_real_full_path(ROOT_PATH, "init", "db", "sqlite3"), "sqlite3.ini"
    )
    if filename is None:
        msg = "Arquivo de configuração {0} não pode ser localizado!!"
        raise Exception(msg.format(filename))

    # Objeto Parser
    parser = ConfigParser()
    parser.read(filename)

    # Obtém a seção que contém as configurações
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(
            "A seção {0} não foi localizada no arquivo {1} de configuração!!"
        ).format(section, filename)

    return config
