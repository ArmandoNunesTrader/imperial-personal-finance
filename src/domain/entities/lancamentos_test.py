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
        Teste da classe Lançamentos
    ============================================================================
"""

from datetime import datetime
from uuid import uuid4

import re

from src.domain.entities.lancamentos import Lancamentos

import src.utils.validate_utils as vdu


def test_create():
    mask_1 = re.compile(
        r"^ID: [a-f0-9-]{36} - Data do Vencimento: 01-01-2024"
        + r" - Descrição: Compra de Mercado - Valor: € 65,498.12$"
    )
    mask_2 = re.compile(
        r"^ID: [a-f0-9-]{36} - Data do Vencimento: 01-01-2024"
        + r" - Descrição: Compra de Mercado - Valor: R\$ 65.498,12$"
    )
    mask_3 = re.compile(
        r"^ID: [a-f0-9-]{36} - Data do Vencimento: 01-01-2100"
        + r" - Descrição: Compra de Mercado - Valor: € 1.00$"
    )
    mask_4 = re.compile(
        r"^ID: [a-f0-9-]{36} - Data do Vencimento: 01-01-2024"
        + r" - Descrição: Compra de Mercado - Valor: € 12,345.67$"
    )
    obj_lancamento_1 = Lancamentos(
        descricao="Compra de Mercado",
        id_plano_de_contas=uuid4(),
        id_conta=uuid4(),
        id_cartao_de_credito=uuid4(),
        id_centro_de_custo=uuid4(),
        data_do_lancamento=datetime(2024, 12, 1, 0, 0, 0, 0).date(),
        data_do_vencimento=datetime(2024, 1, 1, 0, 0, 0, 0).date(),
        tipo_de_moeda="EUR",
        valor=65498.12,
        descricao_situacao_do_lancamento="A Receber",
        descricao_tipo_de_lancamento="Lançamento de Investimento",
    )

    assert vdu.is_valid_uuid(obj_lancamento_1.id_lancamento)
    assert obj_lancamento_1.descricao == "Compra de Mercado"
    assert obj_lancamento_1.valor_do_lancamento.formatada == "€ 65,498.12"
    assert obj_lancamento_1.ano_mes_orcamento == "2024-01"
    assert isinstance(obj_lancamento_1.created_at, datetime)
    assert isinstance(obj_lancamento_1.updated_at, datetime)
    assert str(obj_lancamento_1) is not None

    assert re.fullmatch(mask_1, str(obj_lancamento_1))

    assert obj_lancamento_1 is not None

    obj_lancamento_2 = Lancamentos(
        descricao="Compra de Mercado",
        id_plano_de_contas=uuid4(),
        id_conta=uuid4(),
        id_cartao_de_credito=uuid4(),
        id_centro_de_custo=uuid4(),
        data_do_lancamento=datetime(2024, 12, 1, 0, 0, 0, 0).date(),
        data_do_vencimento=datetime(2024, 1, 1, 0, 0, 0, 0).date(),
        tipo_de_moeda=None,
        valor=65498.12,
        descricao_situacao_do_lancamento="Recebido",
        descricao_tipo_de_lancamento="Lançamento de Investimento",
    )

    assert vdu.is_valid_uuid(obj_lancamento_2.id_lancamento)
    assert obj_lancamento_2.descricao == "Compra de Mercado"
    assert obj_lancamento_2.valor_do_lancamento.formatada == "R$ 65.498,12"
    assert obj_lancamento_2.ano_mes_orcamento == "2024-01"
    assert isinstance(obj_lancamento_2.created_at, datetime)
    assert isinstance(obj_lancamento_2.updated_at, datetime)

    assert str(obj_lancamento_2) is not None

    assert re.fullmatch(mask_2, str(obj_lancamento_2))

    obj_lancamento_3 = Lancamentos(
        descricao="Compra de Mercado",
        id_plano_de_contas=uuid4(),
        id_conta=uuid4(),
        id_cartao_de_credito=uuid4(),
        id_centro_de_custo=uuid4(),
        data_do_lancamento=datetime(2024, 12, 1, 0, 0, 0, 0).date(),
        data_do_vencimento=datetime(2100, 1, 1, 0, 0, 0, 0).date(),
        tipo_de_moeda="EUR",
        valor=None,
        descricao_situacao_do_lancamento="A Receber",
        descricao_tipo_de_lancamento="Lançamento de Investimento",
    )

    assert vdu.is_valid_uuid(obj_lancamento_3.id_lancamento)
    assert obj_lancamento_3.descricao == "Compra de Mercado"
    assert obj_lancamento_3.valor_do_lancamento.formatada == "€ 1.00"
    assert obj_lancamento_3.ano_mes_orcamento == "2100-01"
    assert isinstance(obj_lancamento_3.created_at, datetime)
    assert isinstance(obj_lancamento_3.updated_at, datetime)

    assert str(obj_lancamento_3) is not None

    assert re.fullmatch(mask_3, str(obj_lancamento_3))

    obj_lancamento_4 = Lancamentos(
        descricao="Compra de Mercado",
        id_plano_de_contas=uuid4(),
        id_conta=uuid4(),
        id_cartao_de_credito=uuid4(),
        id_centro_de_custo=uuid4(),
        data_do_lancamento=datetime(2024, 12, 1, 0, 0, 0, 0).date(),
        data_do_vencimento=datetime(2024, 1, 1, 0, 0, 0, 0).date(),
        tipo_de_moeda="EUR",
        valor=12345.67,
        descricao_situacao_do_lancamento=None,
        descricao_tipo_de_lancamento=None,
    )

    assert vdu.is_valid_uuid(obj_lancamento_4.id_lancamento)
    assert obj_lancamento_4.descricao == "Compra de Mercado"
    assert obj_lancamento_4.valor_do_lancamento.formatada == "€ 12,345.67"
    assert obj_lancamento_4.ano_mes_orcamento == "2024-01"
    assert isinstance(obj_lancamento_4.created_at, datetime)
    assert isinstance(obj_lancamento_4.updated_at, datetime)

    assert str(obj_lancamento_4) is not None

    assert re.fullmatch(mask_4, str(obj_lancamento_4))
