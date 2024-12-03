#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   database_connector.py
@Created :   02/12/2024 22:26:34
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Conector padrão para os bancos de dados
    ============================================================================
"""

from dotenv import load_dotenv
from abc import ABC, abstractmethod


class DatabaseConnector(ABC):
    # --------------------------------------------------------------------------
    # Hook que verifica se todos os métodos foram obrigatoriamente
    #   implementados nas classes filhas e com os mesmos parâmetros
    # --------------------------------------------------------------------------
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is DatabaseConnector:
            subclass_dict = subclass.__mro__[0].__dict__
            cls_dict = cls.__mro__[0].__dict__
            cls_abstract_methods = cls.__abstractmethods__

            for method_name, method in cls_dict.items():
                # If the method is an abstracmethod
                if method_name in cls_abstract_methods and hasattr(
                    method, "__annotations__"
                ):
                    if (
                        method_name not in subclass_dict
                        or subclass_dict[method_name].__annotations__
                        != cls_dict[method_name].__annotations__
                    ):
                        return False
            return True

    # --------------------------------------------------------------------------
    # Construtor
    # --------------------------------------------------------------------------
    def __init__(self):
        load_dotenv()

    # --------------------------------------------------------------------------
    # Métodos da interface que terão de ser implementados na herança
    # --------------------------------------------------------------------------
    @abstractmethod
    def get_db_name(self) -> str:
        pass

    @abstractmethod
    def create_db(self) -> bool:
        pass

    @abstractmethod
    def create_functions(self) -> bool:
        pass

    @abstractmethod
    def create_dir_and_db(self, verify: bool = False) -> None:
        pass

    @abstractmethod
    def connect_db(self) -> any:
        pass

    @abstractmethod
    def desconnect_db(self) -> None:
        pass
