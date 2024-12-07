#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   plano_de_contas.py
@Created :   07/12/2024 14:11:22
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de Plano de Contas contábil e de receitas/despesas
    ============================================================================
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from typing import List

from src.domain.enums.grupos_de_contas import GruposDeContas
from src.domain.enums.categorias_de_contas import CategoriasDeContas
from src.domain.value_objects import Moeda
from src.domain.entities.moedas import Moedas

import src.utils.datetime_utils as dtu


def create_moeda() -> Moeda:
    return Moeda(0, "BRL")


@dataclass
class PlanoDeContas:
    id_plano_de_contas: UUID = field(default_factory=uuid4)
    codigo_contabil: str  # No formato 9.99.999
    descricao: str
    saldo_inicial: Moedas
    eh_totalizadora: bool = field(default=False)
    grupo_de_contas: GruposDeContas = field(default=GruposDeContas.ativo.value)
    categoria_de_contas: CategoriasDeContas = field(
        default=CategoriasDeContas.receita.value
    )
    subordinadas: List["PlanoDeContas"] = field(default_factory=list)
    created_at: datetime = field(default_factory=dtu.dt_now_utc())
    updated_at: datetime = field(default_factory=dtu.dt_now_utc())

    @property
    def saldo_atual(self) -> Moeda:
        return max(
            [subordinada.price for subordinada in self.subordinadas]
            + [self.saldo_inicial],
            key=lambda x: x.valor,
        )
