#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_moedas.py
@Created :   11/12/2024 12:42:22
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Casos de uso: Criar Moeda, Atualizar Moeda e Excluir Moeda
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
from src.use_cases.validators.moedas_validators import (
    moedas_dto_in_validator_id,
    moedas_dto_in_validator_full,
)
from src.use_cases.moedas.serializers_moeda import dto_in_to_entity
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId
from src.use_cases.moedas.obter_moeda_por_sigla import ObterMoedaPorSigla
from src.errors.moedas_errors import (
    MoedasException,
    MoedaNaoInformada,
    MoedaAlteracaoOK,
    MoedaExclusaoOK,
    MoedaIdNaoLocalizado,
    MoedaSiglaJaCadastrada,
    MoedaSiglaNaoLocalizada,
)


import src.utils.datetime_utils as dtu


class CriarMoeda:
    def __init__(self, repo: Type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, dto_in: Type[MoedaDTOIn]) -> Type[Moedas]:
        if is_null_or_empty(dto_in):
            raise MoedaNaoInformada()

        dto_in = sanitize(dto_in)

        moedas_dto_in_validator_full(dto_in)
        try:
            # Previne a duplicidade de siglas
            try:
                if isinstance(ObterMoedaPorSigla(self.repo).execute(dto_in), Moedas):
                    raise MoedaSiglaJaCadastrada()
            except MoedaSiglaNaoLocalizada as exception:  # noqa F841
                pass

            obj_moeda = dto_in_to_entity(dto_in, False)

            return self.repo.criar_moeda(obj_moeda)
        except MoedaSiglaJaCadastrada as exception:
            raise exception
        except Exception as exception:
            raise MoedasException(str(exception), 500)


class AtualizarMoeda:
    def __init__(self, repo: Type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, dto_in: Type[MoedaDTOIn]) -> None:
        if is_null_or_empty(dto_in):
            raise MoedaNaoInformada()

        dto_in = sanitize(dto_in)

        moedas_dto_in_validator_full(dto_in)
        try:
            # Busca o objeto a alterar
            try:
                ObterMoedaPorId(self.repo).execute(dto_in)
            except MoedaIdNaoLocalizado as exception:  # noqa F841
                raise MoedaIdNaoLocalizado

            # Previne a duplicidade de siglas
            try:
                obj_check = ObterMoedaPorSigla(self.repo).execute(dto_in)
                exists = str(obj_check.id_moeda) != dto_in.to_dict()["id_moeda"]
                if isinstance(obj_check, Moedas) and exists:
                    raise MoedaSiglaJaCadastrada
            except MoedaSiglaNaoLocalizada as exception:  # noqa F841
                pass
            except MoedaSiglaJaCadastrada as exception:  # noqa F841
                raise MoedaSiglaJaCadastrada

            obj_moeda = dto_in_to_entity(dto_in, True)
            obj_moeda.updated_at = dtu.dt_now_utc()

            result = self.repo.atualizar_moeda(obj_moeda)
            if result is True:
                raise MoedaAlteracaoOK()
        except MoedaAlteracaoOK as exception:
            raise exception
        except MoedaIdNaoLocalizado as exception:
            raise exception
        except MoedaSiglaJaCadastrada as exception:
            raise exception
        except Exception as exception:
            raise MoedasException(str(exception), 500)


class ExcluirMoeda:
    def __init__(self, repo: Type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, dto_in: Type[MoedaDTOIn]) -> None:
        if is_null_or_empty(dto_in):
            raise MoedaNaoInformada()

        dto_in = sanitize(dto_in)

        moedas_dto_in_validator_id(dto_in)
        try:
            # Busca o objeto a alterar
            obj_moeda = ObterMoedaPorId(self.repo).execute(dto_in)

            result = self.repo.excluir_moeda(obj_moeda)
            if result is True:
                raise MoedaExclusaoOK()
        except MoedaExclusaoOK as exception:
            raise exception
        except MoedaIdNaoLocalizado as exception:
            raise exception
        except Exception as exception:
            raise MoedasException(str(exception), 500)
