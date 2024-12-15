#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_errors.py
@Created :   11/12/2024 12:46:56
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classes de erro referentes à entidade Moedas
    ============================================================================
"""


class MoedaBadRequest(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Bad Request"
        self.status_code = 400


class MoedaNaoInformada(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Moeda não informada!")


class MoedaIdNaoInformado(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Identificador da Moeda informado não é válido!")


class MoedaSiglaNaoInformada(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Sigla da Moeda informada incorretamente!")


class MoedaSiglaJaCadastrada(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Sigla da Moeda já cadastrada!")


class MoedaDadosInvalidos(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Informe todos os dados corretamente!")


class MoedaErrosDeValidacao(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unprocessable Entity"
        self.status_code = 422


class MoedasException(Exception):  # pragma: no cover
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Internal Server Error"
        self.status_code = status_code
