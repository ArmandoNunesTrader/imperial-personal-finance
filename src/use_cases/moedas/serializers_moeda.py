#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   serializers_moeda.py
@Created :   16/12/2024 17:47:17
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Serializadores da entidade Moeda
    ============================================================================
"""

from typing import Type, Dict

from src.domain.entities.moedas import Moedas
from src.use_cases.dtos.dto_moedas import MoedaDTOIn

import src.utils.datetime_utils as dtu


def entity_to_dto_in(moeda: Type[Moedas]) -> Type[MoedaDTOIn]:
    dict_in = MoedaDTOIn().from_dict(
        {
            "id_moeda": str(moeda.id_moeda),
            "sigla": moeda.sigla,
            "descricao": moeda.descricao,
            "_tipo_de_moeda": moeda._tipo_de_moeda,
            "_valor_da_paridade": moeda._valor_da_paridade,
        }
    )
    return dict_in


def entity_to_dto_out(moeda: Type[Moedas]) -> Dict:
    return {
        "id_moeda": str(moeda.id_moeda),
        "sigla": moeda.sigla,
        "descricao": moeda.descricao,
        "paridade": {
            "sigla": moeda.paridade_com_real_brasileiro.tipo_de_moeda.name,
            "descricao": moeda._tipo_de_moeda,
            "valor": moeda._valor_da_paridade,
            "formatada": moeda.paridade_com_real_brasileiro.formatada,
        },
        "created_at": dtu.datetime_dd_mm_yyyy_hh_mm_ss(moeda.created_at),
        "updated_at": dtu.datetime_dd_mm_yyyy_hh_mm_ss(moeda.updated_at),
    }


def dto_in_to_entity(dto_in: Type[MoedaDTOIn], with_id: bool = True) -> Type[Moedas]:
    dict_dto = dto_in.to_dict()
    obj_moeda = Moedas(
        dict_dto["sigla"],
        dict_dto["descricao"],
        dict_dto["_tipo_de_moeda"],
        dict_dto["_valor_da_paridade"],
    )
    if with_id is True:
        obj_moeda.id_moeda = dict_dto["id_moeda"]

    return obj_moeda
