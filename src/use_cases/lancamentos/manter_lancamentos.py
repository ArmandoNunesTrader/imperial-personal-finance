#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_lancamentos.py
@Created :   11/12/2024 13:19:01
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Casos de uso: Criar Lançamento, Atualizar Lançamento e
            Excluir Lançamento
    ============================================================================
"""

from typing import Type, List

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.lancamentos import Lancamentos
from src.domain.interfaces.lancamentos_repositorio_interface import (
    LancamentosRepositorioInterface,
)
from src.errors.lancamentos_errors import LancamentoNaoInformado


class CriarLancamento:
    def __init_(self, repo: type[LancamentosRepositorioInterface]):
        self.repo = repo

    def execute(self, lancamento: Type[Lancamentos]) -> List[Lancamentos]:
        if is_null_or_empty(lancamento):
            raise LancamentoNaoInformado("Lançamento não informado!")

        return self.repo.criar_lancamento(lancamento)


class AtualizarLancamento:
    def __init_(self, repo: type[LancamentosRepositorioInterface]):
        self.repo = repo

    def execute(self, lancamento: Type[Lancamentos]) -> bool:
        if is_null_or_empty(lancamento):
            raise LancamentoNaoInformado("Lançamento não informada!")

        return self.repo.atualizar_lancamento(lancamento)


class ExcluirLancamento:
    def __init_(self, repo: type[LancamentosRepositorioInterface]):
        self.repo = repo

    def execute(self, lancamento: Type[Lancamentos]) -> bool:
        if is_null_or_empty(lancamento):
            raise LancamentoNaoInformado("Lançamento não informada!")

        return self.repo.excluir_lancamento(lancamento)
