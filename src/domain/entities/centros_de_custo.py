#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   centros_de_custo.py
@Created :   07/12/2024 13:25:20
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de Centros de Custo
    ============================================================================
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

import src.utils.datetime_utils as dtu
from src.domain.entities.lancamentos import Lancamentos


@dataclass
class CentrosDeCusto:
    sigla: str = field(repr=True, compare=True)
    descricao: str = field(repr=True, compare=True)
    # Campos com valor default devem ser os últimos
    id_centro_de_custo: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    lancamentos: list[Lancamentos] = field(
        repr=True, compare=True, init=False, default_factory=list
    )
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_centro_de_custo, self.sigla, self.descricao)
