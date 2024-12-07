#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   Moeda.py
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


def real_br_money_mask(my_value):
    a = "{:,.2f}".format(float(my_value))
    b = a.replace(",", "v")
    c = b.replace(".", ",")
    return c.replace("v", ".")


@dataclass(frozen=True)  # Garante que os atributos depois de criados, não mudam
class Moeda:
    valor: float = field(default=1.00)
    tipo_de_moeda: TiposDeMoedas = field(default=TiposDeMoedas.BRL)

    @property
    def formatada(self) -> str:
        if self.tipo_de_moeda is TiposDeMoedas.BRL:
            return "R$ " + real_br_money_mask(self.valor)
        elif self.tipo_de_moeda == TiposDeMoedas.USD:
            return "\N{dollar sign} " + "{:,.2f}".format(self.valor)
        elif self.tipo_de_moeda == TiposDeMoedas.EUR:
            return "\N{euro sign} " + "{:,.2f}".format(self.valor)
