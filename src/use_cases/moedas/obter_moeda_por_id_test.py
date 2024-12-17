#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_id_test.py
@Created :   12/12/2024 10:43:54
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do caso de uso Obter Moeda por Id
    ============================================================================
"""

import pytest

from src.errors.moedas_errors import (
    MoedaErrosDeValidacao,
    MoedaIdNaoInformado,
)

from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId

obj_repo = MoedasRepositorio()
for reg in obj_repo.repo:
    id_moeda = reg.id_moeda
    obj_moeda_1 = reg
    break

obj_dto_ok = MoedaDTOIn().from_dict({"id_moeda": str(id_moeda)})
obj_dto_erro_1 = MoedaDTOIn().from_dict(
    {"id_moeda": "9d06fc00-c162-439e-a559-1e6a495fdbbe"}
)
obj_dto_erro_2 = MoedaDTOIn().from_dict({"id_moeda": 123.45})
obj_dto_erro_3 = MoedaDTOIn().from_dict({})


def test_obter_moeda_por_id_moeda_ok():
    obj_moeda = ObterMoedaPorId(obj_repo).execute(obj_dto_ok)

    assert obj_moeda is not None
    assert obj_moeda == obj_moeda_1


def test_obter_moeda_por_id_moeda_erro_validacao():
    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        ObterMoedaPorId(obj_repo).execute(obj_dto_erro_2)
    assert msg_error.value.message != ""


def test_obter_moeda_por_id_moeda_erro_nao_informada():
    with pytest.raises(MoedaIdNaoInformado) as msg_error:
        ObterMoedaPorId(obj_repo).execute(obj_dto_erro_3)
    assert msg_error.value.message == "Identificador da Moeda não informado!"


def test_obter_moeda_por_id_moeda_erro_nao_localizada():
    assert ObterMoedaPorId(obj_repo).execute(obj_dto_erro_1) is False
