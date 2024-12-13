#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   http_request.py
@Created :   12/12/2024 18:21:43
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe dos requests recebidos via protocolo HTTP
    ============================================================================
"""


# O comentário é para que esse teste não seja computado no relatório de cobertura
class HttpRequest:
    def __init__(
        self,
        headers: str = None,
        body: str = None,
        query_params: any = None,
        path_params: any = None,
        url: str = None,
        ipv4: str = None,
    ) -> None:
        self.headers = headers  # pragma: no cover
        self.body = body  # pragma: no cover
        self.query_params = query_params  # pragma: no cover
        self.path_params = path_params  # pragma: no cover
        self.url = url  # pragma: no cover
        self.ipv4 = ipv4  # pragma: no cover
