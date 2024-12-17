#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_id_controller_test.py
@Created :   16/12/2024 22:34:56
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do controller de Obter Moeda Por Id
    ============================================================================
"""

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.controllers.obter_moeda_por_id_controller import (
    ObterMoedaPorIdController,
)


def test_obter_moeda_por_id_controller_OK():
    obj_repo = MoedasRepositorio()
    id_moeda = str(obj_repo.repo[0].id_moeda)

    obj_request = HttpRequest()
    obj_request.query_params = [{"id_moeda": id_moeda}]

    obj_use_case = ObterMoedaPorId(obj_repo)

    obj_controller = ObterMoedaPorIdController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 200
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_obter_moeda_por_id_controller_nao_localizado():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [{"id_moeda": "baf6c2c9-3e1b-4bf6-9916-a2dfb82f8d83"}]

    obj_use_case = ObterMoedaPorId(obj_repo)

    obj_controller = ObterMoedaPorIdController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 404
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))
