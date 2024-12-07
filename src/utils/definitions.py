#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   definitions.py
@Created :   03/12/2024 14:45:22
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Tratamento da variável da pasta raiz do projeto
    ============================================================================
"""

from pathlib import Path

ROOT_PATH = str(Path(Path(__file__).parent.parent.parent).resolve())
