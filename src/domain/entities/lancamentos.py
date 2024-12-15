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
import src.utils.math_utils as mtu


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
    _tipo_de_moeda: str = field(
        repr=False, compare=False, init=True, default="Real Brasileiro"
    )
    _valor_do_lancamento: float = field(
        repr=False, compare=False, init=True, default=1.0
    )
    _situacao_do_lancamento: str = field(
        repr=False, compare=False, init=True, default="A Receber"
    )
    _tipo_de_lancamento: str = field(
        repr=False, compare=False, init=True, default="Lançamento de Receita"
    )

    # Campos que não aparecerão no construtor da classe
    # --------------------------------------------------------------------------
    # Campos com valor default devem ser os últimos
    id_lancamento: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    created_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )
    updated_at: datetime = field(
        repr=True, compare=True, init=False, default=dtu.dt_now_utc()
    )

    @property
    def valor_do_lancamento(self) -> VOMoeda:
        if (is_null_or_empty(self._tipo_de_moeda)) or (
            self._tipo_de_moeda not in TiposDeMoedas.all_values()
        ):
            aux_tipo_de_moeda = Lancamentos._tipo_de_moeda
        else:
            aux_tipo_de_moeda = self._tipo_de_moeda
        if mtu.is_float(self._valor_do_lancamento):
            aux_valor_do_lancamento = float(self._valor_do_lancamento)
        else:
            aux_valor_do_lancamento = Lancamentos._valor_do_lancamento
        return VOMoeda(aux_valor_do_lancamento, TiposDeMoedas(aux_tipo_de_moeda))

    @valor_do_lancamento.setter
    def valor_do_lancamento(self, value: VOMoeda) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._valor_do_lancamento = (
                Lancamentos._valor_do_lancamento
            )  # pragma: no cover
        else:
            self._tipo_de_moeda = value.tipo_de_moeda
            self._valor_do_lancamento = float(value.valor)

    @property
    def situacao_do_lancamento(self) -> SituacoesDosLancamentos:
        if is_null_or_empty(self._situacao_do_lancamento) or (
            self._situacao_do_lancamento not in SituacoesDosLancamentos.all_values()
        ):
            aux_situacao_do_lancamento = Lancamentos._situacao_do_lancamento
        else:
            aux_situacao_do_lancamento = self._situacao_do_lancamento

        return SituacoesDosLancamentos(aux_situacao_do_lancamento)

    @situacao_do_lancamento.setter
    def situacao_do_lancamento(self, value: SituacoesDosLancamentos) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._situacao_do_lancamento = (
                Lancamentos._situacao_do_lancamento
            )  # pragma: no cover
        else:
            self._situacao_do_lancamento = value.value

    @property
    def tipo_de_lancamento(self) -> TiposDeLancamentos:
        if is_null_or_empty(self._tipo_de_lancamento) or (
            self._tipo_de_lancamento not in TiposDeLancamentos.all_values()
        ):
            aux_tipo_de_lancamento = Lancamentos._tipo_de_lancamento
        else:
            aux_tipo_de_lancamento = self._tipo_de_lancamento

        return TiposDeLancamentos(aux_tipo_de_lancamento)

    @tipo_de_lancamento.setter
    def tipo_de_lancamento(self, value: TiposDeLancamentos) -> None:
        # Se o valor inicial não for especificado, usa o default
        if type(value) is property:
            self._tipo_de_lancamento = (
                Lancamentos._tipo_de_lancamento
            )  # pragma: no cover
        else:
            self._tipo_de_lancamento = value.value

    @property
    def vencido(self) -> bool:
        if (self.situacao_do_lancamento == SituacoesDosLancamentos.A_PAGAR) or (
            self.situacao_do_lancamento == SituacoesDosLancamentos.A_RECEBER
        ):
            if self.data_do_vencimento <= dtu.date_now_brasilia():
                return True
            else:
                return False
        else:
            return False

    @property
    def ano_mes_orcamento(self) -> str:
        return self.data_do_vencimento.strftime("%Y-%m")

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        pass

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
