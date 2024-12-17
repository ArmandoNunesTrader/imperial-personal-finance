#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_todas_moedas_test.py
@Created :   12/12/2024 12:04:20
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do caso de uso Obter Todas as Moedas
    ============================================================================
"""

import pytest

from src.errors.moedas_errors import MoedaNotFound
from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_todas_moedas import ObterTodasAsMoedas

obj_repo = MoedasRepositorio()
for reg in obj_repo.repo:
    obj_moeda_1 = reg
    break

obj_repo_clean = MoedasRepositorio()
obj_repo_clean.repo = []


def test_obter_todas_as_moedas_ok():
    list_moedas = ObterTodasAsMoedas(obj_repo).execute()

    assert list_moedas is not None
    assert list_moedas[0] == obj_moeda_1

    # Retirar os comentários para visualizar o objeto retornado
    # print()
    # print(str(obj_moeda_1))


def test_obter_todas_as_moedas_erro():
    with pytest.raises(MoedaNotFound) as msg_error:
        ObterTodasAsMoedas(obj_repo_clean).execute()
    assert msg_error.value.message == "Não existem Moedas cadastradas!"
