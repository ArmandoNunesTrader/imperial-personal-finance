#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   datetime_utils.py
@Created :   03/12/2024 11:10:09
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Funções diversas de tratamento de data/hora
    ============================================================================
"""

from datetime import datetime, timezone

import pytz


# Obtém a data/hora atual no padrão UTC
def dt_now_utc() -> datetime:
    return datetime.now(timezone.utc)


# Verifica se uma data/hora está no passado com relação ao horário de Brasília
def dt_in_past(my_now: datetime) -> bool:
    now_aux = dt_now_utc()
    now_aux = now_aux.astimezone(pytz.timezone("America/Sao_Paulo"))

    now_base = my_now.astimezone(pytz.timezone("America/Sao_Paulo"))

    return now_aux > now_base


# Obtém a data atual na timezone de Brasília
def date_now_brasilia() -> datetime.date:
    now_aux = datetime.now(pytz.timezone("America/Sao_Paulo")).date()

    return now_aux


# Obtém a data atual na timezone UTC
def date_now_utc() -> datetime:
    now_aux = dt_now_utc().date()

    return now_aux


# Obtém a hora atual na timezone de Brasília
def time_now_brasilia() -> datetime:
    now_aux = datetime.now(pytz.timezone("America/Sao_Paulo")).time()

    return now_aux


# Obtém a hora atual na timezone UTC
def time_now_utc() -> datetime:
    now_aux = dt_now_utc().time()

    return now_aux


# Formata um campo date no formato dd-mm-aaaa
def date_dd_mm_yyyy(date_in: datetime.date) -> str:
    dt_in = datetime.strptime(str(date_in), "%Y-%m-%d").strftime("%d-%m-%Y")

    return dt_in


# Formata um campo time no formato hh:mm:ss
def time_hh_mm_ss(time_in: datetime.time) -> str:
    dt_in = time_in.strftime("%H:%M:%S")

    return dt_in


# Formata um campo datetime no formato dd-mm-aaaa hh:mm:ss
def datetime_dd_mm_yyyy_hh_mm_ss(datetime_in: datetime) -> str:
    date_in = datetime_in.date()
    time_in = datetime_in.time()

    result = "{} {}".format(date_dd_mm_yyyy(date_in), time_hh_mm_ss(time_in))

    return result


# Converte um datetime do horário UTC para o horário de Brasília
def dt_from_utc_to_brasilia(my_dt: datetime) -> datetime:
    # Aqui geramos e tratamos o timestamp para deixar em UTC
    #   já que o fromtimestamp gera com base na hora local sempre
    utc_aux = my_dt.replace(tzinfo=pytz.utc).timestamp()
    utc_timestamp = utc_aux

    return datetime.fromtimestamp(utc_timestamp)


# Converte um datetime do horário de Brasília para o horário UTC
def dt_from_brasila_to_utc(my_dt: datetime) -> datetime:
    # Aqui geramos e tratamos o timestamp adicionado o dobro da
    #   diferença de fuso
    #   já que o fromtimestamp gera com base na hora local sempre
    utc_aux = my_dt.replace(tzinfo=pytz.utc).timestamp()
    utc_timestamp = utc_aux + (6 * 3600)

    return datetime.fromtimestamp(utc_timestamp)
