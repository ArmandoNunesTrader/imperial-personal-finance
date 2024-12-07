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

from src.domain.value_objects.moeda import Moeda as VO_Moeda
from src.domain.enums.situacoes_dos_lancamentos import SituacoesDosLancamentos
from src.domain.enums.tipos_de_lancamentos import TiposDeLancamentos

import src.utils.datetime_utils as dtu


@dataclass
class Lancamentos:
    id_lancamento: UUID = field(default_factory=uuid4)
    data_do_lancamento: date = field(default=dtu.date_now_brasilia())
    data_do_vencimento: date = field(default=dtu.date_now_brasilia())
    valor_do_lancamento: VO_Moeda = field(default=VO_Moeda())
    descricao: str = field(default="Lançamento")
    id_plano_de_contas: UUID = field(default=None)
    id_conta: UUID = field(default=None)
    id_cartao_de_credito: UUID = field(default=None)
    id_centro_de_custo: UUID = field(default=None)
    situacao_do_lancamento: SituacoesDosLancamentos = field(
        default=SituacoesDosLancamentos.A_RECEBER
    )
    tipo_de_lancamento: TiposDeLancamentos = field(default=TiposDeLancamentos.RECEITA)
    created_at: datetime = field(default=dtu.dt_now_utc())
    updated_at: datetime = field(default=dtu.dt_now_utc())

    # Necessário para o funcionamento do __repr__ que é criado automaticamente
    def __str__(self):
        repr = "ID: {} - Data do Vencimento: {} - Descrição: {} - Valor: {}"

        return repr.format(
            self.id_lancamento,
            dtu.date_dd_mm_yyyy(self.data_do_vencimento),
            self.descricao,
            self.valor_do_lancamento.formatada,
        )
