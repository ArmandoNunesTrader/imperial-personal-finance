#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tipos_de_moedas.py
@Created :   07/12/2024 12:07:19
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""


"""
    ============================================================================
        Enum de tipos de moedas
    ============================================================================
"""

from enum import StrEnum


class TiposDeMoedas(StrEnum):
    BRL = "Real Brasileiro"
    USD = "Dólar Americano"
    EUR = "Euro"

    @classmethod
    def name(cls, val):
        return {v: k for k, v in dict(vars(cls)).items() if isinstance(v, str)}.get(
            val, None
        )
