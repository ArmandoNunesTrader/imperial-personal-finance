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
from typing import List

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu
import src.utils.string_utils as stu


@dataclass
class CartoesDeCredito:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    sigla: str = field(repr=True, compare=True, init=True)
    nome: str = field(repr=True, compare=True, init=True)
    numero: str = field(
        repr=True, compare=True, init=True
    )  # No formato 9999.9999.9999.9999
    data_de_validade: str = field(
        repr=True, compare=True, init=True
    )  # No formato 99/9999
    melhor_dia_de_compra: int = field(repr=True, compare=True, init=True)
    dia_de_vencimento: int = field(repr=True, compare=True, init=True)
    id_moeda: UUID = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    tipo_de_moeda: str = field(repr=False, compare=False, init=True, default="BRL")
    valor: float = field(repr=False, compare=False, init=True, default=1.0)

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    limite_de_credito: VOMoeda = field(repr=True, compare=False, init=False)
    # Campos com valor default devem ser os últimos
    id_cartao_de_credito: UUID = field(
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
        self.limite_de_credito = VOMoeda(self.valor, TiposDeMoedas[self.tipo_de_moeda])

    def __str__(self):
        repr = (
            "ID: {} - Sigla: {}"
            + " - Nome: {}"
            + " - Número: {} - Validade: {} - Dia de Vencimento: {}"
        )

        return repr.format(
            self.id_cartao_de_credito,
            self.sigla,
            self.nome,
            self.numero,
            self.data_de_validade,
            stu.pad_str_left(self.dia_de_vencimento, 2, "0"),
        )
