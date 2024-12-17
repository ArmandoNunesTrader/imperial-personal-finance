#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_presenters_test.py
@Created :   13/12/2024 13:09:19
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste dos Presenters da Entidade Moedas
    ============================================================================
"""
from src.domain.entities.moedas import Moedas
from src.adapters.http.presenters.moedas_presenters import (
    moedas_presenter_one,
    moedas_presenter_all,
)


def test_moedas_presenter_one():
    obj_moeda_ok = Moedas("Teste", "Moeda   de Teste", "EUR", 7.89)
    obj_presenter_1 = moedas_presenter_one(obj_moeda_ok)

    assert obj_presenter_1 is not None
    assert obj_presenter_1.status_code == 200
    assert obj_presenter_1.body is not None

    obj_presenter_2 = moedas_presenter_one(None)
    assert obj_presenter_2 is not None
    assert obj_presenter_2.status_code == 500
    assert (
        obj_presenter_2.body["message"] == "Ocorreu um erro desconhecido no servidor!"
    )

    obj_erro = {
        "status_code": 404,
        "body": {"errors": [{"title": "Bad Request", "detail": "Erro detectado!"}]},
    }
    obj_presenter_3 = moedas_presenter_one(obj_erro)
    assert obj_presenter_3 is not None
    assert obj_presenter_3.status_code == 404
    assert obj_presenter_3.body["message"]["errors"][0]["detail"] == "Erro detectado!"


def test_moedas_presenter_all():
    obj_moeda_1_ok = Moedas("Teste One", "Moeda de Teste One", "EUR", 7.89)
    obj_moeda_2_ok = Moedas("Teste Two", "Moeda de Teste Two", "USD", 12.34)
    obj_moeda_3_ok = Moedas("Teste Three", "Moeda de Teste Three", "BRL", 5.67)
    list_obj = []
    list_obj.append(obj_moeda_1_ok)
    list_obj.append(obj_moeda_2_ok)
    list_obj.append(obj_moeda_3_ok)
    obj_presenter_1 = moedas_presenter_all(list_obj)

    assert obj_presenter_1 is not None
    assert obj_presenter_1.status_code == 200
    assert obj_presenter_1.body is not None

    obj_presenter_2 = moedas_presenter_all(None, 500)
    assert obj_presenter_2 is not None
    assert obj_presenter_2.status_code == 500
    assert obj_presenter_2.body["message"] != ""
