#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   criar_moeda_controller.py
@Created :   12/12/2024 18:52:06
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Controller do caso de uso Criar Moeda
    ============================================================================
"""

from src.errors.moedas_errors import MoedaDadosInvalidos
from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.moedas.manter_moedas import CriarMoeda
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_response import HttpResponse
from src.adapters.http.presenters.moedas_presenters import moedas_presenter_one

from typing import Type


class CriarMoedaController(ControllerInterface):
    def __init__(self, use_case: Type[CriarMoeda]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: type[HttpRequest]) -> HttpResponse:
        if (
            (http_request.query_params is None)
            or ("sigla" not in http_request.query_params)
            or ("descricao" not in http_request.query_params)
            or ("tipo_de_moeda" not in http_request.query_params)
            or ("valor_da_paridade" not in http_request.query_params)
        ):
            raise MoedaDadosInvalidos()

        dict_http = {
            "sigla": http_request.query_params["sigla"],
            "descricao": http_request.query_params["descricao"],
            "tipo_de_moeda": http_request.query_params["tipo_de_moeda"],
            "valor_da_paridade": http_request.query_params["valor_da_paridade"],
        }

        dto_in = MoedaDTOIn().from_dict(dict_http)
        response = self.__use_case.execute(dto_in)

        return moedas_presenter_one(response, 201)
