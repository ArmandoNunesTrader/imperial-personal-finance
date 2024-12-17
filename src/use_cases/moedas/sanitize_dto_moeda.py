#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   sanitize_dto_moeda.py
@Created :   16/12/2024 09:20:28
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Sanitiza e valida um DTO de Moeda
    ============================================================================
"""

from typing import Type
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

from src.use_cases.dtos.dto_moedas import MoedaDTOIn

from src.utils.sanitize_utils import (
    sanitize_uuid,
    sanitize_pt_br_phrase_capitalize,
)


def sanitize_dto_moeda(dto_in: Type[MoedaDTOIn]) -> Type[MoedaDTOIn]:
    dto_sanitized = {}
    dto_in_dict = dto_in.to_dict()
    if "id_moeda" in dto_in_dict and not is_null_or_empty(dto_in_dict["id_moeda"]):
        dto_sanitized.update({"id_moeda": sanitize_uuid(dto_in.id_moeda)})

    if "sigla" in dto_in_dict and not is_null_or_empty(dto_in_dict["sigla"]):
        dto_sanitized.update({"sigla": sanitize_pt_br_phrase_capitalize(dto_in.sigla)})

    if "descricao" in dto_in_dict and not is_null_or_empty(dto_in_dict["descricao"]):
        dto_sanitized.update(
            {"descricao": sanitize_pt_br_phrase_capitalize(dto_in.descricao)}
        )

    if "_tipo_de_moeda" in dto_in_dict and not is_null_or_empty(
        dto_in_dict["_tipo_de_moeda"]
    ):
        dto_sanitized.update(
            {"_tipo_de_moeda": sanitize_pt_br_phrase_capitalize(dto_in._tipo_de_moeda)}
        )
    if "_valor_da_paridade" in dto_in_dict and not is_null_or_empty(
        dto_in_dict["_valor_da_paridade"]
    ):
        dto_sanitized.update({"_valor_da_paridade": dto_in._valor_da_paridade})

    return MoedaDTOIn().from_dict(dto_sanitized)
