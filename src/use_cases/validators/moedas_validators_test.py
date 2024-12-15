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
import pytest

from src.errors.moedas_errors import MoedaErrosDeValidacao
from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.use_cases.validators.moedas_validators import (
    moedas_dto_in_validator,
)


def test_moeda_validators_ok():
    obj_1 = MoedaDTOIn().from_dict(
        {
            "id_moeda": "d4004b05-268d-4e01-9b46-0bca3f1c06b2",
            "sigla": "Testes",
            "descricao": "Moeda de Testes",
            "tipo_de_moeda": "USD",
            "valor_da_paridade": 5.46,
        }
    )

    assert moedas_dto_in_validator(obj_1) is None


def test_moeda_validators_errors():
    obj_1 = MoedaDTOIn().from_dict(
        {
            "id_moeda": "6af83914-40a7-Xdc1-a0c9-27670b679836",
            "sigla": "M",
            "descricao": "M",
            "tipo_de_moeda": "XXX",
            "valor_da_paridade": -1,
        }
    )

    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        moedas_dto_in_validator(obj_1)
    assert msg_error.value.message != ""

    obj_2 = MoedaDTOIn().from_dict(
        {
            "sigla": "M123456 789 123456789 123456789 123456789 123456789 ",
            "descricao": "M123456789 123456789 123456789 123456789 123456789 123456789 ",  # noqa E501
            "tipo_de_moeda": "XXX",
            "valor_da_paridade": 100000,
        }
    )

    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        moedas_dto_in_validator(obj_2)
    assert msg_error.value.message != ""
