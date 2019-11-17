#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/ContactDetail) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .contactpoint import ContactPoint
from .element import Element


@dataclass
class ContactDetail(Element):
    """ Contact information.

    Specifies contact information for a person or organization.
    """
    resource_type: ClassVar[str] = "ContactDetail"

    name: Optional[str] = None
    telecom: Optional[List[ContactPoint]] = None