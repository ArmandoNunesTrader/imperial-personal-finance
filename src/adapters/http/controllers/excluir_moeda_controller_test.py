#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   excluir_moeda_controller_test.py
@Created :   18/12/2024 09:27:31
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do controller de Excluir Moeda
    ============================================================================
"""

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.manter_moedas import ExcluirMoeda
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.controllers.excluir_moeda_controller import (
    ExcluirMoedaController,
)


def test_excluir_moeda_controller_ok():
    obj_repo = MoedasRepositorio()
    id_moeda = str(obj_repo.repo[0].id_moeda)

    obj_request = HttpRequest()
    obj_request.query_params = [{"id_moeda": id_moeda}]

    obj_use_case = ExcluirMoeda(obj_repo)

    obj_controller = ExcluirMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 200
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_excluir_moeda_controller_id_nao_localizado():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [{"id_moeda": "baf6c2c9-3e1b-4bf6-9916-a2dfb82f8d83"}]

    obj_use_case = ExcluirMoeda(obj_repo)

    obj_controller = ExcluirMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 404
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_excluir_moeda_controller_id_erro():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [{"id_moeda": "baf6c2c9-3e1b-Xbf6-9916-a2dfb82f8d83"}]

    obj_use_case = ExcluirMoeda(obj_repo)

    obj_controller = ExcluirMoedaController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 422
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))
