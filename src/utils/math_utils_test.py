#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   math_utils_test.py
@Created :   08/12/2024 09:18:02
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes das funções utilitárias mateméticas
    ============================================================================
"""
import numpy as np
import pandas as pd

import src.utils.math_utils as fmu


def test_get_minvalue():
    my_list_1 = [1, 2, 3]

    assert fmu.get_minvalue(my_list_1) == 1


def test_is_int():
    assert fmu.is_int(10) is True
    assert fmu.is_int(10.5) is False
    assert fmu.is_int(10 ** (1 / 2)) is False
    assert fmu.is_int("a") is False


def test_is_float():
    assert fmu.is_float(10) is True
    assert fmu.is_float(10.5) is True
    assert fmu.is_float(10 ** (1 / 2)) is True
    assert fmu.is_float("a") is False


def test_safe_divide():
    result = 10 / 3
    assert fmu.safe_divide(10, 3) == result
    assert fmu.safe_divide(10, 0) == 0.0
    assert fmu.safe_divide(10, -2) == -5
    assert fmu.safe_divide(None, None) == 0.0


def test_safe_divide_array():
    a = np.array([1.2, 2.3, 3.4, 4.5, 5.5])
    b = np.array([2, 0, 3, 4, 10])
    c = np.array([1, 2, 3, 4, 5])

    assert (
        fmu.safe_divide_array(a, b) == np.array([0.6, 0.0, 1.133333, 1.125, 0.55])
    ).all()

    assert (fmu.safe_divide_array(c, b) == np.array([0.5, 0.0, 1.0, 1.0, 0.5])).all()
    assert fmu.safe_divide_array(None, b) is None


def test_safe_divide_df():
    col_1 = [10, 20, 30, 40, 50, 60]
    col_2 = [2, 0, 5, 3.2, 1.2, 3]

    dict = {"num": col_1, "den": col_2}
    df_1 = pd.DataFrame(dict)

    result = np.array([5.0, 0.0, 6.0, 12.5, 41.666667, 20], dtype=float)

    assert (fmu.safe_divide_df(df_1, "num", "den") == result).all()
    assert fmu.safe_divide_df(None, "num", "den") is None
    assert fmu.safe_divide_df(None, 1, 2) is None
    assert fmu.safe_divide_df(df_1, "xx", "zz") is None
