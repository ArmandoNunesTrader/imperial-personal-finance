#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   centros_de_custo_errors.py
@Created :   11/12/2024 12:59:35
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classes de erro referentes à entidade Centros de Custo
    ============================================================================
"""


class CentroDeCustoNaoInformado(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRequest"
        self.code = 400
