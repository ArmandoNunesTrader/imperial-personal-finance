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
from typing import List

from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu


@dataclass
class CentrosDeCusto:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    sigla: str = field(repr=True, compare=True, init=True)
    descricao: str = field(repr=True, compare=True, init=True)

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    # Campos com valor default devem ser os últimos
    id_centro_de_custo: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    lancamentos: List[Lancamentos] = field(
        repr=True, compare=True, init=False, default_factory=list
    )
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        pass

    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_centro_de_custo, self.sigla, self.descricao)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CentrosDeCusto):
            return False

        return (
            (self.id_centro_de_custo == other.id_centro_de_custo)
            and (self.sigla == other.sigla)
            and (self.descricao == other.descricao)
        )
