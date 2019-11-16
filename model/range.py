#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Range) on 2019-11-16.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .quantity import Quantity


@dataclass
class Range(Element):
    """ Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """
    resource_type: ClassVar[str] = "Range"

    low: Optional[Quantity] = None
    high: Optional[Quantity] = None