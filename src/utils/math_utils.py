#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   math_utils.py
@Created :   08/12/2024 09:12:14
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Funções utilitárias para cálculos mateméticos
    ============================================================================
"""
import numpy as np
import pandas as pd


def get_minvalue(input_list) -> int | float:
    min_value = min(input_list)
    return min_value


# Verifica se um valor é um inteiro
def is_int(val: int | float) -> bool:
    return isinstance(val, int)


# Verifica se um valor é um ponto flutuante
def is_float(val: int | float) -> bool:
    return isinstance(val, float) | isinstance(val, int)


# Divisão segura entre dois valores
def safe_divide(a: int | float, b: int | float) -> float:
    if is_float(a) and is_float(b):
        result = a / b if b != 0 else 0
    else:
        result = 0.0

    return result


# Divisão segura de valores zerados em arrays
def safe_divide_array(arr_num: np.array, arr_den: np.array) -> np.array:
    try:
        arr_den = np.array(arr_den, dtype=float)
        arr_num = np.array(arr_num, dtype=float)
        c = np.round(
            np.divide(
                arr_num,
                arr_den,
                out=np.zeros_like(arr_num, dtype=float),
                where=arr_den != 0,
            ),
            6,
        )

    except ValueError:
        c = None

    return c


# Divisão segura de valores zerados em colunas de um dataframe
def safe_divide_df(df: pd.DataFrame, col_num: str, col_den: str) -> np.array:
    if not isinstance(df, pd.DataFrame):
        return None

    if not ((col_num in df.columns) and (col_den in df.columns)):
        return None

    a = np.array(df[col_num], dtype=float)
    b = np.array(df[col_den], dtype=float)

    c = np.round(np.divide(a, b, out=np.zeros_like(a, dtype=float), where=b != 0), 6)

    return c
