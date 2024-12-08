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
from src.domain.value_objects.moeda import Moeda as VO_Moeda

import src.utils.datetime_utils as dtu


@dataclass
class Lancamentos:
    descricao: str = field(repr=True, compare=True)
    id_plano_de_contas: UUID = field(repr=True, compare=True)
    id_conta: UUID = field(repr=True, compare=True)
    id_cartao_de_credito: UUID = field(repr=True, compare=True)
    id_centro_de_custo: UUID = field(repr=True, compare=True)
    # Campos com valor default devem ser os últimos
    tipo_de_moeda: str = field(repr=False, compare=False, default="BRL")
    valor: float = field(repr=False, compare=False, default=1.0)
    id_lancamento: UUID = field(
        repr=True, compare=True, init=False, default_factory=uuid4
    )
    data_do_lancamento: date = field(
        repr=True, compare=True, init=True, default=dtu.date_now_brasilia()
    )
    data_do_vencimento: date = field(
        repr=True, compare=True, init=True, default=dtu.date_now_brasilia()
    )
    descricao_situacao_do_lancamento: str = field(
        repr=False, compare=False, default="A Receber"
    )
    descricao_tipo_de_lancamento: str = field(
        repr=False, compare=False, default="Lançamento de Receita"
    )
    valor_do_lancamento: VO_Moeda = field(repr=True, compare=False, init=False)
    situacao_do_lancamento: SituacoesDosLancamentos = field(
        repr=True, compare=False, init=False
    )
    tipo_de_lancamento: TiposDeLancamentos = field(repr=True, compare=False, init=False)
    created_at: datetime = field(default=dtu.dt_now_utc())
    updated_at: datetime = field(default=dtu.dt_now_utc())

    # Manipulação de campos para compor o estado inicial da classe
    def __post_init__(self):
        # Trata o Value Object Valor do Documento
        if is_null_or_empty(self.tipo_de_moeda):
            aux_tipo_de_moeda = "BRL"
        else:
            aux_tipo_de_moeda = self.tipo_de_moeda

        if is_null_or_empty(self.valor):
            aux_valor = 1
        else:
            aux_valor = self.valor
        self.valor_do_lancamento = VO_Moeda(aux_valor, TiposDeMoedas[aux_tipo_de_moeda])

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

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Data do Vencimento: {} - Descrição: {} - Valor: {}"

        return repr.format(
            self.id_lancamento,
            dtu.date_dd_mm_yyyy(self.data_do_vencimento),
            self.descricao,
            self.valor_do_lancamento.formatada,
        )
