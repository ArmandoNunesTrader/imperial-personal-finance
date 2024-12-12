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

import src.utils.sanitize_utils as fsn


def test_dto_moedas_in():
    dict_1 = {
        "sigla": fsn.sanitize_pt_br_phrase("Sigla Moeda"),
        "descricao": fsn.sanitize_pt_br_phrase("Descrição Moeda de Testes"),
        "tipo_de_moeda": fsn.sanitize_pt_br_phrase("BRL").upper(),
        "valor_da_paridade": 1.00,
    }
    obj_1 = MoedaDTOIn().from_dict(dict_1)

    assert obj_1.sigla == "Sigla Moeda"
    assert obj_1.descricao == "Descrição Moeda de Testes"
    assert obj_1.tipo_de_moeda == "BRL"
    assert obj_1.valor_da_paridade == 1.00
    assert obj_1.to_dict() == dict_1
