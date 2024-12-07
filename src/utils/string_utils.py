#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   string_utils.py
@Created :   02/12/2024 22:35:32
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Classe de funções utilitárias diversas de tratamento de string
    ============================================================================
"""


def string_repeat(s: str, num: int) -> str:
    return "".join([char * num for char in s])


def substring_after(s: str, delim: str) -> str:
    return s.partition(delim)[2]


def substring_before(s: str, delim: str) -> str:
    return s.partition(delim)[0]


def substring_contains(s: str, substr: str) -> str:
    return str(substr) in s


def last_chars(s: str, chars: int) -> str:
    if len(s) - chars < 1:
        return s
    else:
        return s[len(s) - chars :]


def first_chars(s: str, chars: int) -> str:
    if chars < 1:
        return s
    else:
        return s[:chars]


def first_2_chars(s: str) -> str:
    return first_chars(s, 2)


# Formata um número inteiro com separador de milhar e com espaços à esquerda
def pad_int_left(num: int, len: int) -> str:
    aux = ("{:>" + str(len) + ",.0f}").format(num).replace(",", ".")

    return aux


# Formata uma string preenchendo à direita com caractere definido e
#   alinhando à esquerda para um tamanho definido
def pad_str_left(str: str, len: int, char: str = " "):
    return str.ljust(len, char)


# Formata uma string preenchendo à esquerda com caractere definido e
#   alinhando à direita para um tamanho definido
def pad_str_right(str: str, len: int, char: str = " "):
    return str.rjust(len, char)


# Formata uma string preenchendo à esquerda e à direita com caractere definido e
#   alinhando ao centro para um tamanho definido
def pad_str_center(str: str, len: int, char: str = " "):
    return str.center(len, char)
