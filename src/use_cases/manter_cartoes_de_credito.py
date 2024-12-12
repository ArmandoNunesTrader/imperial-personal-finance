#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_cartoes_de_credito.py
@Created :   11/12/2024 13:13:25
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Casos de uso: Criar Cartão de Crédito, Atualizar Cartão de Crédito e
            Excluir Cartão de Crédito
    ============================================================================
"""

from typing import Type, List

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.cartoes_de_credito import CartoesDeCredito
from src.domain.interfaces.cartoes_de_credito_repositorio_interface import (
    CartoesDeCreditoRepositorioInterface,
)
from src.errors.cartoes_de_credito_errors import CartaoDeCreditoNaoInformado


class CriarCartaoDeCredito:
    def __init_(self, repo: type[CartoesDeCreditoRepositorioInterface]):
        self.repo = repo

    def execute(
        self, cartao_de_credito: Type[CartoesDeCredito]
    ) -> List[CartoesDeCredito]:
        if is_null_or_empty(cartao_de_credito):
            raise CartaoDeCreditoNaoInformado("Cartão de Crédito não informado!")

        return self.repo.criar_cartao_de_credito(cartao_de_credito)


class AtualizarCartaoDeCredito:
    def __init_(self, repo: type[CartoesDeCreditoRepositorioInterface]):
        self.repo = repo

    def execute(self, cartao_de_credito: Type[CartoesDeCredito]) -> bool:
        if is_null_or_empty(cartao_de_credito):
            raise CartaoDeCreditoNaoInformado("Cartão de Crédito não informado!")

        return self.repo.atualizar_cartao_de_credito(cartao_de_credito)


class ExcluirCartaoDeCredito:
    def __init_(self, repo: type[CartoesDeCreditoRepositorioInterface]):
        self.repo = repo

    def execute(self, cartao_de_credito: Type[CartoesDeCredito]) -> bool:
        if is_null_or_empty(cartao_de_credito):
            raise CartaoDeCreditoNaoInformado("Cartão de Crédito não informado!")

        return self.repo.excluir_cartao_de_credito(cartao_de_credito)
