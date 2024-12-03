#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   directory_utils_test.py
@Created :   03/12/2024 12:58:16
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes das funções de tratamento de diretórios
    ============================================================================
"""

import os

import src.utils.string_utils as fsu
import src.utils.directory_utils as fdu

from src.utils.definitions import ROOT_PATH

part_1 = ROOT_PATH
part_2 = "src"
part_3 = ROOT_PATH + os.sep + "src"


def test_add_slash():
    assert fsu.last_chars(fdu.add_slash("."), 1) == os.sep
    assert fsu.last_chars(fdu.add_slash(".\\"), 1) == os.sep


def test_union_paths_exists():
    assert fdu.union_paths_exists(part_1, part_2) == part_3


def test_get_full_path():
    assert fdu.get_full_path(part_3) == (part_3)


def test_get_base_path():
    assert fdu.get_base_path() == ROOT_PATH + os.sep


def test_get_data_path():
    assert fdu.get_data_path() == (ROOT_PATH + os.sep + "data" + os.sep)


def test_get_bd_path():
    assert fdu.get_bd_path() == (ROOT_PATH + os.sep + "data" + os.sep + "db" + os.sep)


def test_get_logs_path():
    assert fdu.get_logs_path() == (ROOT_PATH + os.sep + "logs" + os.sep)


def test_file_exists_fullpath():
    assert (
        fdu.file_exists_fullpath(ROOT_PATH, "requirements.txt")
        == ROOT_PATH + os.sep + "requirements.txt"
    )

    assert fdu.file_exists_fullpath(ROOT_PATH, "none.txt") is None


def test_file_real_full_path():
    assert (
        fdu.file_real_full_path(ROOT_PATH, "requirements.txt")
        == ROOT_PATH + os.sep + "requirements.txt"
    )

    assert (
        fdu.file_real_full_path(ROOT_PATH, "none.txt")
        == ROOT_PATH + os.sep + "none.txt"
    )
