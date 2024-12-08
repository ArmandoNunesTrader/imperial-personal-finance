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

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import Moeda as VO_Moeda
from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu


@dataclass
class Contas:
    sigla: str = field(repr=True, compare=True)
    descricao: str = field(repr=True, compare=True)
    # Campos com valor default devem ser os últimos
    tipo_de_moeda: str = field(repr=False, compare=False, default="BRL")
    valor_de_saldo: float = field(repr=False, compare=False, default=0.0)
    id_conta: UUID = field(repr=True, compare=True, init=False, default_factory=uuid4)
    lancamentos: list[Lancamentos] = field(
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
        self.saldo_de_abertura = VO_Moeda(
            self.valor_de_saldo, TiposDeMoedas[self.tipo_de_moeda]
        )

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_conta, self.sigla, self.descricao)
