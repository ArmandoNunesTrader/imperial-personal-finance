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
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu
import src.utils.string_utils as stu
import src.utils.math_utils as mtu


@dataclass
class CartoesDeCredito:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    sigla: str = field(repr=True, compare=True, init=True)
    nome: str = field(repr=True, compare=True, init=True)
    # No formato 9999.9999.9999.9999
    numero: str = field(repr=True, compare=True, init=True)
    # No formato 99/9999
    data_de_validade: str = field(repr=True, compare=True, init=True)
    melhor_dia_de_compra: int = field(repr=True, compare=True, init=True)
    dia_de_vencimento: int = field(repr=True, compare=True, init=True)
    id_moeda: UUID = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    _tipo_de_moeda: str = field(
        repr=False, compare=False, init=True, default="Real Brasileiro"
    )
    _valor_do_limite: float = field(repr=False, compare=False, init=True, default=1.0)

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
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

    @property
    def limite_de_credito(self) -> VOMoeda:
        if (is_null_or_empty(self._tipo_de_moeda)) or (
            self._tipo_de_moeda not in TiposDeMoedas.all_values()
        ):
            aux_tipo_de_moeda = CartoesDeCredito._tipo_de_moeda
        else:
            aux_tipo_de_moeda = self._tipo_de_moeda
        if mtu.is_float(self._valor_do_limite):
            aux_valor_do_limite = float(self._valor_do_limite)
        else:
            aux_valor_do_limite = CartoesDeCredito._valor_do_limite
        return VOMoeda(aux_valor_do_limite, TiposDeMoedas(aux_tipo_de_moeda))

    @limite_de_credito.setter
    def limite_de_credito(self, value: VOMoeda) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._tipo_de_moeda = CartoesDeCredito._tipo_de_moeda  # pragma: no cover
            self._valor_do_limite = (
                CartoesDeCredito._valor_do_limite
            )  # pragma: no cover
        else:
            self._tipo_de_moeda = value.tipo_de_moeda
            self._valor_do_limite = float(value.valor)

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        pass

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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CartoesDeCredito):
            return False

        return (
            (self.id_cartao_de_credito == other.id_cartao_de_credito)
            and (self.sigla == other.sigla)
            and (self.nome == other.nome)
            and (self.numero == other.numero)
            and (self.limite_de_credito.formatada == other.limite_de_credito.formatada)
            and (self.id_moeda == other.id_moeda)
        )
