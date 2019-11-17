#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/SampledData) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .quantity import Quantity


@dataclass
class SampledData(Element):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    resource_type: ClassVar[str] = "SampledData"

    origin: Quantity = None
    period: float = None
    factor: Optional[float] = None
    lowerLimit: Optional[float] = None
    upperLimit: Optional[float] = None
    dimensions: int = None
    data: Optional[str] = None