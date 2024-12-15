#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_test.py
@Created :   07/12/2024 17:45:00
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste da classe Moedas
    ============================================================================
"""

from datetime import datetime

import re

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.moedas import Moedas

import src.utils.validate_utils as vdu


def test_create():
    obj_moeda_1 = Moedas(
        sigla="Moeda",
        descricao="Moeda de Teste",
        _tipo_de_moeda="Dólar Americano",
        _valor_da_paridade=5.67,
    )
    obj_moeda_2 = Moedas(
        sigla="Moeda",
        descricao="Moeda de Teste",
    )
    obj_moeda_1_clone = obj_moeda_1

    assert vdu.is_valid_uuid(obj_moeda_1.id_moeda)
    assert obj_moeda_1.sigla == "Moeda"
    assert obj_moeda_1.descricao == "Moeda de Teste"
    assert obj_moeda_1.paridade_com_real_brasileiro.formatada == "$ 5.67"
    assert isinstance(obj_moeda_1.created_at, datetime)
    assert isinstance(obj_moeda_1.updated_at, datetime)
    assert str(obj_moeda_1) is not None

    mask = re.compile("^ID: [a-f0-9-]{36} - Sigla: Moeda - Descrição: Moeda de Teste$")

    assert re.fullmatch(mask, str(obj_moeda_1))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_moeda_1 is not None

    assert obj_moeda_1 == obj_moeda_1_clone
    assert obj_moeda_1 != obj_moeda_2

    # Valida criação dos valores default do Value Object
    assert obj_moeda_2._tipo_de_moeda == "Real Brasileiro"
    assert obj_moeda_2._valor_da_paridade == 1.00
    assert obj_moeda_2.paridade_com_real_brasileiro.formatada == "R$ 1,00"

    assert obj_moeda_2 != [obj_moeda_2, obj_moeda_2]

    obj_moeda_2._tipo_de_moeda = "Libra Esterlina"
    obj_moeda_2._valor_da_paridade = 20000

    assert obj_moeda_2.paridade_com_real_brasileiro.formatada == "R$ 20.000,00"
    assert str(obj_moeda_2) is not None

    obj_moeda_2._valor_da_paridade = "20000.00"

    assert obj_moeda_2.paridade_com_real_brasileiro.formatada == "R$ 1,00"
    assert str(obj_moeda_2) is not None

    obj_vo_moeda = VOMoeda(1254, TiposDeMoedas.EUR)
    obj_moeda_2.paridade_com_real_brasileiro = obj_vo_moeda
    assert obj_moeda_2.paridade_com_real_brasileiro.formatada == "€ 1,254.00"
    assert str(obj_moeda_2) is not None
