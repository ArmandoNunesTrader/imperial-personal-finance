#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_plano_de_contas.py
@Created :   11/12/2024 13:11:26
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Casos de uso: Criar Plano de Contas, Atualizar Plano de Contas e
            Excluir Plano de Contas
    ============================================================================
"""

from typing import Type, List

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.plano_de_contas import PlanoDeContas
from src.domain.interfaces.plano_de_contas_repositorio_interface import (
    PlanoDeContasRepositorioInterface,
)
from src.errors.plano_de_contas_errors import PlanoDeContasNaoInformado


class CriarPlanoDeContas:
    def __init_(self, repo: type[PlanoDeContasRepositorioInterface]):
        self.repo = repo

    def execute(self, plano_de_contas: Type[PlanoDeContas]) -> List[PlanoDeContas]:
        if is_null_or_empty(plano_de_contas):
            raise PlanoDeContasNaoInformado("Plano de Contas não informado!")

        return self.repo.criar_plano_de_contas(plano_de_contas)


class AtualizarPlanoDeContas:
    def __init_(self, repo: type[PlanoDeContasRepositorioInterface]):
        self.repo = repo

    def execute(self, plano_de_contas: Type[PlanoDeContas]) -> bool:
        if is_null_or_empty(plano_de_contas):
            raise PlanoDeContasNaoInformado("Plano de Contas não informado!")

        return self.repo.atualizar_plano_de_contas(plano_de_contas)


class ExcluirPlanoDeContas:
    def __init_(self, repo: type[PlanoDeContasRepositorioInterface]):
        self.repo = repo

    def execute(self, plano_de_contas: Type[PlanoDeContas]) -> bool:
        if is_null_or_empty(plano_de_contas):
            raise PlanoDeContasNaoInformado("Plano de Contas não informado!")

        return self.repo.excluir_plano_de_contas(plano_de_contas)
