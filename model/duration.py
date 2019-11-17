#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Duration) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .quantity import Quantity


@dataclass
class Duration(Quantity):
    """ A length of time.
    """
    resource_type: ClassVar[str] = "Duration"
