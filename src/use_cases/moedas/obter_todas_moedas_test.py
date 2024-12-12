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

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.moedas.obter_todas_moedas import ObterTodasAsMoedas

obj_repo = MoedasRepositorio()
for ind, reg in obj_repo.repo[0].items():
    sigla = reg.sigla
    obj_moeda_1 = reg
    break


def test_obter_todas_as_moedas():
    list_moedas = ObterTodasAsMoedas(obj_repo).execute()

    assert list_moedas is not None
    assert list_moedas[0] == obj_moeda_1
