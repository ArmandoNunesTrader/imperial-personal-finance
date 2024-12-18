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

from src.errors.errors_handler import handler_errors

from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.moedas.manter_moedas import ExcluirMoeda
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.http_types.http_response import HttpResponse

from src.adapters.http.presenters.presenter_error import presenter_error


from typing import Type


class ExcluirMoedaController(ControllerInterface):
    def __init__(self, use_case: Type[ExcluirMoeda]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: type[HttpRequest]) -> HttpResponse:
        id_moeda = MoedaDTOIn().from_dict(http_request.query_params[0])

        try:
            self.__use_case.execute(id_moeda)
        except Exception as exception:
            result = handler_errors(exception)
            return presenter_error(result)
