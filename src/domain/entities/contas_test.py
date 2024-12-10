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

import re

from src.domain.entities.moedas import Moedas

import src.utils.validate_utils as vdu


def test_create():
    obj_moeda = Moedas(
        sigla="Moeda",
        descricao="Moeda de Teste",
        tipo_de_moeda="USD",
        valor_da_paridade=5.67,
    )

    assert vdu.is_valid_uuid(obj_moeda.id_moeda)
    assert obj_moeda.sigla == "Moeda"
    assert obj_moeda.descricao == "Moeda de Teste"
    assert obj_moeda.paridade_com_real_brasileiro.formatada == "$ 5.67"
    assert isinstance(obj_moeda.created_at, datetime)
    assert isinstance(obj_moeda.updated_at, datetime)
    assert str(obj_moeda) is not None

    mask = re.compile("^ID: [a-f0-9-]{36} - Sigla: Moeda - Descrição: Moeda de Teste$")

    assert re.fullmatch(mask, str(obj_moeda))

    # Colocar como is None para ver os detalhes após a criação
    assert obj_moeda is not None
