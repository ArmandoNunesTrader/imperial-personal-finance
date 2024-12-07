#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   contas.py
@Created :   07/12/2024 13:26:50
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de Contas de movimentação de valores
    ============================================================================
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

from src.domain.value_objects import Moeda

import src.utils.datetime_utils as dtu


def create_moeda() -> Moeda:
    return Moeda(0, "BRL")


@dataclass
class Contas:
    id_conta: UUID = field(default_factory=uuid4)
    sigla: str
    descricao: str
    saldo_de_abertura: Moeda = field(default_factory=create_moeda)
    created_at: datetime = field(default_factory=dtu.dt_now_utc())
    updated_at: datetime = field(default_factory=dtu.dt_now_utc())

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_conta, self.sigla, self.descricao)
