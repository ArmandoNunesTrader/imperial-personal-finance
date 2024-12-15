#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_id_test.py
@Created :   11/12/2024 19:43:53
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do caso de uso Obter Moeda por ID
    ============================================================================
"""

import pytest

from src.errors.moedas_errors import MoedaIdNaoInformado
from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId

obj_repo = MoedasRepositorio()
for ind, reg in obj_repo.repo[0].items():
    id_moeda = reg.id_moeda
    obj_moeda_1 = reg
    break


def test_obter_moeda_por_id():
    obj_moeda = ObterMoedaPorId(obj_repo).execute(id_moeda)

    assert obj_moeda is not None
    assert obj_moeda == obj_moeda_1

    with pytest.raises(MoedaIdNaoInformado) as msg_error:
        ObterMoedaPorId(obj_repo).execute(None)
    assert msg_error.value.message == "Identificador da Moeda informado não é válido!"

    with pytest.raises(MoedaIdNaoInformado) as msg_error:
        ObterMoedaPorId(obj_repo).execute("UUID_INVALIDA")
    assert msg_error.value.message == "Identificador da Moeda informado não é válido!"
