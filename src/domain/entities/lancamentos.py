#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   lancamentos.py
@Created :   07/12/2024 14:35:23
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de Lançamentos
    ============================================================================
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, date
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.domain.enums.situacoes_dos_lancamentos import SituacoesDosLancamentos
from src.domain.enums.tipos_de_lancamentos import TiposDeLancamentos
from src.domain.value_objects.moeda import VOMoeda

import src.utils.datetime_utils as dtu


@dataclass
class Lancamentos:
    # Campos incluídos no construtor da classe
    # --------------------------------------------------------------------------
    descricao: str = field(repr=True, compare=True, init=True)
    id_plano_de_contas: UUID = field(repr=True, compare=True, init=True)
    id_conta: UUID = field(repr=True, compare=True, init=True)
    id_cartao_de_credito: UUID = field(repr=True, compare=True, init=True)
    id_centro_de_custo: UUID = field(repr=True, compare=True, init=True)
    # Campos com valor default devem ser os últimos
    data_do_lancamento: date = field(
        repr=True, compare=True, init=True, default=dtu.date_now_brasilia()
    )
    data_do_vencimento: date = field(
        repr=True, compare=True, init=True, default=dtu.date_now_brasilia()
    )
    tipo_de_moeda: str = field(repr=False, compare=False, init=True, default="BRL")
    valor: float = field(repr=False, compare=False, init=True, default=1.0)
    descricao_situacao_do_lancamento: str = field(
        repr=False, compare=False, init=True, default="A Receber"
    )
    descricao_tipo_de_lancamento: str = field(
        repr=False, compare=False, init=True, default="Lançamento de Receita"
    )

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    valor_do_lancamento: VOMoeda = field(repr=True, compare=False, init=False)
    situacao_do_lancamento: SituacoesDosLancamentos = field(
        repr=True, compare=False, init=False
    )
    tipo_de_lancamento: TiposDeLancamentos = field(repr=True, compare=False, init=False)
    # Campos com valor default devem ser os últimos
    id_lancamento: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    vencido: bool = field(repr=True, compare=False, init=False, default=False)
    ano_mes_orcamento: str = field(
        repr=True,
        compare=False,
        init=False,
        default=dtu.date_now_brasilia().strftime("%Y-%m"),
    )
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        # Trata o Value Object Valor do Lançamento
        if is_null_or_empty(self.tipo_de_moeda):
            aux_tipo_de_moeda = "BRL"
        else:
            aux_tipo_de_moeda = self.tipo_de_moeda

        if is_null_or_empty(self.valor):
            aux_valor = 1
        else:
            aux_valor = self.valor
        self.valor_do_lancamento = VOMoeda(aux_valor, TiposDeMoedas[aux_tipo_de_moeda])

        # Trata o enum Situação do Lançamento
        if is_null_or_empty(self.descricao_situacao_do_lancamento):
            self.situacao_do_lancamento = SituacoesDosLancamentos.A_RECEBER
        else:
            self.situacao_do_lancamento = SituacoesDosLancamentos(
                self.descricao_situacao_do_lancamento
            )

        # Trata o enum Tipo de Lançamento
        if is_null_or_empty(self.descricao_tipo_de_lancamento):
            self.tipo_de_lancamento = TiposDeLancamentos.RECEITA
        else:
            self.tipo_de_lancamento = TiposDeLancamentos(
                self.descricao_tipo_de_lancamento
            )
        # Gera o indicador de lançamento vencido
        if (self.situacao_do_lancamento == SituacoesDosLancamentos.A_PAGAR) or (
            self.situacao_do_lancamento == SituacoesDosLancamentos.A_RECEBER
        ):
            if self.data_do_vencimento <= dtu.date_now_brasilia():
                self.vencido = True
            else:
                self.vencido = False
        else:
            self.vencido = False

        # Gera o formato para análise de previsto / realizado no orçamento
        self.ano_mes_orcamento = self.data_do_vencimento.strftime("%Y-%m")

    def __str__(self):
        repr = "ID: {} - Data do Vencimento: {} - Descrição: {} - Valor: {}"

        return repr.format(
            self.id_lancamento,
            dtu.date_dd_mm_yyyy(self.data_do_vencimento),
            self.descricao,
            self.valor_do_lancamento.formatada,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Lancamentos):
            return False

        return (
            (self.id_lancamento == other.id_lancamento)
            and (self.descricao == other.descricao)
            and (self.id_plano_de_contas == other.id_plano_de_contas)
            and (self.id_conta == other.id_conta)
            and (self.id_cartao_de_credito == other.id_cartao_de_credito)
            and (self.id_centro_de_custo == other.id_centro_de_custo)
            and (
                self.valor_do_lancamento.formatada
                == other.valor_do_lancamento.formatada
            )
            and (self.data_do_lancamento == other.data_do_lancamento)
            and (self.data_do_vencimento == other.data_do_vencimento)
        )
