#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   plano_de_contas_repositorio_interface.py
@Created :   10/12/2024 12:34:28
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface de repositório de Plano de Contas
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type, List
from uuid import UUID

from src.domain.entities.plano_de_contas import PlanoDeContas


class PlanoDeContasRepositorioInterface(ABC):
    @abstractmethod
    def criar_plano_de_contas(
        plano_de_contas: Type[PlanoDeContas],
    ) -> Type[PlanoDeContas]:
        pass

    @abstractmethod
    def atualizar_plano_de_contas(plano_de_contas: Type[PlanoDeContas]) -> bool:
        pass

    @abstractmethod
    def excluir_plano_de_contas(plano_de_contas: Type[PlanoDeContas]) -> bool:
        pass

    @abstractmethod
    def obter_plano_de_contas_por_id(
        id_plano_de_contas: Type[UUID],
    ) -> Type[PlanoDeContas]:
        pass

    @abstractmethod
    def obter_plano_de_contas_por_descricao(descricao: str) -> Type[PlanoDeContas]:
        pass

    @abstractmethod
    def obter_subordinadas(plano_de_contas: Type[PlanoDeContas]) -> List[PlanoDeContas]:
        pass

    @abstractmethod
    def obter_conta_pai(plano_de_contas: Type[PlanoDeContas]) -> List[PlanoDeContas]:
        pass

    @abstractmethod
    def obter_todos_planos_de_contas() -> List[PlanoDeContas]:
        pass
