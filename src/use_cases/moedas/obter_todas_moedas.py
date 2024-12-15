#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_todas_moedas.py
@Created :   12/12/2024 12:01:44
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Caso de uso Obter Todas as Moedas
    ============================================================================
"""

from typing import List

import json

from src.domain.entities.moedas import Moedas
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.errors.errors_handler import handler_errors
from src.errors.moedas_errors import MoedasException


class ObterTodasAsMoedas:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self) -> List[Moedas] | str:
        try:
            return self.repo.obter_todas_moedas()
        except Exception as exception:
            result = handler_errors(exception)
            raise MoedasException(json.dumps(result["body"]), result["status_code"])
