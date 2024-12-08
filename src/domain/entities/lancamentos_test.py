#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   lancamentos_test.py
@Created :   07/12/2024 18:51:50
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste da classe lançamentos
    ============================================================================
"""

from datetime import datetime
from uuid import uuid4

import re

from src.domain.entities.lancamentos import Lancamentos

import src.utils.validate_utils as vdu


def test_create():
    obj_lancamento = Lancamentos(
        descricao="Compra de Mercado",
        id_plano_de_contas=uuid4(),
        id_cartao_de_credito=uuid4(),
        id_conta=uuid4(),
        id_centro_de_custo=uuid4(),
        tipo_de_moeda="EUR",
        valor=65498.12,
        descricao_situacao_do_lancamento="A Receber",
        descricao_tipo_de_lancamento="Lançamento de Investimento",
        data_do_vencimento=datetime(2024, 1, 1, 0, 0, 0, 0).date(),
    )

    assert vdu.is_valid_uuid(obj_lancamento.id_lancamento)
    assert obj_lancamento.descricao == "Compra de Mercado"
    assert obj_lancamento.valor_do_lancamento.formatada == "€ 65,498.12"
    assert isinstance(obj_lancamento.created_at, datetime)
    assert isinstance(obj_lancamento.updated_at, datetime)
    assert str(obj_lancamento) is not None

    mask = re.compile(
        "^ID: [a-f0-9-]{36} - Data do Vencimento: 01-01-2024"
        + " - Descrição: Compra de Mercado - Valor: € 65,498.12$"
    )

    assert re.fullmatch(mask, str(obj_lancamento))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_lancamento is not None
