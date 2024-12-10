#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moeda_test.py
@Created :   07/12/2024 17:25:19
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do value object Moeda
    ============================================================================
"""

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda


def test_create():
    obj_1 = VOMoeda()
    obj_2 = VOMoeda(2.58, TiposDeMoedas.USD)
    obj_3 = VOMoeda(67587.98, TiposDeMoedas.EUR)
    obj_4 = VOMoeda(5478.00, TiposDeMoedas("Dólar Americano"))
    obj_5 = VOMoeda(12547892.58, TiposDeMoedas["BRL"])

    assert obj_1.tipo_de_moeda is TiposDeMoedas.BRL
    assert obj_1.valor == 1.00
    assert obj_1.formatada == "R$ 1,00"
    assert obj_2.tipo_de_moeda is TiposDeMoedas.USD
    assert obj_2.valor == 2.58
    assert obj_2.formatada == "$ 2.58"
    assert obj_3.tipo_de_moeda is TiposDeMoedas.EUR
    assert obj_3.valor == 67587.98
    assert obj_3.formatada == "€ 67,587.98"
    assert obj_4.tipo_de_moeda is TiposDeMoedas.USD
    assert obj_4.valor == 5478.00
    assert obj_4.formatada == "$ 5,478.00"
    assert obj_5.tipo_de_moeda is TiposDeMoedas.BRL
    assert obj_5.valor == 12547892.58
    assert obj_5.formatada == "R$ 12.547.892,58"
