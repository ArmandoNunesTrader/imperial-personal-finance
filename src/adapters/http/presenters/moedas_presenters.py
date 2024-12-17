#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __init__.py
@Created :   13/12/2024 10:32:10
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Presenter dos Controllers da Entidade Moedas
    ============================================================================
"""

from typing import Dict

from src.domain.entities.moedas import Moedas
from src.adapters.http.http_types.http_response import HttpResponse

from src.use_cases.moedas.serializers_moeda import entity_to_dto_out


def moedas_presenter_one(response: any, status_code_in: int = 200) -> HttpResponse:
    if isinstance(response, Moedas):
        obj_serialized = entity_to_dto_out(response)
        return HttpResponse(
            status_code=status_code_in,
            body={
                "type": "Moedas",
                "count": 1,
                "message": None,
                "attributes": obj_serialized,
            },
        )

    if isinstance(response, Dict):
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


# def moedas_presenter_ok(response: str, status_code_in: int = 200) -> HttpResponse:
#     return HttpResponse(
#         status_code=status_code_in,
#         body={
#             "type": "Moedas",
#             "count": 0,
#             "message": response,
#             "attributes": None,
#         },
#     )
