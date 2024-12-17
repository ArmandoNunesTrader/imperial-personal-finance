#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_sigla_controller_test.py
@Created :   16/12/2024 22:34:56
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do controller de Obter Moeda Por Sigla
    ============================================================================
"""

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_moeda_por_sigla import ObterMoedaPorSigla
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.controllers.obter_moeda_por_id_controller import (
    ObterMoedaPorIdController,
)


def test_obter_moeda_por_sigla_controller_ok():
    obj_repo = MoedasRepositorio()
    sigla = str(obj_repo.repo[0].sigla)

    obj_request = HttpRequest()
    obj_request.query_params = [{"sigla": sigla}]

    obj_use_case = ObterMoedaPorSigla(obj_repo)

    obj_controller = ObterMoedaPorIdController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 200
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_obter_moeda_por_sigla_controller_nao_localizado():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [{"sigla": "Alfa Beta"}]

    obj_use_case = ObterMoedaPorSigla(obj_repo)

    obj_controller = ObterMoedaPorIdController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 404
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_obter_moeda_por_sigla_controller_erro():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()
    obj_request.query_params = [{"sigla": "Teste Com Longos Tamanhos e Etc"}]

    obj_use_case = ObterMoedaPorSigla(obj_repo)

    obj_controller = ObterMoedaPorIdController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 422
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))
