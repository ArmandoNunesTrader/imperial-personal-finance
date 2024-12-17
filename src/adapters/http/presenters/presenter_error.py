#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   presenter_error.py
@Created :   17/12/2024 10:28:15
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Presenter genérico de erros do sistema
    ============================================================================
"""

from typing import Dict

from src.adapters.http.http_types.http_response import HttpResponse


def presenter_error(error: Dict) -> HttpResponse:
    return HttpResponse(
        status_code=error["status_code"],
        body=error["body"],
    )
