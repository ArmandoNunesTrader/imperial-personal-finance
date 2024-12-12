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

import src.utils.datetime_utils as dtu


@dataclass
class PlanoDeContas:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    codigo_contabil: str = field(
        repr=True, compare=True, init=True
    )  # No formato 9.99.999
    descricao: str = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    tipo_de_moeda: str = field(repr=False, compare=False, init=True, default="BRL")
    valor: float = field(repr=False, compare=False, init=True, default=1.0)
    eh_totalizadora: bool = field(repr=False, compare=False, init=True, default=False)
    descricao_categoria_de_contas: str = field(
        repr=False, compare=False, init=True, default="Receita"
    )
    descricao_grupo_de_contas: str = field(
        repr=False, compare=False, init=True, default="1-Ativo"
    )

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    saldo_inicial: VOMoeda = field(repr=True, compare=False, init=False)
    categoria_de_contas: CategoriasDeContas = field(
        repr=True, compare=False, init=False
    )
    grupo_de_contas: GruposDeContas = field(repr=True, compare=False, init=False)
    # Campos com valor default devem ser os últimos
    id_plano_de_contas: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    subordinadas: List["PlanoDeContas"] = field(default_factory=list)
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        # Trata o Value Object Saldo Inicial
        if is_null_or_empty(self.tipo_de_moeda):
            aux_tipo_de_moeda = "BRL"
        else:
            aux_tipo_de_moeda = self.tipo_de_moeda

        if is_null_or_empty(self.valor):
            aux_valor = 1
        else:
            aux_valor = self.valor
        self.saldo_inicial = VOMoeda(aux_valor, TiposDeMoedas[aux_tipo_de_moeda])

        # Trata o enum Situação do Lançamento
        if is_null_or_empty(self.descricao_categoria_de_contas):
            self.categoria_de_contas = CategoriasDeContas.RECEITA
        else:
            self.categoria_de_contas = CategoriasDeContas(
                self.descricao_categoria_de_contas
            )

        # Trata o enum Tipo de Lançamento
        if is_null_or_empty(self.descricao_grupo_de_contas):
            self.grupo_de_contas = GruposDeContas.ATIVO
        else:
            self.grupo_de_contas = GruposDeContas(self.descricao_grupo_de_contas)

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
            self.categoria_de_contas.value,
            self.grupo_de_contas.value,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PlanoDeContas):
            return False

        return (
            (self.id_plano_de_contas == other.id_plano_de_contas)
            and (self.codigo_contabil == other.codigo_contabil)
            and (self.descricao == other.descricao)
            and (self.categoria_de_contas.value == other.categoria_de_contas.value)
            and (self.grupo_de_contas.value == other.grupo_de_contas.value)
        )
