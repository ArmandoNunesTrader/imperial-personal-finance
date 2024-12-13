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
from src.errors.errors_handler import handler_errors
from src.errors.moedas_errors import MoedaNaoInformada

from src.utils.sanitize_utils import (
    sanitize_pt_br_phrase_capitalize,
    sanitize_pt_br_phrase_upper,
)


class CriarMoeda:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, moeda_dto_in: Type[MoedaDTOIn]) -> Type[Moedas] | str:
        if is_null_or_empty(moeda_dto_in):
            raise MoedaNaoInformada("Moeda não informada!")

        try:
            moedas_dto_in_validator(moeda_dto_in)
            obj_moeda = Moedas(
                sanitize_pt_br_phrase_capitalize(moeda_dto_in.to_dict()["sigla"]),
                sanitize_pt_br_phrase_capitalize(moeda_dto_in.to_dict()["descricao"]),
                sanitize_pt_br_phrase_upper(moeda_dto_in.to_dict()["tipo_de_moeda"]),
                moeda_dto_in.to_dict()["valor_da_paridade"],
            )
            return self.repo.criar_moeda(obj_moeda)
        except Exception as exception:
            result = handler_errors(exception)
            return json.dumps(result["body"]), result["status_code"]


class AtualizarMoeda:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, moeda: Type[Moedas]) -> bool:
        if is_null_or_empty(moeda):
            raise MoedaNaoInformada("Moeda não informada!")

        try:
            return self.repo.atualizar_moeda(moeda)
        except Exception as exception:
            result = handler_errors(exception)
            return json.dumps(result["body"]), result["status_code"]


class ExcluirMoeda:
    def __init__(self, repo: type[MoedasRepositorioInterface]):
        self.repo = repo

    def execute(self, moeda: Type[Moedas]) -> bool:
        if is_null_or_empty(moeda):
            raise MoedaNaoInformada("Moeda não informada!")

        return self.repo.excluir_moeda(moeda)
