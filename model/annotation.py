#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Annotation) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference


@dataclass
class Annotation(Element):
    """ Text node with attribution.

    A  text note which also  contains information about who made the statement
    and when.
    """
    resource_type: ClassVar[str] = "Annotation"

    authorReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='author',))
    authorString: Optional[str] = field(default=None, metadata=dict(one_of_many='author',))
    time: Optional[FHIRDate] = None
    text: str = None