#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_mock.py
@Created :   11/12/2024 18:41:10
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Repositório mockado da entidade Moedas
    ============================================================================
"""
from uuid import UUID
from typing import Type, List

from src.domain.entities.moedas import Moedas
from src.domain.interfaces.moedas_repositorio_interface import (
    MoedasRepositorioInterface,
)

obj_mock_1 = Moedas(
    "Primeira Moeda", "Primeira Moeda de Teste", "Real Brasileiro", 1.00
)
obj_mock_2 = Moedas("Segunda Moeda", "Segunda Moeda de Teste", "Dólar Americano", 4.56)
obj_mock_3 = Moedas("Terceira Moeda", "Terceira Moeda de Teste", "Euro", 6.78)


class MoedasRepositorio(MoedasRepositorioInterface):
    def __init__(self):
        self.repo = []
        self.repo.append({obj_mock_1.id_moeda: obj_mock_1})
        self.repo.append({obj_mock_2.id_moeda: obj_mock_2})
        self.repo.append({obj_mock_3.id_moeda: obj_mock_3})

    def criar_moeda(self, moeda: Type[Moedas]) -> Type[Moedas] | None:
        self.repo.append({moeda.id_moeda: moeda})
        return moeda

    def atualizar_moeda(self, moeda: Type[Moedas]) -> bool:
        for ind in range(len(self.repo)):
            for key in self.repo[ind]:
                if self.repo[ind][key].id_moeda == moeda.id_moeda:
                    self.repo[ind][key] = moeda
        return True

    def excluir_moeda(self, moeda: Type[Moedas]) -> bool:
        for ind in range(len(self.repo)):
            for key in self.repo[ind]:
                if self.repo[ind][key].id_moeda == moeda.id_moeda:
                    del self.repo[ind][key]
                    break
        return True

    def obter_moeda_por_id(self, id_moeda: Type[UUID]) -> Type[Moedas]:
        for ind in range(len(self.repo)):
            for key in self.repo[ind]:
                if str(self.repo[ind][key].id_moeda) == str(id_moeda):
                    return self.repo[ind][key]
        return None

    def obter_moeda_por_sigla(self, sigla: str) -> Type[Moedas]:
        for ind in range(len(self.repo)):
            for key in self.repo[ind]:
                if self.repo[ind][key].sigla == sigla:
                    return self.repo[ind][key]
        return None

    def obter_todas_moedas(self) -> List[Moedas]:
        result = []
        for ind in range(len(self.repo)):
            for key in self.repo[ind]:
                result.append(self.repo[ind][key])

        return result
