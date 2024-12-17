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


from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.moedas import Moedas
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.moedas.sanitize_dto_moeda import sanitize_dto_moeda as sanitize
from src.use_cases.validators.moedas_validators import moedas_dto_in_validator_sigla
from src.errors.moedas_errors import (
    MoedasException,
    MoedaSiglaNaoInformada,
)


class ObterMoedaPorSigla:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, dto_in: Type[MoedaDTOIn]) -> Type[Moedas] | bool:
        dto_in = sanitize(dto_in)
        if ("sigla" not in dto_in.to_dict()) or is_null_or_empty(
            dto_in.to_dict()["sigla"]
        ):
            raise MoedaSiglaNaoInformada()

        moedas_dto_in_validator_sigla(dto_in)

        try:
            result = self.repo.obter_moeda_por_sigla(dto_in.to_dict()["sigla"])
            if result is None:
                return False
            else:
                return result
        except Exception as exception:
            raise MoedasException(str(exception), 500)
