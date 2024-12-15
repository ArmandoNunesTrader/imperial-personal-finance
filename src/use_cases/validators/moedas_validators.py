#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   moedas_validators.py
@Created :   11/12/2024 16:38:15
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Validadores dos casos de uso da entidade Moedas
    ============================================================================
"""

# from cerberus import Validator
from typing import Type
from cerberus import Validator

import re

from src.domain.entities.moedas import Moedas
from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.errors.moedas_errors import MoedaErrosDeValidacao


def validate_uuid(field, value, error):
    re_uuid = re.compile(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", re.I)
    if not re_uuid.match(value):
        error(field, "must be valid UUID")


def moedas_dto_in_validator(
    dto_in: Type[MoedaDTOIn] = None, moeda_in: Type[Moedas] = None
):

    tipos_de_moedas_list = TiposDeMoedas.all_names()
    dict_schema = {
        "sigla": {
            "type": "string",
            "required": True,
            "empty": False,
            "minlength": 3,
            "maxlength": 15,
        },
        "descricao": {
            "type": "string",
            "required": True,
            "empty": False,
            "minlength": 3,
            "maxlength": 30,
        },
        "tipo_de_moeda": {
            "type": "string",
            "required": True,
            "empty": False,
            "minlength": 3,
            "maxlength": 3,
            "allowed": tipos_de_moedas_list,
        },
        "valor_da_paridade": {
            "type": "float",
            "required": True,
            "empty": False,
            "min": 0.001,
            "max": 1000.000,
        },
    }

    if ((dto_in is not None) and ("id_moeda" in dto_in.to_dict())) or (
        (moeda_in is not None)
    ):
        dict_schema.update({"id_moeda": {"check_with": validate_uuid}})
    validator_schema = Validator(dict_schema)

    if dto_in is not None:
        response = validator_schema.validate(dto_in.to_dict())
    elif moeda_in is not None:
        response = validator_schema.validate(
            {
                "id_moeda": str(moeda_in.id_moeda),
                "sigla": moeda_in.sigla,
                "descricao": moeda_in.descricao,
                "tipo_de_moeda": moeda_in.tipo_de_moeda,
                "valor_da_paridade": moeda_in.valor_da_paridade,
            }
        )

    if response is False:
        raise MoedaErrosDeValidacao(validator_schema.errors)
