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
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda

import src.utils.datetime_utils as dtu
import src.utils.math_utils as mtu


@dataclass
class Moedas:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    sigla: str = field(repr=True, compare=True, init=True)
    descricao: str = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    _tipo_de_moeda: str = field(
        repr=False, compare=False, init=True, default="Real Brasileiro"
    )
    _valor_da_paridade: float = field(repr=False, compare=False, init=True, default=1.0)

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    # Campos com valor default devem ser os últimos
    id_moeda: UUID = field(repr=True, compare=True, init=False, default_factory=uuid4)
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    @property
    def paridade_com_real_brasileiro(self) -> VOMoeda:
        if (is_null_or_empty(self._tipo_de_moeda)) or (
            self._tipo_de_moeda not in TiposDeMoedas.all_values()
        ):
            aux_tipo_de_moeda = Moedas._tipo_de_moeda
        else:
            aux_tipo_de_moeda = self._tipo_de_moeda
        if mtu.is_float(self._valor_da_paridade):
            aux_valor_da_paridade = float(self._valor_da_paridade)
        else:
            aux_valor_da_paridade = Moedas._valor_da_paridade
        return VOMoeda(aux_valor_da_paridade, TiposDeMoedas(aux_tipo_de_moeda))

    @paridade_com_real_brasileiro.setter
    def paridade_com_real_brasileiro(self, value: VOMoeda) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._tipo_de_moeda = Moedas._tipo_de_moeda  # pragma: no cover
            self._valor_da_paridade = Moedas._valor_da_paridade  # pragma: no cover
        else:
            self._tipo_de_moeda = value.tipo_de_moeda
            self._valor_da_paridade = float(value.valor)

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        pass

    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {}"

        return repr.format(self.id_moeda, self.sigla, self.descricao)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Moedas):
            return False

        return (
            (self.id_moeda == other.id_moeda)
            and (self.sigla == other.sigla)
            and (self.descricao == other.descricao)
            and (
                self.paridade_com_real_brasileiro.formatada
                == other.paridade_com_real_brasileiro.formatada
            )
        )
