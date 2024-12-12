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

from src.errors.moedas_errors import MoedaSiglaNaoInformada

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_moeda_por_sigla import ObterMoedaPorSigla

obj_repo = MoedasRepositorio()
for ind, reg in obj_repo.repo[0].items():
    sigla = reg.sigla
    obj_moeda_1 = reg
    break


def test_obter_moeda_por_sigla():
    obj_moeda = ObterMoedaPorSigla(obj_repo).execute(sigla)

    assert obj_moeda is not None
    assert obj_moeda == obj_moeda_1

    with pytest.raises(MoedaSiglaNaoInformada) as msg_error:
        ObterMoedaPorSigla(obj_repo).execute(None)
    assert msg_error.value.message == "Sigla da Moeda não informada!"

    obj_moeda = ObterMoedaPorSigla(obj_repo).execute("Não Localizado")

    assert obj_moeda is None

    with pytest.raises(MoedaSiglaNaoInformada) as msg_error:
        ObterMoedaPorSigla(obj_repo).execute(125.54)
    assert msg_error.value.message == "Sigla da Moeda informado não é válida!"
