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
        tipo_de_moeda="USD",
        valor=1256.87,
        eh_totalizadora=True,
        descricao_categoria_de_contas="Despesa",
        descricao_grupo_de_contas="2-Passivo",
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
        tipo_de_moeda="USD",
        valor=1256.87,
        eh_totalizadora=True,
        descricao_categoria_de_contas=None,
        descricao_grupo_de_contas=None,
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
        tipo_de_moeda=None,
        valor=None,
        eh_totalizadora=True,
        descricao_categoria_de_contas=None,
        descricao_grupo_de_contas=None,
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
