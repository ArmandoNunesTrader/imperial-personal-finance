#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   criar_moeda_controller_test.py
@Created :   18/12/2024 10:21:10
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do controller de Criar Moeda
    ============================================================================
"""

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.manter_moedas import CriarMoeda
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.controllers.criar_moeda_controller import (
    CriarMoedaController,
)


def test_criar_moeda_controller_ok():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [
        {
            "sigla": "Minha Moeda",
            "descricao": "Minha Moeda de Teste",
            "_tipo_de_moeda": "Real Brasileiro",
            "_valor_da_paridade": 6.45,
        }
    ]

    obj_use_case = CriarMoeda(obj_repo)

    obj_controller = CriarMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 201
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_criar_moeda_controller_erro():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [
        {
            "sigla": "Mi",
            "descricao": "Minha Moeda de Teste com Descrição Muito Longa Para Testes de Erro ",  # noqa E501
            "_tipo_de_moeda": "Realxx Brasileiro",
            "_valor_da_paridade": -1.00,
        }
    ]

    obj_use_case = CriarMoeda(obj_repo)

    obj_controller = CriarMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 422
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))
