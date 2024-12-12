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
from typing import List

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu


@dataclass
class Contas:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    sigla: str = field(repr=True, compare=True, init=True)
    descricao: str = field(repr=True, compare=True, init=True)
    id_moeda: UUID = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    tipo_de_moeda: str = field(repr=False, compare=False, default="BRL")
    valor_de_saldo: float = field(repr=False, compare=False, default=0.0)

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    saldo_de_abertura: VOMoeda = field(repr=True, compare=False, init=False)
    # Campos com valor default devem ser os últimos
    id_conta: UUID = field(repr=True, compare=True, init=False, default_factory=uuid4)
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
        self.saldo_de_abertura = VOMoeda(
            self.valor_de_saldo, TiposDeMoedas[self.tipo_de_moeda]
        )

    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_conta, self.sigla, self.descricao)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Contas):
            return False

        return (
            (self.id_conta == other.id_conta)
            and (self.sigla == other.sigla)
            and (self.descricao == other.descricao)
            and (self.id_moeda == other.id_moeda)
        )
