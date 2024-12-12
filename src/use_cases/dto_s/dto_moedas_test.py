#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   dto_moedas_test.py
@Created :   11/12/2024 14:38:51
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de testes dos DTO's de Moedas
    ============================================================================
"""

from src.use_cases.dto_s.dto_moedas import MoedaDTOIn


def test_dto_moedas_in():
    dict_1 = {
        "sigla": "Sigla Moeda",
        "descricao": "Descrição Moeda 1",
        "tipo_de_moeda": "BRL",
        "valor_da_paridade": 1.00,
    }
    obj_1 = MoedaDTOIn().from_dict(dict_1)

    assert obj_1.sigla == "Sigla Moeda"
    assert obj_1.descricao == "Descrição Moeda 1"
    assert obj_1.tipo_de_moeda == "BRL"
    assert obj_1.valor_da_paridade == 1.00
    assert obj_1.to_dict() == dict_1
