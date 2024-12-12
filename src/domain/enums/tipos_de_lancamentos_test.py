#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tipos_de_lancamentos_test.py
@Created :   07/12/2024 16:44:43
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do enum Tipos de Lançamentos
    ============================================================================
"""

from src.domain.enums.tipos_de_lancamentos import TiposDeLancamentos


def test_create():
    obj_1 = TiposDeLancamentos(TiposDeLancamentos.RECEITA)
    obj_2 = TiposDeLancamentos(TiposDeLancamentos.DESPESA)
    obj_3 = TiposDeLancamentos(TiposDeLancamentos.INVESTIMENTO)
    obj_4 = TiposDeLancamentos(TiposDeLancamentos.OUTRO)

    assert obj_1.value == "Lançamento de Receita"
    assert obj_2.value == "Lançamento de Despesa"
    assert obj_3.value == "Lançamento de Investimento"
    assert obj_4.value == "Outro Lançamento"
    assert obj_1.value_to_name("Lançamento de Receita") == "RECEITA"
    assert obj_2.value_to_name("Lançamento de Despesa") == "DESPESA"
    assert obj_3.value_to_name("Lançamento de Investimento") == "INVESTIMENTO"
    assert obj_4.value_to_name("Outro Lançamento") == "OUTRO"
    assert TiposDeLancamentos["RECEITA"] is TiposDeLancamentos.RECEITA
    assert TiposDeLancamentos["DESPESA"] is TiposDeLancamentos.DESPESA
    assert TiposDeLancamentos["INVESTIMENTO"] is TiposDeLancamentos.INVESTIMENTO
    assert TiposDeLancamentos["OUTRO"] is TiposDeLancamentos.OUTRO
    assert TiposDeLancamentos("Lançamento de Receita") is TiposDeLancamentos.RECEITA
    assert TiposDeLancamentos("Lançamento de Despesa") is TiposDeLancamentos.DESPESA
    assert (
        TiposDeLancamentos("Lançamento de Investimento")
        is TiposDeLancamentos.INVESTIMENTO
    )
    assert TiposDeLancamentos("Outro Lançamento") is TiposDeLancamentos.OUTRO

    assert TiposDeLancamentos.all_names() == [
        "RECEITA",
        "DESPESA",
        "INVESTIMENTO",
        "OUTRO",
    ]
    assert TiposDeLancamentos.all_values() == [
        "Lançamento de Receita",
        "Lançamento de Despesa",
        "Lançamento de Investimento",
        "Outro Lançamento",
    ]
