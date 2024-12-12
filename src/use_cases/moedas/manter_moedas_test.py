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
from src.errors.moedas_errors import MoedaNaoInformada
from src.use_cases.moedas.manter_moedas import CriarMoeda, AtualizarMoeda, ExcluirMoeda
from src.use_cases.moedas.obter_moeda_por_id import ObterMoedaPorId

obj_repo = MoedasRepositorio()
for ind, reg in obj_repo.repo[0].items():
    id_moeda = reg.id_moeda
    obj_moeda_1 = reg
    break


def test_criar_moeda():
    obj_moeda_dto_in = MoedaDTOIn.from_dict(
        {
            "sigla": "Moeda 1",
            "descricao": "Moeda de Testes",
            "tipo_de_moeda": "EUR",
            "valor_da_paridade": 6.54,
        }
    )

    obj_moeda = CriarMoeda(obj_repo).execute(obj_moeda_dto_in)

    assert obj_moeda is not None

    id_moeda_check = obj_moeda.id_moeda
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_moeda == obj_check

    # Teste do caso de uso Atualizar Moeda
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    obj_check.sigla = "Sigla Alterada"
    obj_check.descricao = "Descrição Alterada"

    result = AtualizarMoeda(obj_repo).execute(obj_check)

    assert result is True

    obj_check_pos = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_check_pos.sigla == obj_check.sigla
    assert obj_check_pos.descricao == obj_check.descricao

    # Teste do caso de uso Excluir Moeda
    obj_check = ObterMoedaPorId(obj_repo).execute(id_moeda_check)

    result = ExcluirMoeda(obj_repo).execute(obj_check)

    assert result is True

    obj_check_pos = ObterMoedaPorId(obj_repo).execute(id_moeda_check)
    assert obj_check_pos is None

    with pytest.raises(MoedaNaoInformada) as msg_error:
        CriarMoeda(obj_repo).execute(None)
    assert msg_error.value.message == "Moeda não informada!"

    with pytest.raises(MoedaNaoInformada) as msg_error:
        AtualizarMoeda(obj_repo).execute(None)
    assert msg_error.value.message == "Moeda não informada!"

    with pytest.raises(MoedaNaoInformada) as msg_error:
        ExcluirMoeda(obj_repo).execute(None)
    assert msg_error.value.message == "Moeda não informada!"
