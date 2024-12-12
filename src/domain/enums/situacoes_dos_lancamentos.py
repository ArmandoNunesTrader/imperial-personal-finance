#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   situacoes_dos_lancamentos.py
@Created :   07/12/2024 12:10:27
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Enum das situações dos lançamentos
    ============================================================================
"""

from enum import StrEnum
from typing import List


class SituacoesDosLancamentos(StrEnum):
    RECEBIDO = "Recebido"
    PAGO = "Pago"
    A_RECEBER = "A Receber"
    A_PAGAR = "A Pagar"

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
