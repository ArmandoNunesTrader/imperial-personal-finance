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

import json

from src.domain.entities.moedas import Moedas
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)
from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.use_cases.validators.moedas_validators import moedas_dto_in_validator
from src.use_cases.moedas.obter_moeda_por_sigla import ObterMoedaPorSigla
from src.errors.errors_handler import handler_errors
from src.errors.moedas_errors import (
    MoedasException,
    MoedaNaoInformada,
    MoedaSiglaJaCadastrada,
    MoedaErrosDeValidacao,
)

from src.utils.sanitize_utils import (
    sanitize_pt_br_phrase_capitalize,
    sanitize_pt_br_phrase_upper,
)

import src.utils.datetime_utils as dtu


"""
    Criar Moeda:
        Possiveis retornos:
            Objeto da Entidade Moeda
            Strins com a mensagem de Erro
            Exception
"""


class CriarMoeda:
    def __init__(self, repo: Type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, moeda_dto_in: Type[MoedaDTOIn]) -> Type[Moedas] | str:
        if is_null_or_empty(moeda_dto_in):
            raise MoedaNaoInformada("Moeda não informada!")

        # Verifica a existência da sigla para evitar duplicidade
        if not is_null_or_empty(moeda_dto_in.to_dict()["sigla"]):
            sigla_check_dup = sanitize_pt_br_phrase_capitalize(
                moeda_dto_in.to_dict()["sigla"]
            )
            obj_moeda_sigla = ObterMoedaPorSigla(self.repo).execute(sigla_check_dup)
            if isinstance(obj_moeda_sigla, Moedas):
                raise MoedaSiglaJaCadastrada("Sigla da Moeda já cadastrada!")

        try:
            sanitized_sigla = sanitize_pt_br_phrase_capitalize(
                moeda_dto_in.to_dict()["sigla"]
            )
            sanitized_descricao = sanitize_pt_br_phrase_capitalize(
                moeda_dto_in.to_dict()["descricao"]
            )
            sanitized_tipo_de_moeda = sanitize_pt_br_phrase_upper(
                moeda_dto_in.to_dict()["tipo_de_moeda"]
            )
            dict_sanitized = {
                "sigla": sanitized_sigla,
                "descricao": sanitized_descricao,
                "tipo_de_moeda": sanitized_tipo_de_moeda,
                "valor_da_paridade": moeda_dto_in.valor_da_paridade,
            }

            moedas_dto_in_validator(MoedaDTOIn().from_dict(dict_sanitized))

            obj_moeda = Moedas(
                sanitized_sigla,
                sanitized_descricao,
                sanitized_tipo_de_moeda,
                moeda_dto_in.valor_da_paridade,
            )
            return self.repo.criar_moeda(obj_moeda)
        except MoedaErrosDeValidacao as exception:
            raise exception
        except Exception as exception:
            result = handler_errors(exception)
            raise MoedasException(json.dumps(result["body"]), result["status_code"])


class AtualizarMoeda:
    def __init__(self, repo: Type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, moeda: Type[Moedas]) -> bool:
        if is_null_or_empty(moeda):
            raise MoedaNaoInformada("Moeda não informada!")

        # Verifica a existência da sigla para evitar duplicidade
        if not is_null_or_empty(moeda.sigla):
            sigla_check_dup = sanitize_pt_br_phrase_capitalize(moeda.sigla)
            obj_moeda_sigla_dup = ObterMoedaPorSigla(self.repo).execute(sigla_check_dup)
            if isinstance(obj_moeda_sigla_dup, Moedas) and (
                obj_moeda_sigla_dup.id_moeda != moeda.id_moeda
            ):
                raise MoedaSiglaJaCadastrada("Sigla da Moeda já cadastrada!")

        try:
            moeda.sigla = sanitize_pt_br_phrase_capitalize(moeda.sigla)
            moeda.descricao = sanitize_pt_br_phrase_capitalize(moeda.descricao)
            moeda.tipo_de_moeda = sanitize_pt_br_phrase_upper(moeda.tipo_de_moeda)
            moeda.updated_at = dtu.dt_now_utc()

            moedas_dto_in_validator(moeda=moeda)

            return self.repo.atualizar_moeda(moeda)
        except Exception as exception:
            result = handler_errors(exception)
            return json.dumps(result["body"]), result["status_code"]


class ExcluirMoeda:
    def __init__(self, repo: Type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, moeda: Type[Moedas]) -> bool:
        if is_null_or_empty(moeda):
            raise MoedaNaoInformada("Moeda não informada!")

        return self.repo.excluir_moeda(moeda)
