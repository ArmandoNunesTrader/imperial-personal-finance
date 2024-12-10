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


utc_aux = datetime(2024, 12, 1, 18, 50, 45, 0, tzinfo=pytz.UTC)
utc_aux_f = datetime(2024, 12, 1, 15, 50, 45, 0)

brasilia_aux = datetime(
    2024, 12, 1, 15, 50, 45, 0, tzinfo=pytz.timezone("America/Sao_Paulo")
)
brasilia_aux_f = datetime(2024, 12, 1, 18, 50, 45, 0)


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


def test_date_dd_mm_yyyy():
    now = str(datetime.now().date())
    now_out = datetime.strptime(now, "%Y-%m-%d").strftime("%d-%m-%Y")

    assert fdtu.date_dd_mm_yyyy(now) == now_out


def test_time_hh_mm_ss():
    now = datetime.now().time()
    now_out = now.strftime("%H:%M:%S")

    assert fdtu.time_hh_mm_ss(now) == now_out


def test_datetime_dd_mm_yyyy_hh_mm_ss():
    now_aux = datetime.now()
    now_date = str(now_aux.date())
    now_time = now_aux.time()
    now_out_date = datetime.strptime(now_date, "%Y-%m-%d").strftime("%d-%m-%Y")
    now_out_time = now_time.strftime("%H:%M:%S")

    assert (
        fdtu.datetime_dd_mm_yyyy_hh_mm_ss(now_aux) == now_out_date + " " + now_out_time
    )


def test_dt_from_utc_to_brasilia():
    assert fdtu.dt_from_utc_to_brasilia(utc_aux) == utc_aux_f


def test_dt_from_brasilia_to_utc():
    assert fdtu.dt_from_brasila_to_utc(brasilia_aux) == brasilia_aux_f
