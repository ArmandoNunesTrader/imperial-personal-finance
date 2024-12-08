#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   validate_utils_test.py
@Created :   08/12/2024 11:10:11
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes das funções utilitárias de validação e segurança
    ============================================================================
"""

import src.utils.validate_utils as fvl

str_aux_1 = "Minha String"
str_aux_2 = 1000.5
str_aux_3 = "fcafe9ce-db7b-4d28-83b4-9cdd0837eb8c"


def test_is_valid_uuid():
    assert fvl.is_valid_uuid(str_aux_1) is False
    assert fvl.is_valid_uuid(str_aux_2) is False
    assert fvl.is_valid_uuid(str_aux_3) is True
