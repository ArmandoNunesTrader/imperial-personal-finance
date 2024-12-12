#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   categorias_de_contas_test.py
@Created :   07/12/2024 15:58:23
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do enum Categorias de Contas
    ============================================================================
"""

from src.domain.enums.categorias_de_contas import CategoriasDeContas


def test_create():
    obj_1 = CategoriasDeContas(CategoriasDeContas.RECEITA)
    obj_2 = CategoriasDeContas(CategoriasDeContas.DESPESA)
    obj_3 = CategoriasDeContas(CategoriasDeContas.INVESTIMENTO)

    assert obj_1.value == "Receita"
    assert obj_2.value == "Despesa"
    assert obj_3.value == "Investimento"
    assert obj_1.value_to_name("Receita") == "RECEITA"
    assert obj_2.value_to_name("Despesa") == "DESPESA"
    assert obj_3.value_to_name("Investimento") == "INVESTIMENTO"
    assert CategoriasDeContas["RECEITA"] is CategoriasDeContas.RECEITA
    assert CategoriasDeContas["DESPESA"] is CategoriasDeContas.DESPESA
    assert CategoriasDeContas["INVESTIMENTO"] is CategoriasDeContas.INVESTIMENTO
    assert CategoriasDeContas("Receita") is CategoriasDeContas.RECEITA
    assert CategoriasDeContas("Despesa") is CategoriasDeContas.DESPESA
    assert CategoriasDeContas("Investimento") is CategoriasDeContas.INVESTIMENTO

    assert CategoriasDeContas.all_names() == [
        "RECEITA",
        "DESPESA",
        "INVESTIMENTO",
    ]
    assert CategoriasDeContas.all_values() == [
        "Receita",
        "Despesa",
        "Investimento",
    ]
