#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Expression) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class Expression(Element):
    """ An expression that can be used to generate a value.

    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """
    resource_type: ClassVar[str] = "Expression"

    description: Optional[str] = None
    name: Optional[str] = None
    language: str = None
    expression: Optional[str] = None
    reference: Optional[str] = None