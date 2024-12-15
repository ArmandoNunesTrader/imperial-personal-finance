#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   cartoes_de_credito_test.py
@Created :   09/12/2024 11:47:11
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste da classe Cartões de Crédito
    ============================================================================
"""

from datetime import datetime
from uuid import uuid4

import re

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.cartoes_de_credito import CartoesDeCredito

import src.utils.validate_utils as vdu


def test_create():
    obj_cartao_de_credito = CartoesDeCredito(
        sigla="VISA Mercado Livre",
        nome="Cartão Visa Internacional Mercado Livre",
        numero="1234.5678.9012.3456",
        data_de_validade="01/2030",
        melhor_dia_de_compra=8,
        dia_de_vencimento=2,
        id_moeda=uuid4(),
        _tipo_de_moeda="Euro",
        _valor_do_limite=65498.12,
    )
    obj_cartao_de_credito_clone = obj_cartao_de_credito

    assert vdu.is_valid_uuid(obj_cartao_de_credito.id_cartao_de_credito)
    assert obj_cartao_de_credito.sigla == "VISA Mercado Livre"
    assert obj_cartao_de_credito.nome == "Cartão Visa Internacional Mercado Livre"
    assert obj_cartao_de_credito.numero == "1234.5678.9012.3456"
    assert obj_cartao_de_credito.data_de_validade == "01/2030"
    assert obj_cartao_de_credito.melhor_dia_de_compra == 8
    assert obj_cartao_de_credito.dia_de_vencimento == 2
    assert vdu.is_valid_uuid(obj_cartao_de_credito.id_moeda)
    assert obj_cartao_de_credito.limite_de_credito.formatada == "€ 65,498.12"
    assert isinstance(obj_cartao_de_credito.created_at, datetime)
    assert isinstance(obj_cartao_de_credito.updated_at, datetime)
    assert str(obj_cartao_de_credito) is not None

    mask = re.compile(
        "^ID: [a-f0-9-]{36}"
        + " - Sigla: VISA Mercado Livre"
        + " - Nome: Cartão Visa Internacional Mercado Livre"
        + " - Número: 1234.5678.9012.3456"
        + " - Validade: 01/2030"
        + " - Dia de Vencimento: 02"
        + "$"
    )

    assert re.fullmatch(mask, str(obj_cartao_de_credito))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_cartao_de_credito is not None

    assert obj_cartao_de_credito == obj_cartao_de_credito_clone
    assert obj_cartao_de_credito != [obj_cartao_de_credito, obj_cartao_de_credito_clone]

    obj_cartao_de_credito = CartoesDeCredito(
        nome="Cartão Visa Internacional Mercado Livre",
        numero="1234.5678.9012.3456",
        data_de_validade="01/2030",
        melhor_dia_de_compra=8,
        dia_de_vencimento=2,
        id_moeda=uuid4(),
        sigla="VISA Mercado Livre",
        _tipo_de_moeda="Libra Esterlina",
        _valor_do_limite=65498.12,
    )

    obj_vo_moeda = VOMoeda(20000, TiposDeMoedas("Dólar Americano"))
    obj_cartao_de_credito.limite_de_credito = obj_vo_moeda
    assert obj_cartao_de_credito.limite_de_credito.formatada == "$ 20,000.00"
    assert str(obj_cartao_de_credito) is not None

    obj_cartao_de_credito._tipo_de_moeda = "Libra Esterlina"
    obj_cartao_de_credito._valor_do_limite = 20000

    assert obj_cartao_de_credito.limite_de_credito.formatada == "R$ 20.000,00"
    assert str(obj_cartao_de_credito) is not None

    obj_cartao_de_credito._valor_do_limite = "20000.00"

    assert obj_cartao_de_credito.limite_de_credito.formatada == "R$ 1,00"
    assert str(obj_cartao_de_credito) is not None

    obj_vo_moeda = VOMoeda(1254, TiposDeMoedas.EUR)
    obj_cartao_de_credito.limite_de_credito = obj_vo_moeda
    assert obj_cartao_de_credito.limite_de_credito.formatada == "€ 1,254.00"
    assert str(obj_cartao_de_credito) is not None
