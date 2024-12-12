#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   situacoes_dos_lancamentos_test.py
@Created :   07/12/2024 16:24:28
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste do enum Situações dos lançamentos
    ============================================================================
"""

from src.domain.enums.situacoes_dos_lancamentos import SituacoesDosLancamentos


def test_create():
    obj_1 = SituacoesDosLancamentos(SituacoesDosLancamentos.RECEBIDO)
    obj_2 = SituacoesDosLancamentos(SituacoesDosLancamentos.PAGO)
    obj_3 = SituacoesDosLancamentos(SituacoesDosLancamentos.A_RECEBER)
    obj_4 = SituacoesDosLancamentos(SituacoesDosLancamentos.A_PAGAR)

    assert obj_1.value == "Recebido"
    assert obj_2.value == "Pago"
    assert obj_3.value == "A Receber"
    assert obj_4.value == "A Pagar"
    assert obj_1.value_to_name("Recebido") == "RECEBIDO"
    assert obj_2.value_to_name("Pago") == "PAGO"
    assert obj_3.value_to_name("A Receber") == "A_RECEBER"
    assert obj_4.value_to_name("A Pagar") == "A_PAGAR"
    assert SituacoesDosLancamentos["RECEBIDO"] is SituacoesDosLancamentos.RECEBIDO
    assert SituacoesDosLancamentos["PAGO"] is SituacoesDosLancamentos.PAGO
    assert SituacoesDosLancamentos["A_RECEBER"] is SituacoesDosLancamentos.A_RECEBER
    assert SituacoesDosLancamentos["A_PAGAR"] is SituacoesDosLancamentos.A_PAGAR
    assert SituacoesDosLancamentos("Recebido") is SituacoesDosLancamentos.RECEBIDO
    assert SituacoesDosLancamentos("Pago") is SituacoesDosLancamentos.PAGO
    assert SituacoesDosLancamentos("A Receber") is SituacoesDosLancamentos.A_RECEBER
    assert SituacoesDosLancamentos("A Pagar") is SituacoesDosLancamentos.A_PAGAR

    assert SituacoesDosLancamentos.all_names() == [
        "RECEBIDO",
        "PAGO",
        "A_RECEBER",
        "A_PAGAR",
    ]
    assert SituacoesDosLancamentos.all_values() == [
        "Recebido",
        "Pago",
        "A Receber",
        "A Pagar",
    ]
