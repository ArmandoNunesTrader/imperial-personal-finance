#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tipos_de_contas.py
@Created :   07/12/2024 12:15:25
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Enum de tipos de contas
    ============================================================================
"""

from enum import StrEnum
from typing import List


class TiposDeContas(StrEnum):
    ATIVO = "Conta de Ativo"
    BANCO = "Conta Corrente Bancária"
    INVESTIMENTO = "Conta de Investimento"
    CAIXA = "Conta Caixa"

    @classmethod
    def value_to_name(cls, val):
        return {v: k for k, v in dict(vars(cls)).items() if isinstance(v, str)}.get(
            val, None
        )

    @classmethod
    def all_names(cls) -> List:
        return [elem.name for elem in cls]

    @classmethod
    def all_values(cls) -> List:
        return [elem.value for elem in cls]
