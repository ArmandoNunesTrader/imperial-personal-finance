#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tipos_de_moedas_test.py
@Created :   07/12/2024 17:00:15
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do enum Tipos de Moedas
    ============================================================================
"""

from src.domain.enums.tipos_de_moedas import TiposDeMoedas


def test_create():
    obj_1 = TiposDeMoedas(TiposDeMoedas.BRL)
    obj_2 = TiposDeMoedas(TiposDeMoedas.USD)
    obj_3 = TiposDeMoedas(TiposDeMoedas.EUR)

    assert obj_1.value == "Real Brasileiro"
    assert obj_2.value == "Dólar Americano"
    assert obj_3.value == "Euro"
    assert obj_1.name("Real Brasileiro") == "BRL"
    assert obj_2.name("Dólar Americano") == "USD"
    assert obj_3.name("Euro") == "EUR"
    assert TiposDeMoedas["BRL"] is TiposDeMoedas.BRL
    assert TiposDeMoedas["USD"] is TiposDeMoedas.USD
    assert TiposDeMoedas["EUR"] is TiposDeMoedas.EUR
    assert TiposDeMoedas("Real Brasileiro") is TiposDeMoedas.BRL
    assert TiposDeMoedas("Dólar Americano") is TiposDeMoedas.USD
    assert TiposDeMoedas("Euro") is TiposDeMoedas.EUR
