#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   lancamentos_repositorio_interface.py
@Created :   10/12/2024 12:44:07
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface de repositório de Lançamentos
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type, List
from uuid import UUID

from src.domain.entities.lancamentos import Lancamentos


class LancamentosRepositorioInterface(ABC):
    @abstractmethod
    def criar_lancamento(lancamento: Type[Lancamentos]) -> Lancamentos:
        pass

    @abstractmethod
    def atualizar_lancamento(lancamento: Type[Lancamentos]) -> bool:
        pass

    @abstractmethod
    def excluir_lancamento(lancamento: Type[Lancamentos]) -> bool:
        pass

    @abstractmethod
    def obter_lancamento_por_id(id_lancamento: Type[UUID]) -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_por_plano_de_contas(
        id_plano_de_contas: Type[UUID],
    ) -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_por_conta(id_conta: Type[UUID]) -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_por_cartao_de_credito(
        id_cartao_de_credito: Type[UUID],
    ) -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_por_centro_de_custo(
        id_centro_de_custo: Type[UUID],
    ) -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_vencidos_em_aberto() -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_vencidos_efetivados() -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_a_vencer_em_aberto() -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_a_vencer_efetivados() -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_orcados() -> List[Lancamentos]:
        pass

    @abstractmethod
    def obter_lancamentos_efetivados() -> List[Lancamentos]:
        pass
