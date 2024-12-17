#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_contas copy.py
@Created :   11/12/2024 13:15:53
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Casos de uso: Criar Conta, Atualizar Conta e Excluir Conta
    ============================================================================
"""

from typing import Type, List

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.contas import Contas
from src.domain.interfaces.contas_repositorio_interface import (
    ContasRepositorioInterface,
)
from src.errors.contas_errors import ContaNaoInformada


class CriarConta:
    def __init_(self, repo: type[ContasRepositorioInterface]):
        self.repo = repo

    def execute(self, conta: Type[Contas]) -> List[Contas]:
        if is_null_or_empty(conta):
            raise ContaNaoInformada("Conta não informada!")

        return self.repo.criar_conta(conta)


class AtualizarConta:
    def __init_(self, repo: type[ContasRepositorioInterface]):
        self.repo = repo

    def execute(self, conta: Type[Contas]) -> bool:
        if is_null_or_empty(conta):
            raise ContaNaoInformada("Conta não informada!")

        return self.repo.atualizar_conta(conta)


class ExcluirConta:
    def __init_(self, repo: type[ContasRepositorioInterface]):
        self.repo = repo

    def execute(self, conta: Type[Contas]) -> bool:
        if is_null_or_empty(conta):
            raise ContaNaoInformada("Conta não informada!")

        return self.repo.excluir_conta(conta)
