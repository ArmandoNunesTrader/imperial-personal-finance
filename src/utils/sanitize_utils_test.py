#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   sanitize_utils_test.py
@Created :   12/12/2024 15:43:27
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Testes das funções utilitárias de sanitização de strings
    ============================================================================
"""

import src.utils.sanitize_utils as fsn

str_aux_1 = " Minha String "
str_aux_1_o = "minha string"
str_aux_2 = "<Minha String>"
str_aux_2_o = "MINHA STRING"
str_aux_3 = '"Minha String"'
str_aux_3_o = "Minha String"
str_aux_4 = "THIS TEXT WILL BE LOWERCASED. THIS WON'T: ßßß"
str_aux_4_o = "this text will be lowercased. this won't: ssssss"
str_aux_5 = "Here's <a href='https://example.com'> a tag</a>"
str_aux_5_o = r"Here's  a tag"
str_aux_6 = """
<body>
<div> This is a sample text with <b>lots of tags</b> </div>
<br/>
</body>
"""
str_aux_6_o = "This is a sample text with lots of tags"

str_aux_7 = "     \t\tA      text\t\t\t\n\n sample       "
str_aux_7_o = "A text sample"
str_aux_8 = "A lot of !!!! .... ,,,, ;;;;;;;?????"
str_aux_8_o = "A lot of"
str_aux_9 = (
    "Remove these numbers: 1919191 2229292 11.233 22/22/22. "
    + "But don't remove this one H2O"
)
str_aux_9_o = "Remove these numbers: .//. But don't remove this one H2O"
str_aux_10 = "I want to keep this one: 10/10/20 but not this one 222333"
str_aux_10_o = "I want to keep this one: 10/10/20 but not this one"
str_aux_11 = "Sample text with numbers 123455 and words !!!"
str_aux_11_o = "Sample text with numbers and words"
str_aux_12 = "Sample text 123 !!!! Haha.... !!!! ##$$$%%%%"
str_aux_12_o = "Sample text 123  Haha"
str_aux_13 = "I love 🥑"
str_aux_13_o = "I love :avocado:"
str_aux_14 = "hellooooo"
str_aux_14_o = "hello"
str_aux_15 = "minicurso de python para mulheres"
str_aux_15_o = "Minicurso de Python para Mulheres"
str_aux_16 = "1e7297ee-a97d-4fc4-ad69-f3c3ed37dea3*& "
str_aux_16_o = "1e7297ee-a97d-4fc4-ad69-f3c3ed37dea3"

str_filename_1 = r"ar\quivo\\_de_testes.txt"
str_filename_1_o = "ar_quivo___de_testes.txt"


def test_sanitize_filename():
    assert fsn.sanitize_filename(str_filename_1) == str_filename_1_o


def test_sanitize_str_to_lower():
    assert fsn.sanitize_str_to_lower(str_aux_1) == str_aux_1_o


def test_sanitize_str_to_casefold():
    assert fsn.sanitize_str_to_casefold(str_aux_4) == str_aux_4_o


def test_sanitize_str_to_upper():
    assert fsn.sanitize_str_to_upper(str_aux_2) == str_aux_2_o


def test_sanitize_str_to_title():
    assert fsn.sanitize_str_to_title(str_aux_3) == str_aux_3_o


def test_sanitize_remove_a_tag():
    assert fsn.sanitize_remove_a_tag(str_aux_5) == str_aux_5_o


def test_sanitize_remove_extra_spaces_tabs_and_line_breaks():
    assert (
        fsn.sanitize_remove_extra_spaces_tabs_and_line_breaks(str_aux_7) == str_aux_7_o
    )


def test_sanitize_remove_all_html_tags():
    assert fsn.sanitize_remove_all_html_tags(str_aux_6) == str_aux_6_o


def test_sanitize_remove_ponctuation():
    assert fsn.sanitize_remove_ponctuation(str_aux_8) == str_aux_8_o


def test_sanitize_remove_numbers():
    assert fsn.sanitize_remove_numbers(str_aux_9) == str_aux_9_o


def test_sanitize_remove_gigits():
    assert fsn.sanitize_remove_digits(str_aux_10) == str_aux_10_o


def test_sanitize_remove_non_alphabetic():
    assert fsn.sanitize_remove_non_alphabetic(str_aux_11) == str_aux_11_o


def test_sanitize_uuid():
    assert fsn.sanitize_uuid(str_aux_16) == str_aux_16_o


def test_sanitize_remove_all_special_chars_and_ponctuation():
    assert (
        fsn.sanitize_remove_all_special_chars_and_ponctuation(str_aux_12)
        == str_aux_12_o
    )


def test_sanitize_transforme_emojis_in_chars():
    assert fsn.sanitize_transforme_emojis_in_chars(str_aux_13) == str_aux_13_o


def test_sanitize_remove_repeated_chars():
    assert fsn.sanitize_remove_repeated_chars(str_aux_14) == str_aux_14_o


def test_sanitize_capitalize_without_pt_br_prepositions():
    assert (
        fsn.sanitize_capitalize_without_pt_br_prepositions(str_aux_15) == str_aux_15_o
    )


def test_sanitize_pt_br_phrase_capitalize():
    str_aux = (
        str_aux_7
        + str_aux_8
        + str_aux_11
        + str_aux_12
        + str_aux_13
        + str_aux_14
        + str_aux_15
    )
    str_aux_o = (
        "A Text Sample a Lot Of Text With Numbers "
        + "And Words Text Love de Python para Mulheres"
    )

    assert fsn.sanitize_pt_br_phrase_capitalize("Sigla Moeda") == "Sigla Moeda"
    assert (
        fsn.sanitize_pt_br_phrase_capitalize("Descrição Moeda de Testes")
        == "Descrição Moeda de Testes"
    )
    assert fsn.sanitize_pt_br_phrase_capitalize("BRL") == "Brl"

    assert fsn.sanitize_pt_br_phrase_capitalize(str_aux) == str_aux_o


def test_sanitize_pt_br_phrase_upper():
    assert fsn.sanitize_pt_br_phrase_upper("BRL") == "BRL"
