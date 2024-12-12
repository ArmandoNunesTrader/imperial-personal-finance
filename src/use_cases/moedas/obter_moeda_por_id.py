#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_id.py
@Created :   11/12/2024 19:33:34
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Caso de uso Obter Moeda por ID da entidade Moedas
    ============================================================================
"""

from typing import Type
from uuid import UUID

import json

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.moedas import Moedas
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.errors.errors_handler import handler_errors
from src.errors.moedas_errors import MoedaIdNaoInformado


class ObterMoedaPorId:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, id_moeda: Type[UUID]) -> Type[Moedas] | str:
        if is_null_or_empty(id_moeda):
            raise MoedaIdNaoInformado("Identificador da Moeda não informado!")

        if isinstance(id_moeda, UUID) is True:
            try:
                return self.repo.obter_moeda_por_id(id_moeda)
            except Exception as exception:
                result = handler_errors(exception)
                return json.dumps(result["body"]), result["status_code"]

        raise MoedaIdNaoInformado("Identificador da Moeda informado não é válido!")
