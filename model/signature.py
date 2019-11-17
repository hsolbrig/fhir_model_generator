#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Signature) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .coding import Coding
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference


@dataclass
class Signature(Element):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..

    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """
    resource_type: ClassVar[str] = "Signature"

    type: List[Coding] = field(default_factory=list)
    when: FHIRDate = None
    whoUri: str = field(default=None, metadata=dict(one_of_many='who',))
    whoReference: FHIRReference = field(default=None, metadata=dict(one_of_many='who',))
    onBehalfOfUri: Optional[str] = field(default=None, metadata=dict(one_of_many='onBehalfOf',))
    onBehalfOfReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='onBehalfOf',))
    contentType: Optional[str] = None
    blob: Optional[str] = None