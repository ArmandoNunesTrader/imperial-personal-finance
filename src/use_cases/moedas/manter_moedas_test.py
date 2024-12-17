#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   manter_moedas_test.py
@Created :   11/12/2024 18:38:54
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes do caso de uso Manter Moedas
    ============================================================================
"""

import pytest
import dataclasses

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.dtos.dto_moedas import MoedaDTOIn
from src.use_cases.moedas.serializers_moeda import entity_to_dto_in
from src.errors.moedas_errors import (
    MoedaNaoInformada,
    MoedaIdNaoLocalizado,
    MoedaSiglaJaCadastrada,
    MoedaErrosDeValidacao,
)
from src.use_cases.moedas.manter_moedas import (
    CriarMoeda,
    AtualizarMoeda,
    ExcluirMoeda,
)
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId

obj_repo = MoedasRepositorio()
for reg in obj_repo.repo:
    id_moeda_1 = reg.id_moeda
    obj_moeda_1 = reg
    break


def test_moedas_use_cases_criar():
    # Criação da Moeda com Erros na validação ----------------------------------
    dict_1 = {
        "sigla": "S",
        "descricao": "M",
        "_tipo_de_moeda": "XXX",
        "_valor_da_paridade": 98765431.54,
    }
    obj_moeda_dto_in = MoedaDTOIn().from_dict(dict_1)
    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        CriarMoeda(obj_repo).execute(obj_moeda_dto_in)
    assert msg_error.value.status_code == 422
    assert msg_error.value.message["sigla"] == ["min length is 3"]
    assert msg_error.value.message["descricao"] == ["min length is 3"]
    assert msg_error.value.message["_tipo_de_moeda"] == ["unallowed value Xxx"]
    assert msg_error.value.message["_valor_da_paridade"] == ["max value is 1000.0"]

    # Criação da Moeda com Sigla já existente ----------------------------------
    dict_1 = {
        "sigla": "Primeira Moeda",
        "descricao": "Moeda já criada no Mock",
        "_tipo_de_moeda": "Dólar Americano",
        "_valor_da_paridade": 9.54,
    }
    obj_moeda_dto_in = MoedaDTOIn().from_dict(dict_1)
    with pytest.raises(MoedaSiglaJaCadastrada) as msg_error:
        CriarMoeda(obj_repo).execute(obj_moeda_dto_in)
    assert msg_error.value.message == "Sigla da Moeda já cadastrada!"

    # Criação da Moeda ---------------------------------------------------------
    dict_1 = {
        "sigla": "Moeda de Teste",
        "descricao": "Moeda de Testes",
        "_tipo_de_moeda": "Euro",
        "_valor_da_paridade": 6.54,
    }
    obj_moeda_dto_in = MoedaDTOIn().from_dict(dict_1)
    obj_moeda_1 = CriarMoeda(obj_repo).execute(obj_moeda_dto_in)
    assert obj_moeda_1 is not None


def test_moedas_use_cases_atualizar():
    # Tenta obter Moeda inexistente --------------------------------------------
    id_moeda_check = MoedaDTOIn().from_dict(
        {
            "id_moeda": "38b6f4c7-0ff8-4f05-a751-f7aba95763b7",
            "sigla": "Correta",
            "descricao": "Correta",
            "_tipo_de_moeda": "Real Brasileiro",
            "_valor_da_paridade": 1.23,
        }
    )
    with pytest.raises(MoedaIdNaoLocalizado) as msg_error:
        AtualizarMoeda(obj_repo).execute(id_moeda_check)
    assert msg_error.value.message == "Identificador da Moeda não localizado!"

    # Obtém a Moeda por Id para confirmar a gravação ---------------------------
    id_moeda_check = MoedaDTOIn().from_dict({"id_moeda": id_moeda_1})
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_moeda_1 == obj_check

    # Teste do caso de uso Atualizar Moeda com Sigla duplicada -----------------
    obj_new = dataclasses.replace(obj_check)
    obj_new.id_moeda = obj_check.id_moeda
    obj_new.sigla = "Segunda Moeda"
    obj_new.descricao = "Descrição Ajustada"
    dict_in = entity_to_dto_in(obj_new)
    with pytest.raises(MoedaSiglaJaCadastrada) as msg_error:
        AtualizarMoeda(obj_repo).execute(dict_in)
    assert msg_error.value.message == "Sigla da Moeda já cadastrada!"

    # Teste do caso de uso Atualizar Moeda com erros de validação --------------
    obj_new.sigla = "Seg Moeda"
    obj_new.descricao = "De"
    dict_in = entity_to_dto_in(obj_new)

    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        AtualizarMoeda(obj_repo).execute(dict_in)
    assert msg_error.value.status_code == 422
    assert msg_error.value.message["descricao"] == ["min length is 3"]

    # Teste do caso de uso Atualizar Moeda -------------------------------------
    id_moeda_check = MoedaDTOIn().from_dict({"id_moeda": id_moeda_1})
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    obj_check.sigla = "Sigla Alterada"
    obj_check.descricao = "Descrição Alterada New"
    dict_in = entity_to_dto_in(obj_check)

    result = AtualizarMoeda(obj_repo).execute(dict_in)

    assert result is True

    obj_check_pos = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_check_pos.sigla == obj_check.sigla
    assert obj_check_pos.descricao == obj_check.descricao


def test_moedas_use_cases_excluir():
    # Tenta obter Moeda inexistente --------------------------------------------
    id_moeda_check = MoedaDTOIn().from_dict(
        {
            "id_moeda": "38b6f4c7-0ff8-4f05-a751-f7aba95763b7",
            "sigla": "Correta",
            "descricao": "Correta",
            "_tipo_de_moeda": "Real Brasileiro",
            "_valor_da_paridade": 1.23,
        }
    )
    with pytest.raises(MoedaIdNaoLocalizado) as msg_error:
        ExcluirMoeda(obj_repo).execute(id_moeda_check)
    assert msg_error.value.message == "Identificador da Moeda não localizado!"

    # Tenta obter Moeda com erros de validação ---------------------------------
    id_moeda_check = MoedaDTOIn().from_dict(
        {
            "id_moeda": "38b6f4c7-0ff8-Xz05-a751-f7aba95763b7",
            "sigla": "Correta",
            "descricao": "Correta",
            "_tipo_de_moeda": "Real Brasileiro",
            "_valor_da_paridade": 1.23,
        }
    )
    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        ExcluirMoeda(obj_repo).execute(id_moeda_check)
    assert msg_error.value.message["id_moeda"][0] == "must be valid UUID"

    # Teste do caso de uso Excluir Moeda ---------------------------------------
    dict_excluir = MoedaDTOIn().from_dict({"id_moeda": str(id_moeda_1)})
    result = ExcluirMoeda(obj_repo).execute(dict_excluir)
    assert result is True

    with pytest.raises(MoedaIdNaoLocalizado) as msg_error:
        ObterMoedaPorId(obj_repo).execute(dict_excluir)
    assert msg_error.value.message == "Identificador da Moeda não localizado!"


def test_moedas_use_cases_excessoes():
    # Excessões ----------------------------------------------------------------
    with pytest.raises(MoedaNaoInformada) as msg_error:
        CriarMoeda(obj_repo).execute(None)
    assert msg_error.value.message == "Moeda não informada!"

    with pytest.raises(MoedaNaoInformada) as msg_error:
        AtualizarMoeda(obj_repo).execute(None)
    assert msg_error.value.message == "Moeda não informada!"

    with pytest.raises(MoedaNaoInformada) as msg_error:
        ExcluirMoeda(obj_repo).execute(None)
    assert msg_error.value.message == "Moeda não informada!"
