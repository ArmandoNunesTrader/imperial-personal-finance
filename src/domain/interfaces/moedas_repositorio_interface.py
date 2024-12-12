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
    def criar_moeda(cls, moeda: Type[Moedas]) -> Type[Moedas] | None:
        pass

    @abstractmethod
    def atualizar_moeda(cls, moeda: Type[Moedas]) -> bool:
        pass

    @abstractmethod
    def excluir_moeda(cls, moeda: Type[Moedas]) -> bool:
        pass

    @abstractmethod
    def obter_moeda_por_id(id_moeda: Type[UUID]) -> Type[Moedas]:
        pass

    @abstractmethod
    def obter_moeda_por_sigla(sigla: str) -> Type[Moedas]:
        pass

    @abstractmethod
    def obter_todas_moedas() -> List[Moedas]:
        pass
