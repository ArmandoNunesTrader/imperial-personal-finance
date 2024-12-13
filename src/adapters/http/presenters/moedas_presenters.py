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

from src.domain.entities.moedas import Moedas
from src.adapters.http.http_types.http_response import HttpResponse

from typing import Dict


def moedas_presenter_one(response: any) -> HttpResponse:
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
                        "sigla": response.paridade_com_real_brasileiro.tipo_de_moeda.name,  # noqa E501
                        "valor": response.paridade_com_real_brasileiro.valor,
                        "formatada": response.paridade_com_real_brasileiro.formatada,  # noqa E501
                    },
                },
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
