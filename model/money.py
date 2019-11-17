#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Money) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class Money(Element):
    """ An amount of economic utility in some recognized currency.
    """
    resource_type: ClassVar[str] = "Money"

    value: Optional[float] = None
    currency: Optional[str] = None