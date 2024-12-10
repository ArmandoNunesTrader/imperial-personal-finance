#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   centros_de_custo_repositorio_interface.py
@Created :   10/12/2024 12:31:20
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface de repositório de Centros de Custo
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type, List
from uuid import UUID

from src.domain.entities.centros_de_custo import CentrosDeCusto


class CentrosDeCustoRepositorioInterface(ABC):
    @abstractmethod
    def criar_centro_de_custo(
        centro_de_custo: Type[CentrosDeCusto],
    ) -> CentrosDeCusto:
        pass

    @abstractmethod
    def atualizar_centro_de_custo(centro_de_custo: Type[CentrosDeCusto]) -> bool:
        pass

    @abstractmethod
    def excluir_centro_de_custo(centro_de_custo: Type[CentrosDeCusto]) -> bool:
        pass

    @abstractmethod
    def obter_centro_de_custo_por_id(
        id_centro_de_custo: Type[UUID],
    ) -> List[CentrosDeCusto]:
        pass

    @abstractmethod
    def obter_centro_de_custo_por_sigla(sigla: str) -> List[CentrosDeCusto]:
        pass
