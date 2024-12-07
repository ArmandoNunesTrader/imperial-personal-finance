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

from src.domain.entities.moedas import Moedas
from src.domain.enums.situacoes_dos_lancamentos import SituacoesDosLancamentos
from src.domain.enums.tipos_de_lancamentos import TiposDeLancamentos

import src.utils.datetime_utils as dtu


@dataclass
class PlanoDeContas:
    id_lancamento: UUID = field(default_factory=uuid4)
    data_do_lancamento: date = field(default=dtu.date_now_brasilia)
    data_do_vencimento: date = field(default=dtu.date_now_brasilia)
    valor_do_lancamento: Moedas
    descricao: str
    id_plano_de_contas: UUID
    id_conta: UUID
    id_cartao_de_credito: UUID
    id_centro_de_custo: UUID
    situacao_do_lancamento: SituacoesDosLancamentos = field(
        default=SituacoesDosLancamentos.a_receber.value
    )
    tipo_de_lancamento: TiposDeLancamentos = field(
        default=TiposDeLancamentos.receita.value
    )
    created_at: datetime = field(default_factory=dtu.dt_now_utc())
    updated_at: datetime = field(default_factory=dtu.dt_now_utc())

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Data do Vencimento: {} - Descrição: {} - Valor: {}"

        return repr.format(
            self.id_lancamento,
            self.data_do_lancamento.strftime("%d-%m-%Y"),
            self.valor_do_lancamento,
        )
