#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas.py
@Created :   07/12/2024 13:19:22
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de Moedas
    ============================================================================
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


from src.domain.value_objects import Moeda

import src.utils.datetime_utils as dtu


@dataclass
class Moedas:
    id_moeda: UUID = field(default_factory=uuid4)
    sigla: str
    descricao: str
    paridade_com_real_brasileiro: Moeda
    created_at: datetime = field(default_factory=dtu.dt_now_utc())
    updated_at: datetime = field(default_factory=dtu.dt_now_utc())

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_moeda, self.sigla, self.descricao)
