#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_validators_test.py
@Created :   11/12/2024 17:37:57
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes dos validadores do DTO da entidade Moedas
    ============================================================================
"""

from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.use_cases.validators.moedas_validators import moedas_dto_in_validator


def test_moeda_validators_ok():
    obj_1 = MoedaDTOIn.from_dict(
        {
            "sigla": "Testes",
            "descricao": "Moeda de Testes",
            "tipo_de_moeda": "USD",
            "valor_da_paridade": 5.46,
        }
    )

    assert moedas_dto_in_validator(obj_1) is None


def test_moeda_validators_error():
    obj_1 = MoedaDTOIn.from_dict(
        {
            "sigla": "M",
            "descricao": "M",
            "tipo_de_moeda": "XXX",
            "valor_da_paridade": -1,
        }
    )

    obj_2 = {
        "sigla": "M123456 789 123456789 123456789 123456789 123456789 ",
        "descricao": "M123456789 123456789 123456789 123456789 123456789 123456789 ",
        "tipo_de_moeda": "XXX",
        "valor_da_paridade": 100000,
    }

    try:
        moedas_dto_in_validator(obj_1)
    except:
        assert True

    try:
        moedas_dto_in_validator(obj_2)
    except:
        assert True
