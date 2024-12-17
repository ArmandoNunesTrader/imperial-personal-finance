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


from src.errors.moedas_errors import MoedasException, MoedaNotFound
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.domain.entities.moedas import Moedas


class ObterTodasAsMoedas:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self) -> List[Moedas] | bool:
        try:
            result = self.repo.obter_todas_moedas()
            if result == []:
                raise MoedaNotFound()
            else:
                return result
        except MoedaNotFound as exception:
            raise exception
        except Exception as exception:
            raise MoedasException(str(exception), 500)
