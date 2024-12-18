#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   atualizar_moeda_controller_test.py
@Created :   18/12/2024 10:32:47
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do controller de Atualizar Moeda
    ============================================================================
"""

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.manter_moedas import AtualizarMoeda
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.controllers.atualizar_moeda_controller import (
    AtualizarMoedaController,
)


def test_atualizar_moeda_controller_ok():
    obj_repo = MoedasRepositorio()
    id_moeda = str(obj_repo.repo[0].id_moeda)

    obj_request = HttpRequest()
    obj_request.query_params = [
        {
            "id_moeda": id_moeda,
            "sigla": "Minha Moeda",
            "descricao": "Minha Moeda de Teste",
            "_tipo_de_moeda": "Real Brasileiro",
            "_valor_da_paridade": 6.45,
        }
    ]

    obj_use_case = AtualizarMoeda(obj_repo)

    obj_controller = AtualizarMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 200
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_atualizar_moeda_controller_erro():
    obj_repo = MoedasRepositorio()
    id_moeda = str(obj_repo.repo[0].id_moeda)

    obj_request = HttpRequest()
    obj_request.query_params = [
        {
            "id_moeda": id_moeda,
            "sigla": "Mi",
            "descricao": "Minha Moeda de Teste com Descrição Muito Longa Para Testes de Erro ",  # noqa E501
            "_tipo_de_moeda": "Realxx Brasileiro",
            "_valor_da_paridade": -1.00,
        }
    ]

    obj_use_case = AtualizarMoeda(obj_repo)

    obj_controller = AtualizarMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 422
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_atualizar_moeda_controller_id_nao_localizado():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [
        {
            "id_moeda": "baf6c2c9-3e1b-4bf6-9916-a2dfb82f8d83",
            "sigla": "Minha Moeda",
            "descricao": "Minha Moeda de Teste",
            "_tipo_de_moeda": "Real Brasileiro",
            "_valor_da_paridade": 6.45,
        }
    ]

    obj_use_case = AtualizarMoeda(obj_repo)

    obj_controller = AtualizarMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 404
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))
