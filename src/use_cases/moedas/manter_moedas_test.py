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

from src.use_cases.mocks.moedas_mock import MoedasRepositorio
from src.use_cases.dto_s.dto_moedas import MoedaDTOIn
from src.errors.moedas_errors import (
    MoedaNaoInformada,
    MoedaSiglaJaCadastrada,
    MoedaErrosDeValidacao,
)
from src.use_cases.moedas.manter_moedas import CriarMoeda, AtualizarMoeda, ExcluirMoeda
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId
from src.use_cases.moedas.obter_moeda_por_sigla import ObterMoedaPorSigla

obj_repo = MoedasRepositorio()
for ind, reg in obj_repo.repo[0].items():
    id_moeda = reg.id_moeda
    obj_moeda_1 = reg
    break


def test_moedas_use_cases():
    # Criação da Moeda com Erros na validação ----------------------------------
    dict_1 = {
        "sigla": "S",
        "descricao": "M",
        "tipo_de_moeda": "XXX",
        "valor_da_paridade": 98765431.54,
    }
    obj_moeda_dto_in = MoedaDTOIn().from_dict(dict_1)
    with pytest.raises(MoedaErrosDeValidacao) as msg_error:
        CriarMoeda(obj_repo).execute(obj_moeda_dto_in)
    assert msg_error.value.status_code == 422
    assert msg_error.value.message["sigla"] == ["min length is 3"]
    assert msg_error.value.message["descricao"] == ["min length is 3"]
    assert msg_error.value.message["tipo_de_moeda"] == ["unallowed value XXX"]
    assert msg_error.value.message["valor_da_paridade"] == ["max value is 1000.0"]

    # Criação da Moeda com Sigla já existente ----------------------------------
    dict_1 = {
        "sigla": "Primeira Moeda",
        "descricao": "Moeja já criada no Mock",
        "tipo_de_moeda": "USD",
        "valor_da_paridade": 9.54,
    }
    obj_moeda_dto_in = MoedaDTOIn().from_dict(dict_1)
    with pytest.raises(MoedaSiglaJaCadastrada) as msg_error:
        CriarMoeda(obj_repo).execute(obj_moeda_dto_in)
    assert msg_error.value.status_code == 400
    assert msg_error.value.message == "Sigla da Moeda já cadastrada!"

    # Criação da Moeda ---------------------------------------------------------
    dict_1 = {
        "sigla": "Moeda de Teste",
        "descricao": "Moeda de Testes",
        "tipo_de_moeda": "EUR",
        "valor_da_paridade": 6.54,
    }
    obj_moeda_dto_in = MoedaDTOIn().from_dict(dict_1)
    obj_moeda_1 = CriarMoeda(obj_repo).execute(obj_moeda_dto_in)
    assert obj_moeda_1 is not None

    # Obtém a Moeda por Sigla para confirmar a gravação ------------------------
    id_moeda_check = obj_moeda_1.id_moeda
    sigla_check = "Moeda de Teste"
    obj_check = ObterMoedaPorSigla(obj_repo).execute(sigla_check)
    assert obj_moeda_1 == obj_check

    # Teste do caso de uso Atualizar Moeda com Sigla duplicada -----------------
    obj_check.sigla = "Segunda Moeda"
    obj_check.descricao = "Descrição Alterada"
    with pytest.raises(MoedaSiglaJaCadastrada) as msg_error:
        AtualizarMoeda(obj_repo).execute(obj_check)
    assert msg_error.value.message == "Sigla da Moeda já cadastrada!"

    # Teste do caso de uso Atualizar Moeda -------------------------------------
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    obj_check.sigla = "Sigla New"
    obj_check.descricao = "Descrição Alterada New"

    result = AtualizarMoeda(obj_repo).execute(obj_check)

    assert result is True

    obj_check_pos = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_check_pos.sigla == obj_check.sigla
    assert obj_check_pos.descricao == obj_check.descricao

    # Teste do caso de uso Excluir Moeda ---------------------------------------
    id_moeda_check = obj_moeda_1.id_moeda
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    result = ExcluirMoeda(obj_repo).execute(obj_check)
    assert result is True

    obj_check_pos = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_check_pos is None

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
