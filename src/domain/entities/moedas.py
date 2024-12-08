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

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import Moeda as VO_Moeda

import src.utils.datetime_utils as dtu


@dataclass
class Moedas:
    sigla: str = field(repr=True, compare=True)
    descricao: str = field(repr=True, compare=True)
    # Campos com valor default devem ser os últimos
    tipo_de_moeda: str = field(repr=False, compare=False, default="BRL")
    valor_da_paridade: float = field(repr=False, compare=False, default=1.0)
    id_moeda: UUID = field(repr=True, compare=True, init=False, default_factory=uuid4)
    paridade_com_real_brasileiro: VO_Moeda = field(repr=True, compare=False, init=False)
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        self.paridade_com_real_brasileiro = VO_Moeda(
            self.valor_da_paridade, TiposDeMoedas[self.tipo_de_moeda]
        )

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_moeda, self.sigla, self.descricao)
