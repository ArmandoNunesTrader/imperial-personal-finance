#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   atualizar_moeda_controller.py
@Created :   12/12/2024 19:59:01
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Controller do caso de uso Atualizar Moeda
    ============================================================================
"""

from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.use_cases.moedas.manter_moedas import AtualizarMoeda
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_response import HttpResponse
from src.adapters.http.presenters.moedas_presenters import moedas_presenter_one

from typing import Type


class AtualizarMoedaController(ControllerInterface):
    def __init__(self, use_case: Type[AtualizarMoeda]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: type[HttpRequest]) -> HttpResponse:
        dict_http = {
            http_request.query_params["id_moeda"],
            http_request.query_params["sigla"],
            http_request.query_params["descricao"],
            http_request.query_params["tipo_de_moeda"],
            http_request.query_params["valor_da_paridade"],
        }

        dto_in = MoedaDTOIn().from_dict(dict_http)
        response = self.__use_case.execute(dto_in)

        return moedas_presenter_one(response)
