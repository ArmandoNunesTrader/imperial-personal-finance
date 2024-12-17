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

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.errors.moedas_errors import (
    MoedasException,
    MoedaIdNaoInformado,
    MoedaIdNaoLocalizado,
)
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.domain.entities.moedas import Moedas
from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.validators.moedas_validators import moedas_dto_in_validator_id
from src.use_cases.moedas.sanitize_dto_moeda import sanitize_dto_moeda as sanitize


class ObterMoedaPorId:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, dto_in: Type[MoedaDTOIn]) -> Type[Moedas]:
        dto_in = sanitize(dto_in)
        if ("id_moeda" not in dto_in.to_dict()) or is_null_or_empty(
            dto_in.to_dict()["id_moeda"]
        ):
            raise MoedaIdNaoInformado()

        moedas_dto_in_validator_id(dto_in)

        try:
            id_moeda_uuid = UUID(dto_in.to_dict()["id_moeda"])
            result = self.repo.obter_moeda_por_id(id_moeda_uuid)
            if result is None:
                raise MoedaIdNaoLocalizado()
            else:
                return result
        except MoedaIdNaoLocalizado as exception:
            raise exception
        except Exception as exception:
            raise MoedasException(str(exception), 500)
