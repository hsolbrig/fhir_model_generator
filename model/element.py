#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Element) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .fhirabstractbase import FHIRAbstractBase



@dataclass
class Element(FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """
    resource_type: ClassVar[str] = "Element"

    id: Optional["str"] = None
    extension: Optional[List["Extension"]] = None