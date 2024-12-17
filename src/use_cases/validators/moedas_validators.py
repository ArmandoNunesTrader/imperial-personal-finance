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

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.errors.moedas_errors import MoedaErrosDeValidacao


def validate_uuid(field, value, error):
    re_uuid = re.compile(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", re.I)
    if (value is None) or (not isinstance(value, str)) or (not re_uuid.match(value)):
        error(field, "must be valid UUID")


def moedas_dto_in_validator_full(dto_in: Type[MoedaDTOIn] = None) -> bool:
    tipos_de_moedas_list = TiposDeMoedas.all_values()
    dict_schema = {
        "id_moeda": {"check_with": validate_uuid},
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
        "_tipo_de_moeda": {
            "type": "string",
            "required": True,
            "empty": False,
            "minlength": 3,
            "maxlength": 30,
            "allowed": tipos_de_moedas_list,
        },
        "_valor_da_paridade": {
            "type": "float",
            "required": True,
            "empty": False,
            "min": 0.001,
            "max": 1000.000,
        },
    }

    validator_schema = Validator(dict_schema)

    response = validator_schema.validate(dto_in.to_dict())

    if response is False:
        raise MoedaErrosDeValidacao(validator_schema.errors)

    return True


def moedas_dto_in_validator_id(dto_in: Type[MoedaDTOIn] = None) -> bool:
    dict_schema = {
        "id_moeda": {"check_with": validate_uuid},
    }

    validator_schema = Validator(dict_schema)

    response = validator_schema.validate({"id_moeda": dto_in.to_dict()["id_moeda"]})

    if response is False:
        raise MoedaErrosDeValidacao(validator_schema.errors)

    return True


def moedas_dto_in_validator_sigla(dto_in: Type[MoedaDTOIn] = None) -> bool:
    dict_schema = {
        "sigla": {
            "type": "string",
            "required": True,
            "empty": False,
            "minlength": 3,
            "maxlength": 15,
        },
    }

    validator_schema = Validator(dict_schema)

    response = validator_schema.validate({"sigla": dto_in.to_dict()["sigla"]})
    if response is False:
        raise MoedaErrosDeValidacao(validator_schema.errors)

    return True
