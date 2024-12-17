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

from src.use_cases.dtos.dto_moedas import MoedaDTOIn

import src.utils.sanitize_utils as fsn


def test_dto_moedas_in():
    dict_1 = {
        "sigla": fsn.sanitize_pt_br_phrase_capitalize("Sigla Moeda"),
        "descricao": fsn.sanitize_pt_br_phrase_capitalize("Descrição Moeda de Testes"),
        "_tipo_de_moeda": fsn.sanitize_pt_br_phrase_upper("BRL"),
        "_valor_da_paridade": 1.00,
    }
    dict_1_out = {
        "sigla": fsn.sanitize_pt_br_phrase_capitalize("Sigla Moeda"),
        "descricao": fsn.sanitize_pt_br_phrase_capitalize("Descrição Moeda de Testes"),
        "_tipo_de_moeda": fsn.sanitize_pt_br_phrase_upper("BRL"),
        "_valor_da_paridade": 1.00,
    }
    obj_1 = MoedaDTOIn().from_dict(dict_1)

    dict_2 = {
        "id_moeda": fsn.sanitize_uuid("293a6e26-5904-41e9-bdd0-c064b420e920"),
        "sigla": fsn.sanitize_pt_br_phrase_capitalize("Sigla Moeda"),
        "descricao": fsn.sanitize_pt_br_phrase_capitalize("Descrição Moeda de Testes"),
        "_tipo_de_moeda": fsn.sanitize_pt_br_phrase_upper("BRL"),
        "_valor_da_paridade": 1.00,
    }
    obj_2 = MoedaDTOIn().from_dict(dict_2)

    dict_3 = {
        "id_moeda": fsn.sanitize_uuid("293a6e26-5904-41e9-bdd0-c064b420e920"),
    }
    dict_3_out = {
        "id_moeda": fsn.sanitize_uuid("293a6e26-5904-41e9-bdd0-c064b420e920"),
        "sigla": None,
        "descricao": None,
        "_tipo_de_moeda": None,
        "_valor_da_paridade": None,
    }
    obj_3 = MoedaDTOIn().from_dict(dict_3)

    assert obj_1.sigla == "Sigla Moeda"
    assert obj_1.descricao == "Descrição Moeda de Testes"
    assert obj_1._tipo_de_moeda == "BRL"
    assert obj_1._valor_da_paridade == 1.00
    assert obj_1.to_dict() == dict_1_out

    assert obj_2.id_moeda == "293a6e26-5904-41e9-bdd0-c064b420e920"
    assert obj_2.sigla == "Sigla Moeda"
    assert obj_2.descricao == "Descrição Moeda de Testes"
    assert obj_2._tipo_de_moeda == "BRL"
    assert obj_2._valor_da_paridade == 1.00
    assert obj_2.to_dict() == dict_2

    assert obj_3.id_moeda == "293a6e26-5904-41e9-bdd0-c064b420e920"
    assert obj_3.to_dict() == dict_3_out
