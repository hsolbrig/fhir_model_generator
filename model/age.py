#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Age) on 2019-11-16.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .quantity import Quantity


@dataclass
class Age(Quantity):
    """ A duration of time during which an organism (or a process) has existed.
    """
    resource_type: ClassVar[str] = "Age"
