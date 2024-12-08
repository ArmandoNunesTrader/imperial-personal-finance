#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   centros_de_custo_test.py
@Created :   08/12/2024 14:22:43
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Teste da classe Centros de Custo
    ============================================================================
"""

from datetime import datetime

import re

from src.domain.entities.centros_de_custo import CentrosDeCusto

import src.utils.validate_utils as vdu


def test_create():
    obj_centro_de_custo = CentrosDeCusto(
        sigla="Eu",
        descricao="O Usuário do Sistema",
    )

    assert vdu.is_valid_uuid(obj_centro_de_custo.id_centro_de_custo)
    assert obj_centro_de_custo.sigla == "Eu"
    assert obj_centro_de_custo.descricao == "O Usuário do Sistema"
    assert isinstance(obj_centro_de_custo.created_at, datetime)
    assert isinstance(obj_centro_de_custo.updated_at, datetime)

    assert str(obj_centro_de_custo) is not None

    mask = re.compile(
        "^ID: [a-f0-9-]{36} - Sigla: Eu - Descrição: O Usuário do Sistema$"
    )

    assert re.fullmatch(mask, str(obj_centro_de_custo))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_centro_de_custo is not None
