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
        Funções utilitárias diversas para manipulação de paths
    ============================================================================
"""
import os

from typing import List
from pathlib import Path, PurePath

from src.utils.definitions import ROOT_PATH


# ------------------------------------------------------------------------------
# Garante que uma URL terminal com \ ou / dependendo do SO
# ------------------------------------------------------------------------------
def add_slash(path: str | None) -> str:
    if path is None:
        return None
    str_aux = Path(path) if Path(path).exists() else None
    if str_aux is None:
        return None

    return str(str_aux.resolve()) + os.sep


# ------------------------------------------------------------------------------
# Une o nome de um array de path e verifica se existe devolvendo o path
#   completo. Caso contrário devolve None
# ------------------------------------------------------------------------------
def union_paths_exists(*paths: List) -> str | None:
    result = Path(PurePath(*paths)).resolve()

    return str(result) if (result.exists()) else None


# ------------------------------------------------------------------------------
# Obtém o path completo para um path informado com separador ao final
# ------------------------------------------------------------------------------
def get_full_path(path: str) -> str | None:
    full = str(Path(PurePath(path)).resolve())

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
    result = union_paths_exists(get_base_path(), "src", "infrastructure", "data")

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
    result = union_paths_exists(get_base_path(), "src", "infrastructure", "logs")

    return None if result is None else add_slash(get_full_path(result))


# ------------------------------------------------------------------------------
# Obtém o caminho completo real de um arquivo
# ------------------------------------------------------------------------------
def file_exists_fullpath(path: str | None, filename: str | None) -> str | None:
    if (path is None) and (filename is None):
        return None
    if Path(PurePath(path)).exists():
        full_filepath = union_paths_exists(path, filename)
        return full_filepath

    return None


# ------------------------------------------------------------------------------
# Compõe o nome de um arquivo independente de sua existência
# ------------------------------------------------------------------------------
def file_real_full_path(*paths: List) -> str:
    result = Path(PurePath(*paths)).resolve()

    return str(result)
