#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_todas_moedas_controller_test.py
@Created :   17/12/2024 14:43:01
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do controller de Obter Todas as Moedas
    ============================================================================
"""

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_todas_moedas import ObterTodasAsMoedas
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.controllers.obter_todas_moedas_controller import (
    ObterTodasAsMoedasController,
)


def test_obter_todas_as_moedas_ok():
    obj_repo = MoedasRepositorio()

    obj_request = HttpRequest()

    obj_use_case = ObterTodasAsMoedas(obj_repo)

    obj_controller = ObterTodasAsMoedasController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 200
    assert str(obj_response.body) is not None

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))


def test_obter_todas_as_moedas_vazio():
    obj_repo = MoedasRepositorio()
    obj_repo.repo = []

    obj_request = HttpRequest()

    obj_use_case = ObterTodasAsMoedas(obj_repo)

    obj_controller = ObterTodasAsMoedasController(obj_use_case)

    obj_response = obj_controller.handle(obj_request)

    assert obj_response.status_code == 404
    assert (
        str(obj_response.body[0]["errors"][0]["detail"])
        == "Não existem Moedas cadastradas!"
    )

    # Descomentar a linha abaixo para ver o conteúdo
    # print(obj_response.status_code)
    # print(str(obj_response.body))
