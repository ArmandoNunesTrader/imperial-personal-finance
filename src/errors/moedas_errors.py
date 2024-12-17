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


class MoedasException(Exception):  # pragma: no cover
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Internal Server Error"
        self.status_code = status_code


# ------------------------------------------------------------------------------
#   Referentes ao tratamento geral da entidade
# ------------------------------------------------------------------------------
class MoedaNotFound(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = "Não existem Moedas cadastradas!"
        self.name = "Not Found"
        self.status_code = 404


class MoedaBadRequest(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Bad Request"
        self.status_code = 400


class MoedaErrosDeValidacao(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unprocessable Entity"
        self.status_code = 422


# class MoedaDadosInvalidos(MoedaBadRequest):
#     def __init__(self) -> None:
#         super().__init__("Informe todos os dados corretamente!")


class MoedaNaoInformada(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Moeda não informada!")


# ------------------------------------------------------------------------------
#   Referentes ao id que é identificador primário
# ------------------------------------------------------------------------------
class MoedaIdNaoInformado(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Identificador da Moeda não informado!")


class MoedaIdNaoLocalizado(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = "Identificador da Moeda não localizado!"
        self.name = "Not Found"
        self.status_code = 404


# ------------------------------------------------------------------------------
#   Referentes à sigla que é atributo único
# ------------------------------------------------------------------------------
class MoedaSiglaNaoInformada(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Sigla da Moeda não informada!")


class MoedaSiglaJaCadastrada(MoedaBadRequest):
    def __init__(self) -> None:
        super().__init__("Sigla da Moeda já cadastrada!")


class MoedaSiglaNaoLocalizada(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = "Sigla da Moeda não localizada!"
        self.name = "Not Found"
        self.status_code = 404
