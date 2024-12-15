#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   sanitize_utils.py
@Created :   12/12/2024 15:39:18
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Rotinas de sanitização de strings
    ============================================================================
"""

from string import punctuation
from emoji import demojize

import re


def sanitize_filename(filename: str) -> str:
    return filename.strip().replace("/", "_").replace("\\", "_")


def sanitize_str_to_lower(str_in: str) -> str:
    return str_in.strip().strip("<>").replace('"', "").lower()


def sanitize_str_to_casefold(str_in: str) -> str:
    return str_in.strip().strip("<>").replace('"', "").casefold()


def sanitize_str_to_upper(str_in: str) -> str:
    return str_in.strip().strip("<>").replace('"', "").upper()


def sanitize_str_to_title(str_in: str) -> str:
    return str_in.strip().strip("<>").replace('"', "").title()


def sanitize_remove_a_tag(str_in: str) -> str:
    return re.sub(r"<a[^>]*>(.*?)</a>", r"\1", str_in)


def sanitize_remove_extra_spaces_tabs_and_line_breaks(str_in: str) -> str:
    return " ".join(str_in.split())


def sanitize_remove_all_html_tags(str_in: str) -> str:
    return sanitize_remove_extra_spaces_tabs_and_line_breaks(
        re.sub(r"<.*?>", " ", str_in).strip()
    )


def sanitize_remove_ponctuation(str_in: str) -> str:
    return re.sub(f"[{re.escape(punctuation)}]", "", str_in).strip()


def sanitize_remove_numbers(str_in: str) -> str:
    return re.sub(r"\b[0-9]+\b\s*", "", str_in)


def sanitize_remove_digits(str_in: str) -> str:
    return " ".join(
        [w for w in str_in.split() if not w.isdigit()]
    )  # Side effect: removes extra spaces


def sanitize_remove_non_alphabetic(str_in: str) -> str:
    return " ".join(
        [w for w in str_in.split() if w.isalpha()]
    )  # Side effect: removes extra spaces


def sanitize_uuid(str_in: str) -> str:
    return "".join(w for w in str_in if (w.isalnum() or (w == "-")))


def sanitize_remove_all_special_chars_and_ponctuation(str_in: str) -> str:
    return re.sub(r"[^A-Za-z0-9\s]+", "", str_in).strip()


def sanitize_transforme_emojis_in_chars(str_in: str) -> str:
    return demojize(str_in)


def sanitize_remove_repeated_chars(str_in: str) -> str:
    return re.sub(r"(.)\1{3,}", r"\1", str_in)


def sanitize_capitalize_without_pt_br_prepositions(str_in: str) -> str:
    p = ["da", "de", "di", "do", "du", "para", "o", "a", "os", "as", "e"]
    result = " ".join(
        list(map(lambda w: w if w in p else w.capitalize(), str_in.split()))
    )

    result = result.split()
    if result[0] in p:
        result[0] = result[0].title()

    return " ".join(result)


def sanitize_pt_br_phrase_capitalize(str_in: str) -> str:
    aux = sanitize_str_to_lower(str_in)
    aux = sanitize_remove_a_tag(aux)
    aux = sanitize_remove_extra_spaces_tabs_and_line_breaks(aux)
    aux = sanitize_remove_all_html_tags(aux)
    aux = sanitize_remove_non_alphabetic(aux)
    aux = sanitize_remove_ponctuation(aux)
    aux = sanitize_transforme_emojis_in_chars(aux)
    aux = sanitize_remove_repeated_chars(aux)
    aux = sanitize_capitalize_without_pt_br_prepositions(aux)

    return aux


def sanitize_pt_br_phrase_upper(str_in: str) -> str:
    aux = sanitize_capitalize_without_pt_br_prepositions(str_in)

    return aux.upper()
