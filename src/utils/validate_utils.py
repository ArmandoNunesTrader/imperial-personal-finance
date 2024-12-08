#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   validate_utils.py
@Created :   08/12/2024 11:07:42
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Funções auxiliares de validação e segurança
    ============================================================================
"""

from uuid import UUID


# Verifica se um valor informado é uma UUID válida
def is_valid_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        return False
