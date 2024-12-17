#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   obter_moeda_por_id_controller.py
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

from src.errors.errors_handler import handler_errors

from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.http_types.http_response import HttpResponse

from src.adapters.http.presenters.presenter_error import presenter_error
from src.adapters.http.presenters.moedas_presenters import moedas_presenter_one

from typing import Type


class ObterMoedaPorIdController(ControllerInterface):
    def __init__(self, use_case: Type[ObterMoedaPorId]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        id_moeda = MoedaDTOIn().from_dict(http_request.query_params[0])

        try:
            response = self.__use_case.execute(id_moeda)
            return moedas_presenter_one(response)
        except Exception as exception:
            result = handler_errors(exception)
            return presenter_error(result)
