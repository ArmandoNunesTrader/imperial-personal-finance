#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   cartoes_de_credito.py
@Created :   07/12/2024 14:03:38
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de Cartões de Crédito
    ============================================================================
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

from src.domain.value_objects import Moeda
from src.domain.entities.moedas import Moedas

import src.utils.datetime_utils as dtu


def create_moeda() -> Moeda:
    return Moeda(0, "BRL")


@dataclass
class Contas:
    id_cartao_de_credito: UUID = field(default_factory=uuid4)
    sigla: str
    nome: str
    numero: str  # No formato 9999.9999.9999.9999
    data_de_validade: str  # No formato 99/9999
    melhor_dia_de_compra: int
    dia_de_vencimento: int
    limite_de_credito: Moeda = field(default_factory=create_moeda)
    moeda: Moedas
    created_at: datetime = field(default_factory=dtu.dt_now_utc())
    updated_at: datetime = field(default_factory=dtu.dt_now_utc())
