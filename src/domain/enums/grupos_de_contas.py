#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   grupos_de_contas.py
@Created :   07/12/2024 12:12:02
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Enum dos grupos de contas
    ============================================================================
"""

from enum import StrEnum
from typing import List


class GruposDeContas(StrEnum):
    ATIVO = "1-Ativo"
    PASSIVO = "2-Passivo"
    RESULTADO = "3-Resultado"

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
