#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   directory_utils.py
@Created :   02/12/2024 22:44:29
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de funções utilitárias diversas para manipulação de paths
    ============================================================================
"""
import os

from typing import List

import src.utils.string_utils as fsu

from src.utils.definitions import ROOT_PATH


# ------------------------------------------------------------------------------
# Garante que uma URL terminal com \ ou / dependendo do SO
# ------------------------------------------------------------------------------
def add_slash(path: str) -> str:
    path = os.path.realpath(path) + os.sep

    if fsu.last_chars(path, 2) == (os.sep * 2):
        return path[:-1]
    else:
        return path


# ------------------------------------------------------------------------------
# Une o nome de um array de path e verifica se existe devolvendo o path
#   completo. Caso contrário devolve None
# ------------------------------------------------------------------------------
def union_paths_exists(*paths: List) -> str | None:
    result = file_real_full_path(*paths)

    return result if os.path.exists(result) else None


# ------------------------------------------------------------------------------
# Obtém o path completo para um path informado com separador ao final
# ------------------------------------------------------------------------------
def get_full_path(path: str) -> str | None:
    full = union_paths_exists(add_slash(os.path.realpath(path + os.sep + ".")))

    return full


# ------------------------------------------------------------------------------
# Obtém o path raiz do projeto
# ------------------------------------------------------------------------------
def get_base_path() -> str | None:
    return None if ROOT_PATH is None else add_slash(ROOT_PATH)


# ------------------------------------------------------------------------------
# Obtém o diretório de dados do sistema
# ------------------------------------------------------------------------------
def get_data_path() -> str | None:
    result = union_paths_exists(get_base_path(), "data")

    return None if result is None else add_slash(get_full_path(result))


# ------------------------------------------------------------------------------
# Obtém o diretório do banco de dados local
# ------------------------------------------------------------------------------
def get_bd_path() -> str | None:
    result = union_paths_exists(get_data_path(), "db")

    return None if result is None else add_slash(get_full_path(result))


# ------------------------------------------------------------------------------
# Obtém o diretório dos arquivos de logs
# ------------------------------------------------------------------------------
def get_logs_path() -> str | None:
    result = union_paths_exists(get_base_path(), "logs")

    return None if result is None else add_slash(get_full_path(result))


# ------------------------------------------------------------------------------
# Obtém o caminho completo real de um arquivo
# ------------------------------------------------------------------------------
def file_exists_fullpath(path: str | None, filename: str | None) -> str | None:
    if (path is None) and (filename is None):
        return None
    if os.path.exists(path):
        full_filepath = union_paths_exists(os.path.join(path, filename))
        return full_filepath

    return None


# ------------------------------------------------------------------------------
# Compõe o nome de um arquivo independente de sua existência
# ------------------------------------------------------------------------------
def file_real_full_path(*paths: List) -> str:
    result = os.path.realpath((os.sep).join(paths))

    return result
