#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_todas_moedas_controller.py
@Created :   17/12/2024 14:40:31
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Controller do caso de uso Obter Todas as Moedas
    ============================================================================
"""

from src.errors.errors_handler import handler_errors

from src.use_cases.moedas.obter_todas_moedas_test import ObterTodasAsMoedas
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.http_types.http_response import HttpResponse

from src.adapters.http.presenters.presenter_error import presenter_error
from src.adapters.http.presenters.moedas_presenters import moedas_presenter_all

from typing import Type


class ObterTodasAsMoedasController(ControllerInterface):
    def __init__(self, use_case: Type[ObterTodasAsMoedas]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        try:
            response = self.__use_case.execute()
            return moedas_presenter_all(response)
        except Exception as exception:
            result = handler_errors(exception)
            return presenter_error(result)
