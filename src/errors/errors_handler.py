#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   errors_handler.py
@Created :   11/12/2024 17:18:44
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Handler global de tratamento de erros
    ============================================================================
"""
from typing import Dict

from src.errors.moedas_errors import MoedaErrosDeValidacao, MoedaNaoInformada


# O comentário é para que esta função não seja levada em conta no cálculo de
#   cobertura de testes do pytest
def handler_errors(error: Exception) -> Dict:  # pragma: no cover
    if isinstance(error, (MoedaNaoInformada, MoedaErrosDeValidacao)):
        return {
            "status_code": error.status_code,
            "body": {"errors": [{"title": error.name, "detail": error.message}]},
        }

    return {
        "status_code": 500,
        "body": [{"errors": [{"title": "Server Error", "detail": str(error)}]}],
    }
