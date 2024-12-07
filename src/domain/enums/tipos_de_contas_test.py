#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   tipos_de_contas_test.py
@Created :   07/12/2024 16:39:25
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do enum Tipos de Contas
    ============================================================================
"""

from src.domain.enums.tipos_de_contas import TiposDeContas


def test_create():
    obj_1 = TiposDeContas(TiposDeContas.ATIVO)
    obj_2 = TiposDeContas(TiposDeContas.BANCO)
    obj_3 = TiposDeContas(TiposDeContas.INVESTIMENTO)
    obj_4 = TiposDeContas(TiposDeContas.CAIXA)

    assert obj_1.value == "Conta de Ativo"
    assert obj_2.value == "Conta Corrente Bancária"
    assert obj_3.value == "Conta de Investimento"
    assert obj_4.value == "Conta Caixa"
    assert obj_1.name("Conta de Ativo") == "ATIVO"
    assert obj_2.name("Conta Corrente Bancária") == "BANCO"
    assert obj_3.name("Conta de Investimento") == "INVESTIMENTO"
    assert obj_4.name("Conta Caixa") == "CAIXA"
    assert TiposDeContas["ATIVO"] is TiposDeContas.ATIVO
    assert TiposDeContas["BANCO"] is TiposDeContas.BANCO
    assert TiposDeContas["INVESTIMENTO"] is TiposDeContas.INVESTIMENTO
    assert TiposDeContas["CAIXA"] is TiposDeContas.CAIXA
    assert TiposDeContas("Conta de Ativo") is TiposDeContas.ATIVO
    assert TiposDeContas("Conta Corrente Bancária") is TiposDeContas.BANCO
    assert TiposDeContas("Conta de Investimento") is TiposDeContas.INVESTIMENTO
    assert TiposDeContas("Conta Caixa") is TiposDeContas.CAIXA
