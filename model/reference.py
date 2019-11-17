#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Reference) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class Reference(Element):
    """ A reference from one resource to another.
    """
    resource_type: ClassVar[str] = "Reference"

    reference: Optional[str] = None
    identifier = None
    display: Optional[str] = None