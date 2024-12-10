#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_repositorio_interface.py
@Created :   10/12/2024 12:39:28
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface de repositório de Moedas
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type, List
from uuid import UUID

from src.domain.entities.moedas import Moedas


class MoedasRepositorioInterface(ABC):
    @abstractmethod
    def criar_moeda(moeda: Type[Moedas]) -> Moedas:
        pass

    @abstractmethod
    def atualizar_moeda(moeda: Type[Moedas]) -> bool:
        pass

    @abstractmethod
    def excluir_moeda(moeda: Type[Moedas]) -> bool:
        pass

    @abstractmethod
    def obter_moeda_por_id(id_moeda: Type[UUID]) -> List[Moedas]:
        pass

    @abstractmethod
    def obter_moeda_por_sigla(sigla: str) -> List[Moedas]:
        pass
