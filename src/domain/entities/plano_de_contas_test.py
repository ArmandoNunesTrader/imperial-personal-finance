#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   plano_de_contas_test.py
@Created :   09/12/2024 13:07:29
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste da classe Plano de Contas
    ============================================================================
"""

from datetime import datetime

import re

from src.domain.enums.categorias_de_contas import CategoriasDeContas
from src.domain.enums.grupos_de_contas import GruposDeContas
from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.plano_de_contas import PlanoDeContas

import src.utils.validate_utils as vdu


def test_create():
    mask_1 = re.compile(
        "^ID: [a-f0-9-]{36}"
        + " - Código Contábil: 2."
        + " - Descrição: Passivo"
        + " - Categoria de Contas: Despesa"
        + " - Grupo de Contas: 2-Passivo"
    )
    mask_2 = re.compile(
        "^ID: [a-f0-9-]{36}"
        + " - Código Contábil: 2."
        + " - Descrição: Passivo"
        + " - Categoria de Contas: Receita"
        + " - Grupo de Contas: 1-Ativo"
    )

    obj_plano_de_contas_1 = PlanoDeContas(
        codigo_contabil="2.",
        descricao="Passivo",
        eh_totalizadora=True,
        _tipo_de_moeda="Dólar Americano",
        _saldo_inicial=1256.87,
        _categoria_de_conta="Despesa",
        _grupo_de_conta="2-Passivo",
    )
    obj_plano_de_contas_clone = obj_plano_de_contas_1

    assert vdu.is_valid_uuid(obj_plano_de_contas_1.id_plano_de_contas)
    assert obj_plano_de_contas_1.codigo_contabil == "2."
    assert obj_plano_de_contas_1.descricao == "Passivo"
    assert obj_plano_de_contas_1.saldo_inicial.formatada == "$ 1,256.87"
    assert obj_plano_de_contas_1.eh_totalizadora is True
    assert isinstance(obj_plano_de_contas_1.created_at, datetime)
    assert isinstance(obj_plano_de_contas_1.updated_at, datetime)
    assert str(obj_plano_de_contas_1) is not None

    assert re.fullmatch(mask_1, str(obj_plano_de_contas_1))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_plano_de_contas_1 is not None

    obj_plano_de_contas_2 = PlanoDeContas(
        codigo_contabil="2.",
        descricao="Passivo",
        eh_totalizadora=True,
        _tipo_de_moeda="Dólar Americano",
        _saldo_inicial=1256.87,
        _categoria_de_conta=None,
        _grupo_de_conta=None,
    )

    assert vdu.is_valid_uuid(obj_plano_de_contas_2.id_plano_de_contas)
    assert obj_plano_de_contas_2.codigo_contabil == "2."
    assert obj_plano_de_contas_2.descricao == "Passivo"
    assert obj_plano_de_contas_2.saldo_inicial.formatada == "$ 1,256.87"
    assert obj_plano_de_contas_2.eh_totalizadora is True
    assert isinstance(obj_plano_de_contas_2.created_at, datetime)
    assert isinstance(obj_plano_de_contas_2.updated_at, datetime)
    assert str(obj_plano_de_contas_2) is not None

    assert re.fullmatch(mask_2, str(obj_plano_de_contas_2))

    obj_plano_de_contas_3 = PlanoDeContas(
        codigo_contabil="2.",
        descricao="Passivo",
        eh_totalizadora=True,
        _tipo_de_moeda=None,
        _saldo_inicial=None,
        _categoria_de_conta=None,
        _grupo_de_conta=None,
    )

    assert vdu.is_valid_uuid(obj_plano_de_contas_3.id_plano_de_contas)
    assert obj_plano_de_contas_3.codigo_contabil == "2."
    assert obj_plano_de_contas_3.descricao == "Passivo"
    assert obj_plano_de_contas_3.saldo_inicial.formatada == "R$ 1,00"
    assert obj_plano_de_contas_3.eh_totalizadora is True
    assert isinstance(obj_plano_de_contas_3.created_at, datetime)
    assert isinstance(obj_plano_de_contas_3.updated_at, datetime)
    assert str(obj_plano_de_contas_3) is not None

    assert re.fullmatch(mask_2, str(obj_plano_de_contas_3))

    assert obj_plano_de_contas_1 == obj_plano_de_contas_clone
    assert obj_plano_de_contas_1 != [obj_plano_de_contas_1, obj_plano_de_contas_clone]

    obj_plano_de_contas_1._tipo_de_moeda = "Libra Esterlina"
    obj_plano_de_contas_1._saldo_inicial = 20000

    assert obj_plano_de_contas_1.saldo_inicial.formatada == "R$ 20.000,00"
    assert str(obj_plano_de_contas_1) is not None

    obj_plano_de_contas_1._saldo_inicial = "20000.00"

    obj_plano_de_contas_1_clone = obj_plano_de_contas_1

    assert obj_plano_de_contas_1.saldo_inicial.formatada == "R$ 1,00"
    assert str(obj_plano_de_contas_1) is not None

    obj_vo_moeda = VOMoeda(1254, TiposDeMoedas.EUR)
    obj_plano_de_contas_1.saldo_inicial = obj_vo_moeda
    assert obj_plano_de_contas_1.saldo_inicial.formatada == "€ 1,254.00"
    assert str(obj_plano_de_contas_1) is not None

    obj_plano_de_contas_1._categoria_de_conta = "Conta Teste"
    assert obj_plano_de_contas_1.categoria_de_conta.value == "Receita"

    obj_plano_de_contas_1._categoria_de_conta = "Investimento"
    assert obj_plano_de_contas_1.categoria_de_conta.value == "Investimento"

    obj_plano_de_contas_1.categoria_de_conta = CategoriasDeContas.DESPESA
    assert obj_plano_de_contas_1.categoria_de_conta.value == "Despesa"

    assert obj_plano_de_contas_1 == obj_plano_de_contas_1_clone

    obj_plano_de_contas_1.grupo_de_conta = GruposDeContas.RESULTADO
    assert obj_plano_de_contas_1.grupo_de_conta.value == "3-Resultado"
