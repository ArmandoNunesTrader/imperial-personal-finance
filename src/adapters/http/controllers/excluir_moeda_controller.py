#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   excluir_moeda_controller.py
@Created :   12/12/2024 19:59:01
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Controller do caso de uso Excluir Moeda
    ============================================================================
"""

from src.use_cases.moedas.manter_moedas import ExcluirMoeda
from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_response import HttpResponse

from typing import Type


class ExcluirMoedaController(ControllerInterface):
    def __init__(self, use_case: Type[ExcluirMoeda]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: type[HttpRequest]) -> HttpResponse:
        dto_in = MoedaDTOIn.from_dict(
            {
                http_request.query_params["sigla"],
                http_request.query_params["descricao"],
                http_request.query_params["tipo_de_moeda"],
                http_request.query_params["valor_da_paridade"],
            }
        )
        response = self.__use_case.execute(dto_in)

        return self.__presenter(response)

    def __presenter(self, response: any) -> HttpResponse:
        if isinstance(response, bool):
            return HttpResponse(
                status_code=200,
                body={
                    "type": "Moedas",
                    "count": 1,
                    "message": "Moeda excluída com sucesso!",
                    "attributes": None,
                },
            )

        if isinstance(response, str):
            return HttpResponse(
                status_code=response["status_code"],
                body={
                    "type": "Moedas",
                    "count": 0,
                    "message": response["body"],
                    "attributes": None,
                },
            )

        return HttpResponse(
            status_code=500,
            body={
                "type": "Moedas",
                "count": 0,
                "message": "Ocorreu um erro desconhecido no servidor!",
                "attributes": None,
            },
        )
