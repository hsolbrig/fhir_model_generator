#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class BackboneElement(Element):
    """ Base for elements defined inside a resource.

    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """
    resource_type: ClassVar[str] = "BackboneElement"

    modifierExtension = None