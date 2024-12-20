#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   dto_moedas.py
@Created :   11/12/2024 13:31:16
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classes DTO da entidade Moedas
    ============================================================================
"""
from typing import Dict


class MoedaDTOIn:
    def __init__(self, **kwargs):
        if "id_moeda" in kwargs:
            self.id_moeda = kwargs.get("id_moeda", None)
        self.sigla = kwargs.get("sigla", None)
        self.descricao = kwargs.get("descricao", None)
        self._tipo_de_moeda = kwargs.get("_tipo_de_moeda", None)
        self._valor_da_paridade = kwargs.get("_valor_da_paridade", None)

    def to_dict(self) -> Dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(**dict_obj)
