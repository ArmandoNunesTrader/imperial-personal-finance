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
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.enums.grupos_de_contas import GruposDeContas
from src.domain.enums.categorias_de_contas import CategoriasDeContas
from src.domain.value_objects.moeda import VOMoeda
from src.domain.entities.lancamentos import Lancamentos

import src.utils.datetime_utils as dtu
import src.utils.math_utils as mtu


@dataclass
class PlanoDeContas:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    # No formato 9.99.999
    codigo_contabil: str = field(repr=True, compare=True, init=True)
    descricao: str = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    eh_totalizadora: bool = field(repr=False, compare=False, init=True, default=False)
    _tipo_de_moeda: str = field(
        repr=False, compare=False, init=True, default="Real Brasileiro"
    )
    _saldo_inicial: float = field(repr=False, compare=False, init=True, default=1.0)
    _categoria_de_conta: str = field(
        repr=False, compare=False, init=True, default="Receita"
    )
    _grupo_de_conta: str = field(
        repr=False, compare=False, init=True, default="1-Ativo"
    )

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    # Campos com valor default devem ser os últimos
    id_plano_de_contas: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    lancamentos: List[Lancamentos] = field(
        repr=True, compare=True, init=False, default_factory=list
    )
    subordinadas: List["PlanoDeContas"] = field(default_factory=list)
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    @property
    def saldo_inicial(self) -> VOMoeda:
        if is_null_or_empty(self._tipo_de_moeda) or (
            self._tipo_de_moeda not in TiposDeMoedas.all_values()
        ):
            aux_tipo_de_moeda = PlanoDeContas._tipo_de_moeda
        else:
            aux_tipo_de_moeda = self._tipo_de_moeda
        if mtu.is_float(self._saldo_inicial):
            aux_saldo_inicial = float(self._saldo_inicial)
        else:
            aux_saldo_inicial = PlanoDeContas._saldo_inicial
        return VOMoeda(aux_saldo_inicial, TiposDeMoedas(aux_tipo_de_moeda))

    @saldo_inicial.setter
    def saldo_inicial(self, value: VOMoeda) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._tipo_de_moeda = PlanoDeContas._tipo_de_moeda  # pragma: no cover
            self._saldo_inicial = PlanoDeContas._saldo_inicial  # pragma: no cover
        else:
            self._tipo_de_moeda = value.tipo_de_moeda
            self._saldo_inicial = float(value.valor)

    @property
    def categoria_de_conta(self) -> CategoriasDeContas:
        if is_null_or_empty(self._categoria_de_conta) or (
            self._categoria_de_conta not in CategoriasDeContas.all_values()
        ):
            aux_categoria_de_conta = PlanoDeContas._categoria_de_conta
        else:
            aux_categoria_de_conta = self._categoria_de_conta

        return CategoriasDeContas(aux_categoria_de_conta)

    @categoria_de_conta.setter
    def categoria_de_conta(self, value: CategoriasDeContas) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._categoria_de_conta = (
                PlanoDeContas._categoria_de_conta
            )  # pragma: no cover
        else:
            self._categoria_de_conta = value.value

    @property
    def grupo_de_conta(self) -> GruposDeContas:
        if is_null_or_empty(self._grupo_de_conta) or (
            self._grupo_de_conta not in GruposDeContas.all_values()
        ):
            aux_grupo_de_conta = PlanoDeContas._grupo_de_conta
        else:
            aux_grupo_de_conta = self._grupo_de_conta

        return GruposDeContas(aux_grupo_de_conta)

    @grupo_de_conta.setter
    def grupo_de_conta(self, value: GruposDeContas) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._grupo_de_conta = PlanoDeContas._grupo_de_conta  # pragma: no cover
        else:
            self._grupo_de_conta = value.value

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        pass

    def __str__(self):
        repr = (
            "ID: {} - Código Contábil: {}"
            + " - Descrição: {}"
            + " - Categoria de Contas: {}"
            + " - Grupo de Contas: {}"
        )

        return repr.format(
            self.id_plano_de_contas,
            self.codigo_contabil,
            self.descricao,
            self.categoria_de_conta.value,
            self.grupo_de_conta.value,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PlanoDeContas):
            return False

        return (
            (self.id_plano_de_contas == other.id_plano_de_contas)
            and (self.codigo_contabil == other.codigo_contabil)
            and (self.descricao == other.descricao)
            and (self.categoria_de_conta.value == other.categoria_de_conta.value)
            and (self.grupo_de_conta.value == other.grupo_de_conta.value)
        )
