#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_centros_de_custo.py
@Created :   11/12/2024 13:04:27
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Casos de uso: Criar Centro de Custo, Atualizar Centro de Custo e
            Excluir Centro de Custo
    ============================================================================
"""

from typing import Type, List

from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.domain.entities.centros_de_custo import CentrosDeCusto
from src.domain.interfaces.centros_de_custo_repositorio_interface import (
    CentrosDeCustoRepositorioInterface,
)
from src.errors.centros_de_custo_errors import CentroDeCustoNaoInformado


class CriarCentroDeCusto:
    def __init_(self, repo: type[CentrosDeCustoRepositorioInterface]):
        self.repo = repo

    def execute(self, centro_de_custo: Type[CentrosDeCusto]) -> List[CentrosDeCusto]:
        if is_null_or_empty(centro_de_custo):
            raise CentroDeCustoNaoInformado("Centro de Custo não informado!")

        return self.repo.criar_centro_de_custo(centro_de_custo)


class AtualizarCentroDeCusto:
    def __init_(self, repo: type[CentrosDeCustoRepositorioInterface]):
        self.repo = repo

    def execute(self, centro_de_custo: Type[CentrosDeCusto]) -> bool:
        if is_null_or_empty(centro_de_custo):
            raise CentroDeCustoNaoInformado("Centro de Custo não informado!")

        return self.repo.atualizar_centro_de_custo(centro_de_custo)


class ExcluirCentroDeCusto:
    def __init_(self, repo: type[CentrosDeCustoRepositorioInterface]):
        self.repo = repo

    def execute(self, centro_de_custo: Type[CentrosDeCusto]) -> bool:
        if is_null_or_empty(centro_de_custo):
            raise CentroDeCustoNaoInformado("Centro de Custo não informado!")

        return self.repo.excluir_centro_de_custo(centro_de_custo)
