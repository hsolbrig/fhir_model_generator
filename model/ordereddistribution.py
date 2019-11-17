#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/OrderedDistribution) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .element import Element
from .quantity import Quantity
from .statistic import Statistic


@dataclass
class OrderedDistributionInterval(Element):
    """ Interval.
    """
    resource_type: ClassVar[str] = "OrderedDistributionInterval"

    rankOrder: int = None
    intervalStatistic: Optional[List[Statistic]] = None


@dataclass
class OrderedDistribution(BackboneElement):
    """ An ordered list (distribution) of statistics.
    """
    resource_type: ClassVar[str] = "OrderedDistribution"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    numberOfIntervals: int = None
    bottomOfFirstInterval: Optional[Quantity] = None
    interval: List[OrderedDistributionInterval] = field(default_factory=list)
    topOfInterval: Optional[Quantity] = None