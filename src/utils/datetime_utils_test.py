#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   datetime_utils_test.py
@Created :   03/12/2024 11:53:44
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes das funções utilitárias de tratamento de data/hora
    ============================================================================
"""

from datetime import datetime, timezone

import pytz

import src.utils.datetime_utils as fdtu


def test_dt_now_utc():
    assert fdtu.dt_now_utc() == datetime.now(timezone.utc)


def test_dt_in_past():
    base_past = datetime.strptime("2024-12-01 10:11:12", "%Y-%m-%d %H:%M:%S")
    base_future = datetime.strptime("2200-12-01 10:11:12", "%Y-%m-%d %H:%M:%S")

    assert fdtu.dt_in_past(base_past) is True
    assert fdtu.dt_in_past(base_future) is False


def test_date_now_brasilia():
    aux = datetime.now(pytz.timezone("America/Sao_Paulo")).date()

    assert fdtu.date_now_brasilia() == aux


def test_date_now_utc():
    aux = fdtu.dt_now_utc().date()

    assert fdtu.date_now_utc() == aux


def test_time_now_brasilia():
    aux = datetime.now(pytz.timezone("America/Sao_Paulo")).time()

    assert fdtu.time_now_brasilia() == aux


def test_time_now_utc():
    aux = fdtu.dt_now_utc().time()

    assert fdtu.time_now_utc() == aux
