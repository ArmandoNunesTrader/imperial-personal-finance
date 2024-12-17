#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moeda.py
@Created :   07/12/2024 15:45:14
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Value Object para valores monetários
    ============================================================================
"""

from dataclasses import dataclass, field

from src.domain.enums.tipos_de_moedas import TiposDeMoedas

import src.utils.string_utils as stu


@dataclass(frozen=True)  # Garante que os atributos depois de criados, não mudam
class VOMoeda:
    def format_vo_moeda(self):
        if self.tipo_de_moeda == TiposDeMoedas.USD:
            return "\N{dollar sign} " + "{:,.2f}".format(self.valor)
        elif self.tipo_de_moeda == TiposDeMoedas.EUR:
            return "\N{euro sign} " + "{:,.2f}".format(self.valor)
        else:  # if self.tipo_de_moeda is TiposDeMoedas.BRL:
            return stu.real_br_money_mask(self.valor)

    valor: float = field(default=1.00)
    tipo_de_moeda: TiposDeMoedas = field(default=TiposDeMoedas.BRL)

    @property
    def formatada(self) -> str:
        return self.format_vo_moeda()
