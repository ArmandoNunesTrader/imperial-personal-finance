#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   cartoes_de_credito_repositorio_interface.py
@Created :   10/12/2024 12:41:55
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface de repositório de Cartões de Crédito
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type, List
from uuid import UUID

from src.domain.entities.cartoes_de_credito import CartoesDeCredito


class CartoesDeCreditoRepositorioInterface(ABC):
    @abstractmethod
    def criar_cartao_de_credito(
        cartao_de_credito: Type[CartoesDeCredito],
    ) -> CartoesDeCredito:
        pass

    @abstractmethod
    def atualizar_cartao_de_credito(cartao_de_credito: Type[CartoesDeCredito]) -> bool:
        pass

    @abstractmethod
    def excluir_cartao_de_credito(cartao_de_credito: Type[CartoesDeCredito]) -> bool:
        pass

    @abstractmethod
    def obter_cartao_de_credito_por_id(
        id_cartao_de_credito: Type[UUID],
    ) -> List[CartoesDeCredito]:
        pass

    @abstractmethod
    def obter_cartao_de_credito_por_nome(nome: str) -> List[CartoesDeCredito]:
        pass

    @abstractmethod
    def obter_cartao_de_credito_por_numero(numero: str) -> List[CartoesDeCredito]:
        pass
