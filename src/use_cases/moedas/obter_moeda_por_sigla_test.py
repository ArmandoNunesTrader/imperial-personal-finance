#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_sigla_test.py
@Created :   12/12/2024 10:43:54
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do caso de uso Obter Moeda por Sigla
    ============================================================================
"""

import pytest

from src.errors.moedas_errors import (
    MoedaErrosDeValidacao,
    MoedaSiglaNaoInformada,
    MoedaSiglaNaoLocalizada,
)

from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_moeda_por_sigla import ObterMoedaPorSigla

obj_repo = MoedasRepositorio()
for reg in obj_repo.repo:
    sigla = reg.sigla
    obj_sigla_1 = reg
    break

obj_dto_erro_1 = MoedaDTOIn().from_dict({"sigla": "Não Localizada"})
obj_dto_erro_2 = MoedaDTOIn().from_dict({"sigla": "A"})
obj_dto_erro_3 = MoedaDTOIn().from_dict({"sigla": 123.45})


def test_obter_moeda_por_sigla_erro_validacao():
    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        ObterMoedaPorSigla(obj_repo).execute(obj_dto_erro_2)
    assert msg_error.value.message != ""


def test_obter_moeda_por_sigla_erro_nao_informada():
    with pytest.raises(MoedaSiglaNaoInformada) as msg_error:
        ObterMoedaPorSigla(obj_repo).execute(obj_dto_erro_3)
    assert msg_error.value.message == "Sigla da Moeda não informada!"


def test_obter_moeda_por_sigla_erro_nao_localizada():
    with pytest.raises(MoedaSiglaNaoLocalizada) as msg_error:
        ObterMoedaPorSigla(obj_repo).execute(obj_dto_erro_1)
    assert msg_error.value.message == "Sigla da Moeda não localizada!"
