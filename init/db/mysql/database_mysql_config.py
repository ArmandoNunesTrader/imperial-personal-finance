#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   database_mysql_config.py
@Created :   02/12/2024 23:16:38
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Tratamento das configurações do MySQL 8.0.30
    ============================================================================
"""

from configparser import ConfigParser

import src.utils.directory_utils as fdu


# Carrega a configuração
def load_config(section="mysql"):
    # Nome do arquivo de configuração
    filename = fdu.file_fullpath(".", "mysql.ini")

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
