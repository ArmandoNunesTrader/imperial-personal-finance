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
from uuid import UUID, uuid4

import re

from src.domain.entities.lancamentos import Lancamentos
from src.domain.value_objects.moeda import Moeda as VO_Moeda


def is_valid_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        return False


def test_create():
    obj_lancamento = Lancamentos(
        valor_do_lancamento=VO_Moeda(123.45),
        descricao="Compra de Mercado",
        id_plano_de_contas=uuid4(),
        id_cartao_de_credito=uuid4(),
        id_conta=uuid4(),
        id_centro_de_custo=uuid4(),
    )

    assert is_valid_uuid(obj_lancamento.id_lancamento)
    assert obj_lancamento.descricao == "Compra de Mercado"
    assert obj_lancamento.valor_do_lancamento.formatada == "R$ 123,45"
    assert isinstance(obj_lancamento.created_at, datetime)
    assert isinstance(obj_lancamento.updated_at, datetime)
    assert str(obj_lancamento) is not None

    mask = re.compile(
        "^ID: [a-f0-9-]{36} - Data do Vencimento: 07-12-2024 - Descrição: Compra de Mercado - Valor: R\$ 123,45$"  # noqa F401
    )

    assert re.fullmatch(mask, str(obj_lancamento))
