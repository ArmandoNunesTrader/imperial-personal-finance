#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   grupos_de_contas_test.py
@Created :   07/12/2024 16:17:27
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do enum Grupos de Contas
    ============================================================================
"""

from src.domain.enums.grupos_de_contas import GruposDeContas


def test_create():
    obj_1 = GruposDeContas(GruposDeContas.ATIVO)
    obj_2 = GruposDeContas(GruposDeContas.PASSIVO)
    obj_3 = GruposDeContas(GruposDeContas.RESULTADO)

    assert obj_1.value == "1-Ativo"
    assert obj_2.value == "2-Passivo"
    assert obj_3.value == "3-Resultado"
    assert obj_1.value_to_name("1-Ativo") == "ATIVO"
    assert obj_2.value_to_name("2-Passivo") == "PASSIVO"
    assert obj_3.value_to_name("3-Resultado") == "RESULTADO"
    assert GruposDeContas["ATIVO"] is GruposDeContas.ATIVO
    assert GruposDeContas["PASSIVO"] is GruposDeContas.PASSIVO
    assert GruposDeContas["RESULTADO"] is GruposDeContas.RESULTADO
    assert GruposDeContas("1-Ativo") is GruposDeContas.ATIVO
    assert GruposDeContas("2-Passivo") is GruposDeContas.PASSIVO
    assert GruposDeContas("3-Resultado") is GruposDeContas.RESULTADO

    assert GruposDeContas.all_names() == [
        "ATIVO",
        "PASSIVO",
        "RESULTADO",
    ]
    assert GruposDeContas.all_values() == [
        "1-Ativo",
        "2-Passivo",
        "3-Resultado",
    ]
