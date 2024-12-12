#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   contas_repositorio_interface.py
@Created :   10/12/2024 12:26:05
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface de repositório de Contas
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type, List
from uuid import UUID

from src.domain.entities.contas import Contas


class ContasRepositorioInterface(ABC):
    @abstractmethod
    def criar_conta(conta: Type[Contas]) -> Type[Contas]:
        pass

    @abstractmethod
    def atualizar_conta(conta: Type[Contas]) -> bool:
        pass

    @abstractmethod
    def excluir_conta(conta: Type[Contas]) -> bool:
        pass

    @abstractmethod
    def obter_conta_por_id(id_conta: Type[UUID]) -> Type[Contas]:
        pass

    @abstractmethod
    def obter_conta_por_sigla(sigla: str) -> Type[Contas]:
        pass

    @abstractmethod
    def obter_todas_contas() -> List[Contas]:
        pass
