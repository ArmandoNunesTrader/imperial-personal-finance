#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tipos_de_lancamentos.py
@Created :   07/12/2024 12:08:13
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Enum dos tipos de lançamentos
    ============================================================================
"""

from enum import StrEnum


class TiposDeLancamentos(StrEnum):
    RECEITA = "Lançamento de Receita"
    DESPESA = "Lançamento de Despesa"
    INVESTIMENTO = "Lançamento de Investimento"
    OUTRO = "Outro Lançamento"

    @classmethod
    def name(cls, val):
        return {v: k for k, v in dict(vars(cls)).items() if isinstance(v, str)}.get(
            val, None
        )
