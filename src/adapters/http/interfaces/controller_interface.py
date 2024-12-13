#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   controller_interface.py
@Created :   12/12/2024 18:29:26
@Author  :   Armando Nunes
@Version :   1.0
@Contact :   armandojorge.trader@gmail.com
@License :   (C)Copyright 2022-2024, Armando Nunes
"""

"""
    ============================================================================
        Interface do Controller usilizado pelos Adapters
    ============================================================================
"""

from abc import ABC, abstractmethod
from typing import Type

from src.adapters.http.http_types.http_request import HttpRequest
from src.adapters.http.http_types.http_response import HttpResponse


class ControllerInterface(ABC):
    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        pass
