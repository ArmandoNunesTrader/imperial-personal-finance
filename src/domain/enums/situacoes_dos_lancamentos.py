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


class SituacoesDosLancamentos(StrEnum):
    RECEBIDO = "Recebido"
    PAGO = "Pago"
    A_RECEBER = "A Receber"
    A_PAGAR = "A Pagar"

    @classmethod
    def name(cls, val):
        return {v: k for k, v in dict(vars(cls)).items() if isinstance(v, str)}.get(
            val, None
        )
