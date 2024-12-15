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

from src.errors.moedas_errors import MoedaDadosInvalidos
from src.domain.entities.moedas import Moedas
from src.use_cases.moedas.manter_moedas import AtualizarMoeda
from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.interfaces.controller_interface import ControllerInterface
from src.adapters.http.http_types.http_response import HttpResponse
from src.adapters.http.presenters.moedas_presenters import moedas_presenter_ok

from typing import Type
from uuid import UUID


class AtualizarMoedaController(ControllerInterface):
    def __init__(self, use_case: Type[AtualizarMoeda]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: type[HttpRequest]) -> HttpResponse:
        if (
            (http_request.query_params is None)
            or ("id_moeda" not in http_request.query_params)
            or ("sigla" not in http_request.query_params)
            or ("descricao" not in http_request.query_params)
            or ("tipo_de_moeda" not in http_request.query_params)
            or ("valor_da_paridade" not in http_request.query_params)
        ):
            raise MoedaDadosInvalidos()

        obj_moeda = Moedas(
            http_request.query_params["sigla"],
            http_request.query_params["descricao"],
            http_request.query_params["tipo_de_moeda"],
            http_request.query_params["valor_da_paridade"],
        )
        obj_moeda.id_moeda = UUID(http_request.query_params["id_moeda"])
        _ = self.__use_case.execute(obj_moeda)

        return moedas_presenter_ok("Moeda atualizada com sucesso!", 200)
