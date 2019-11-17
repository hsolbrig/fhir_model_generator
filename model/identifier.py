#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Identifier) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .element import Element
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class Identifier(Element):
    """ An identifier intended for computation.

    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """
    resource_type: ClassVar[str] = "Identifier"

    use: Optional[str] = None
    type: Optional[CodeableConcept] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional[Period] = None
    assigner: Optional[FHIRReference] = None