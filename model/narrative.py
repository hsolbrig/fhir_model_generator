#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class Narrative(Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).

    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """
    resource_type: ClassVar[str] = "Narrative"

    status: str = None
    div: str = None