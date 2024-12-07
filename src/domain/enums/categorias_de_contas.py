#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   categorias_de_contas.py
@Created :   07/12/2024 12:13:42
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Enum das categorias de contas
    ============================================================================
"""

from enum import StrEnum


class CategoriasDeContas(StrEnum):
    RECEITA = "Receita"
    DESPESA = "Despesa"
    INVESTIMENTO = "Investimento"

    @classmethod
    def name(cls, val):
        return {v: k for k, v in dict(vars(cls)).items() if isinstance(v, str)}.get(
            val, None
        )
