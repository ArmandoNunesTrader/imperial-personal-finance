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

from cerberus import Validator
from typing import Type

from src.domain.enums.tipos_de_moedas import TiposDeMoedas
from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.errors.moedas_errors import MoedaErrosDeValidacao


def moedas_dto_in_validator(dto_in: Type[MoedaDTOIn]):
    tipos_de_moedas_list = TiposDeMoedas.all_names()
    validator_schema = Validator(
        {
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
    )

    response = validator_schema.validate(dto_in.to_dict())
    if response is False:
        raise MoedaErrosDeValidacao(validator_schema.errors)
