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
        Classe de funções diversas de tratamento de data/hora
    ============================================================================
"""

import pytz

from datetime import datetime, timezone


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
def date_now_utc() -> datetime.date:
    now_aux = now_aux = dt_now_utc().date()

    return now_aux


# Obtém a hora atual na timezone de Brasília
def time_now_brasilia() -> datetime.time:
    now_aux = datetime.now(pytz.timezone("America/Sao_Paulo")).time()

    return now_aux


# Obtém a hora atual na timezone UTC
def time_now_utc() -> datetime.time:
    now_aux = now_aux = dt_now_utc().time()

    return now_aux
