#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   contas_test.py
@Created :   08/12/2024 14:30:34
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste da classe Contas
    ============================================================================
"""

from datetime import datetime
from uuid import uuid4

import re

from src.domain.enums.tipos_de_contas import TiposDeContas
from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.contas import Contas

import src.utils.validate_utils as vdu


def test_create():
    obj_conta = Contas(
        sigla="Caixa",
        descricao="Dinheiro em Espécie",
        id_moeda=uuid4(),
        _tipo_de_moeda="Euro",
        _saldo_de_abertura=254.89,
        _tipo_de_conta="Conta Caixa",
    )

    assert vdu.is_valid_uuid(obj_conta.id_conta)
    assert obj_conta.sigla == "Caixa"
    assert obj_conta.descricao == "Dinheiro em Espécie"
    assert obj_conta.saldo_de_abertura.formatada == "€ 254.89"
    assert vdu.is_valid_uuid(obj_conta.id_moeda)
    assert isinstance(obj_conta.created_at, datetime)
    assert isinstance(obj_conta.updated_at, datetime)
    assert str(obj_conta) is not None

    mask = re.compile(
        "^ID: [a-f0-9-]{36} - Sigla: Caixa - Descrição: Dinheiro em Espécie - Saldo de Abertura: € 254.89$"  # noqa E501
    )

    assert re.fullmatch(mask, str(obj_conta))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_conta is not None

    assert obj_conta != [obj_conta, obj_conta]

    obj_conta._tipo_de_moeda = "Libra Esterlina"
    obj_conta._saldo_de_abertura = 20000

    assert obj_conta.saldo_de_abertura.formatada == "R$ 20.000,00"
    assert str(obj_conta) is not None

    obj_conta._saldo_de_abertura = "20000.00"

    obj_conta_clone = obj_conta

    assert obj_conta.saldo_de_abertura.formatada == "R$ 1,00"
    assert str(obj_conta) is not None

    obj_vo_moeda = VOMoeda(1254, TiposDeMoedas.EUR)
    obj_conta.saldo_de_abertura = obj_vo_moeda
    assert obj_conta.saldo_de_abertura.formatada == "€ 1,254.00"
    assert str(obj_conta) is not None

    obj_conta._tipo_de_conta = "Conta Teste"
    assert obj_conta.tipo_de_conta.value == "Conta de Ativo"

    obj_conta._tipo_de_conta = "Conta Caixa"
    assert obj_conta.tipo_de_conta.value == "Conta Caixa"

    obj_conta.tipo_de_conta = TiposDeContas.INVESTIMENTO
    assert obj_conta.tipo_de_conta.value == "Conta de Investimento"

    assert obj_conta == obj_conta_clone
