#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   criar_moeda_controller_test.py
@Created :   13/12/2024 09:37:30
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do Controller Criar Moeda
    ============================================================================
"""

from src.use_cases.moedas.manter_moedas import CriarMoeda
from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.adapters.http.mocks.http_request_moedas import HTTPRequestCriarMoeda
from src.adapters.http.controllers.criar_moeda_controller import CriarMoedaController


def test_criar_moeda_controller():
    obj_http_request = HTTPRequestCriarMoeda(
        headers=None,
        body=None,
        query_params={
            "sigla": "EUR",
            "descricao": "Euro",
            "tipo_de_moeda": "BRL",
            "valor_da_paridade": 6.35,
        },
        path_params=None,
        url=None,
        ipv4=None,
    )
    obj_repository = MoedasRepositorio()
    obj_use_case = CriarMoeda(obj_repository)

    obj_controller = CriarMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_http_request)

    assert obj_response is not None
    assert obj_response.status_code == 200
