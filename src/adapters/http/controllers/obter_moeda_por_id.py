#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_id.py
@Created :   12/12/2024 20:06:16
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Controller do caso de uso Obter Moeda por Id
    ============================================================================
"""

from src.domain.entities.moedas import Moedas
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_response import HttpResponse

from typing import Type
from uuid import UUID


class CriarMoedaController(ControllerInterface):
    def __init__(self, use_case: Type[ObterMoedaPorId]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: type[HttpRequest]) -> HttpResponse:
        id_moeda = UUID(http_request.query_params["id_moeda"])

        try:
            response = self.__use_case.execute(id_moeda)
            return self.__presenter(response)
        except Exception as exception:
            return self.__presenter_error(exception)

    def __presenter_error(self, response: any) -> HttpResponse:
        return HttpResponse(
            status_code=response["code"],
            body={
                "type": "Moedas",
                "count": 0,
                "message": response["message"],
                "attributes": response["name"],
            },
        )

    def __presenter(self, response: any) -> HttpResponse:
        if isinstance(response, Moedas):
            return HttpResponse(
                status_code=200,
                body={
                    "type": "Moedas",
                    "count": 1,
                    "message": None,
                    "attributes": {
                        "sigla": response.sigla,
                        "descricao": response.descricao,
                        "paridade": {
                            "sigla": response.paridade_com_real_brasileiro.tipo_de_response,  # noqa E501
                            "valor": response.paridade_com_real_brasileiro.valor,
                            "formatada": response.paridade_com_real_brasileiro.formatada,  # noqa E501
                        },
                    },
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
