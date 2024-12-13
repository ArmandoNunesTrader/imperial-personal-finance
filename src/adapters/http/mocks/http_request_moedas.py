#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   http_request_moedas.py
@Created :   13/12/2024 09:31:50
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Mock da requisição HEEP para teste da Controller da entidade Moedas
    ============================================================================
"""

from src.adapters.http.http_types.http_request import HttpRequest


class HTTPRequestCriarMoeda(HttpRequest):
    def __init__(
        self,
        headers: str = None,
        body: str = None,
        query_params: any = None,
        path_params: any = None,
        url: str = None,
        ipv4: str = None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
