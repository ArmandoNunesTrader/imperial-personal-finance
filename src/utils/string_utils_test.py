#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   string_utils_test.py
@Created :   03/12/2024 11:37:32
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes das funções utilitárias de manipulação de strings
    ============================================================================
"""

import src.utils.string_utils as fsu

str_aux_1 = "Minha String"


def test_string_repeat():
    assert fsu.string_repeat("-", 10) == "----------"


def test_substring_after():
    assert fsu.substring_after(str_aux_1, " ") == "String"


def test_substring_before():
    assert fsu.substring_before(str_aux_1, " ") == "Minha"


def teste_substring_contains():
    assert fsu.substring_contains(str_aux_1, "Minh") is True
    assert fsu.substring_contains(str_aux_1, "Aux") is False


def test_last_chars():
    assert fsu.last_chars(str_aux_1, 6) == "String"
    assert fsu.last_chars(str_aux_1, 20) == str_aux_1


def test_first_chars():
    assert fsu.first_chars(str_aux_1, 6) == "Minha "
    assert fsu.first_chars(str_aux_1, 0) == str_aux_1
    assert fsu.first_chars("", 6) == ""


def test_first_2_chars():
    assert fsu.first_2_chars(str_aux_1) == "Mi"


def test_pad_int_left():
    assert fsu.pad_int_left(1234, 8) == "   1.234"


def test_pad_str_left():
    assert fsu.pad_str_left(str_aux_1, 15, "-") == "---Minha String"


def test_pad_str_right():
    assert fsu.pad_str_right(str_aux_1, 15, "-") == "Minha String---"


def test_pad_str_center():
    assert fsu.pad_str_center(str_aux_1, 15, "-") == "--Minha String-"


def test_real_br_money_mask():
    assert fsu.real_br_money_mask(0.01) == "R$ 0,01"
    assert fsu.real_br_money_mask(123456789.12) == "R$ 123.456.789,12"
    assert fsu.real_br_money_mask(1) == "R$ 1,00"
    assert fsu.real_br_money_mask("a") == "R$ 0,00"
