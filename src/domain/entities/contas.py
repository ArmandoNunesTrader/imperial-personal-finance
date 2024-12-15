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
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.enums.tipos_de_contas import TiposDeContas
from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu
import src.utils.math_utils as mtu


@dataclass
class Contas:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    sigla: str = field(repr=True, compare=True, init=True)
    descricao: str = field(repr=True, compare=True, init=True)
    id_moeda: UUID = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    _tipo_de_moeda: str = field(
        repr=False, compare=False, init=True, default="Real Brasileiro"
    )
    _saldo_de_abertura: float = field(repr=False, compare=False, init=True, default=1.0)
    _tipo_de_conta: str = field(
        repr=False, compare=False, init=True, default="Conta de Ativo"
    )

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
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

    @property
    def saldo_de_abertura(self) -> VOMoeda:
        if (is_null_or_empty(self._tipo_de_moeda)) or (
            self._tipo_de_moeda not in TiposDeMoedas.all_values()
        ):
            aux_tipo_de_moeda = Contas._tipo_de_moeda
        else:
            aux_tipo_de_moeda = self._tipo_de_moeda
        if mtu.is_float(self._saldo_de_abertura):
            aux_saldo_de_abertura = float(self._saldo_de_abertura)
        else:
            aux_saldo_de_abertura = Contas._saldo_de_abertura
        return VOMoeda(aux_saldo_de_abertura, TiposDeMoedas(aux_tipo_de_moeda))

    @saldo_de_abertura.setter
    def saldo_de_abertura(self, value: VOMoeda) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._tipo_de_moeda = Contas._tipo_de_moeda  # pragma: no cover
            self._saldo_de_abertura = Contas._saldo_de_abertura  # pragma: no cover
        else:
            self._tipo_de_moeda = value.tipo_de_moeda
            self._saldo_de_abertura = float(value.valor)

    @property
    def tipo_de_conta(self) -> TiposDeContas:
        if is_null_or_empty(self._tipo_de_conta) or (
            self._tipo_de_conta not in TiposDeContas.all_values()
        ):
            aux_tipo_de_conta = Contas._tipo_de_conta
        else:
            aux_tipo_de_conta = self._tipo_de_conta

        return TiposDeContas(aux_tipo_de_conta)

    @tipo_de_conta.setter
    def tipo_de_conta(self, value: TiposDeContas) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._tipo_de_conta = Contas._tipo_de_conta  # pragma: no cover
        else:
            self._tipo_de_conta = value.value

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        pass

    def __str__(self):
        repr = "ID: {} - Sigla: {} - Descrição: {} - Saldo de Abertura: {}"

        return repr.format(
            self.id_conta, self.sigla, self.descricao, self.saldo_de_abertura.formatada
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Contas):
            return False

        return (
            (self.id_conta == other.id_conta)
            and (self.sigla == other.sigla)
            and (self.descricao == other.descricao)
            and (self.id_moeda == other.id_moeda)
            and (self.tipo_de_conta.value == other.tipo_de_conta.value)
        )
