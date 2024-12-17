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
    obj_4 = CategoriasDeContas(CategoriasDeContas.FINANCIAMENTO)

    assert obj_1.value == "Receita"
    assert obj_2.value == "Despesa"
    assert obj_3.value == "Investimento"
    assert obj_4.value == "Financiamento"
    assert obj_1.value_to_name("Receita") == "RECEITA"
    assert obj_2.value_to_name("Despesa") == "DESPESA"
    assert obj_3.value_to_name("Investimento") == "INVESTIMENTO"
    assert obj_4.value_to_name("Financiamento") == "FINANCIAMENTO"
    assert CategoriasDeContas["RECEITA"] is CategoriasDeContas.RECEITA
    assert CategoriasDeContas["DESPESA"] is CategoriasDeContas.DESPESA
    assert CategoriasDeContas["INVESTIMENTO"] is CategoriasDeContas.INVESTIMENTO
    assert CategoriasDeContas["FINANCIAMENTO"] is CategoriasDeContas.FINANCIAMENTO
    assert CategoriasDeContas("Receita") is CategoriasDeContas.RECEITA
    assert CategoriasDeContas("Despesa") is CategoriasDeContas.DESPESA
    assert CategoriasDeContas("Investimento") is CategoriasDeContas.INVESTIMENTO
    assert CategoriasDeContas("Financiamento") is CategoriasDeContas.FINANCIAMENTO

    assert CategoriasDeContas.all_names() == [
        "RECEITA",
        "DESPESA",
        "INVESTIMENTO",
        "FINANCIAMENTO",
    ]
    assert CategoriasDeContas.all_values() == [
        "Receita",
        "Despesa",
        "Investimento",
        "Financiamento",
    ]
