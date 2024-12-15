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

from src.domain.enums.situacoes_dos_lancamentos import SituacoesDosLancamentos
from src.domain.enums.tipos_de_lancamentos import TiposDeLancamentos
from src.domain.entities.lancamentos import Lancamentos
from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda

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
        _tipo_de_moeda="Euro",
        _valor_do_lancamento=65498.12,
        _situacao_do_lancamento="A Receber",
        _tipo_de_lancamento="Lançamento de Investimento",
    )
    obj_lancamento_clone = obj_lancamento_1

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
        _tipo_de_moeda=None,
        _valor_do_lancamento=65498.12,
        _situacao_do_lancamento="Recebido",
        _tipo_de_lancamento="Lançamento de Investimento",
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
        _tipo_de_moeda="Euro",
        _valor_do_lancamento=None,
        _situacao_do_lancamento="A Receber",
        _tipo_de_lancamento="Lançamento de Investimento",
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
        _tipo_de_moeda="Euro",
        _valor_do_lancamento=12345.67,
        _situacao_do_lancamento=None,
        _tipo_de_lancamento=None,
    )

    assert vdu.is_valid_uuid(obj_lancamento_4.id_lancamento)
    assert obj_lancamento_4.descricao == "Compra de Mercado"
    assert obj_lancamento_4.valor_do_lancamento.formatada == "€ 12,345.67"
    assert obj_lancamento_4.vencido is True
    assert obj_lancamento_4.ano_mes_orcamento == "2024-01"
    assert isinstance(obj_lancamento_4.created_at, datetime)
    assert isinstance(obj_lancamento_4.updated_at, datetime)

    assert str(obj_lancamento_4) is not None

    assert re.fullmatch(mask_4, str(obj_lancamento_4))

    assert obj_lancamento_1 == obj_lancamento_clone
    assert obj_lancamento_1 != [obj_lancamento_1, obj_lancamento_clone]

    obj_lancamento_1._tipo_de_moeda = "Libra Esterlina"
    obj_lancamento_1._valor_do_lancamento = 20000

    assert obj_lancamento_1.valor_do_lancamento.formatada == "R$ 20.000,00"
    assert str(obj_lancamento_1) is not None

    obj_lancamento_1._valor_do_lancamento = "20000.00"

    obj_lancamento_1_clone = obj_lancamento_1

    assert obj_lancamento_1.valor_do_lancamento.formatada == "R$ 1,00"
    assert str(obj_lancamento_1) is not None

    obj_vo_moeda = VOMoeda(1254, TiposDeMoedas.EUR)
    obj_lancamento_1.valor_do_lancamento = obj_vo_moeda
    assert obj_lancamento_1.valor_do_lancamento.formatada == "€ 1,254.00"
    assert str(obj_lancamento_1) is not None

    obj_lancamento_1._situacao_do_lancamento = "A Receber"
    assert obj_lancamento_1.situacao_do_lancamento.value == "A Receber"

    obj_lancamento_1._situacao_do_lancamento = "Pago"
    assert obj_lancamento_1.situacao_do_lancamento.value == "Pago"

    obj_lancamento_1.situacao_do_lancamento = SituacoesDosLancamentos.RECEBIDO
    assert obj_lancamento_1.situacao_do_lancamento.value == "Recebido"

    assert obj_lancamento_1 == obj_lancamento_1_clone

    obj_lancamento_1._situacao_do_lancamento = "Conta Teste"
    assert obj_lancamento_1.situacao_do_lancamento.value == "A Receber"

    obj_lancamento_1._tipo_de_lancamento = "Lançamento de Teste"
    assert obj_lancamento_1.tipo_de_lancamento.value == "Lançamento de Receita"

    obj_lancamento_1._situacao_do_lancamento = "A Pagar"
    assert obj_lancamento_1.situacao_do_lancamento.value == "A Pagar"

    obj_lancamento_1.data_do_vencimento = datetime(2100, 1, 1, 0, 0, 0, 0).date()
    assert obj_lancamento_1.vencido is False

    obj_lancamento_1._situacao_do_lancamento = "Pago"
    obj_lancamento_1.data_do_vencimento = datetime(2000, 1, 1, 0, 0, 0, 0).date()
    assert obj_lancamento_1.vencido is False

    obj_lancamento_1._tipo_de_lancamento = "Lançamento de Investimento"
    assert obj_lancamento_1.tipo_de_lancamento.value == "Lançamento de Investimento"

    obj_tipo_de_lancamento = TiposDeLancamentos.OUTRO
    obj_lancamento_1.tipo_de_lancamento = obj_tipo_de_lancamento
    assert obj_lancamento_1.tipo_de_lancamento.value == "Outro Lançamento"
