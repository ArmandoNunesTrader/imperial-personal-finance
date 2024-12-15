#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_sigla.py
@Created :   11/12/2024 19:33:34
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Caso de uso Obter Moeda por Sigla da entidade Moedas
    ============================================================================
"""

from typing import Type

import json

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.moedas import Moedas
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.errors.errors_handler import handler_errors
from src.errors.moedas_errors import MoedaSiglaNaoInformada, MoedasException


class ObterMoedaPorSigla:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, sigla: str) -> Type[Moedas] | str:
        if is_null_or_empty(sigla):
            raise MoedaSiglaNaoInformada()

        if isinstance(sigla, str) is True:
            try:
                return self.repo.obter_moeda_por_sigla(sigla)
            except Exception as exception:
                result = handler_errors(exception)
                raise MoedasException(json.dumps(result["body"]), result["status_code"])

        raise MoedaSiglaNaoInformada()
