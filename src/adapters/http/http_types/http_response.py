#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   http_response.py
@Created :   12/12/2024 18:23:21
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe dos responses enviados via protocolo HTTP
    ============================================================================
"""


class HttpResponse:
    def __init__(self, status_code: int, body: str) -> None:
        self.status_code = status_code
        self.body = body
