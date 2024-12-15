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

import pytest

from src.use_cases.moedas.manter_moedas import CriarMoeda
from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.adapters.http.mocks.http_request_moedas import HTTPRequestMoeda
from src.adapters.http.controllers.criar_moeda_controller import CriarMoedaController

from src.errors.moedas_errors import (
    MoedaSiglaJaCadastrada,
    MoedaErrosDeValidacao,
    MoedaDadosInvalidos,
)


def test_criar_moeda_controller_ok():
    obj_http_request = HTTPRequestMoeda(
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
    assert obj_response.status_code == 201


def test_criar_moeda_controller_erro_validacao():
    obj_http_request = HTTPRequestMoeda(
        headers=None,
        body=None,
        query_params={
            "sigla": "E",
            "descricao": "E",
            "tipo_de_moeda": "XXX",
            "valor_da_paridade": 123456789012.35,
        },
        path_params=None,
        url=None,
        ipv4=None,
    )
    obj_repository = MoedasRepositorio()
    obj_use_case = CriarMoeda(obj_repository)

    obj_controller = CriarMoedaController(obj_use_case)

    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        _ = obj_controller.handle(obj_http_request)
    assert msg_error.value.status_code == 422
    assert msg_error.value.message["sigla"] == ["min length is 3"]
    assert msg_error.value.message["descricao"] == ["min length is 3"]
    assert msg_error.value.message["tipo_de_moeda"] == ["unallowed value XXX"]
    assert msg_error.value.message["valor_da_paridade"] == ["max value is 1000.0"]


def test_criar_moeda_controller_erro_sigla_duplicada():
    obj_http_request = HTTPRequestMoeda(
        headers=None,
        body=None,
        query_params={
            "sigla": "Primeira Moeda",
            "descricao": "Teste de Erro de Duplicidade",
            "tipo_de_moeda": "BRL",
            "valor_da_paridade": 1.00,
        },
        path_params=None,
        url=None,
        ipv4=None,
    )
    obj_repository = MoedasRepositorio()
    obj_use_case = CriarMoeda(obj_repository)

    obj_controller = CriarMoedaController(obj_use_case)

    with pytest.raises(MoedaSiglaJaCadastrada) as msg_error:
        _ = obj_controller.handle(obj_http_request)
    assert msg_error.value.message == "Sigla da Moeda já cadastrada!"


def test_criar_moeda_controller_erro_moeda_nao_informada():
    obj_http_request = HTTPRequestMoeda(
        headers=None,
        body=None,
        query_params=None,
        path_params=None,
        url=None,
        ipv4=None,
    )
    obj_repository = MoedasRepositorio()
    obj_use_case = CriarMoeda(obj_repository)

    obj_controller = CriarMoedaController(obj_use_case)

    with pytest.raises(MoedaDadosInvalidos) as msg_error:
        _ = obj_controller.handle(obj_http_request)
    assert msg_error.value.status_code == 400
    assert msg_error.value.message == "Informe todos os dados corretamente!"
