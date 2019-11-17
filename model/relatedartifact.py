#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .element import Element
from .fhirreference import FHIRReference


@dataclass
class RelatedArtifact(Element):
    """ Related artifacts for a knowledge resource.

    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    resource_type: ClassVar[str] = "RelatedArtifact"

    type: str = None
    display: Optional[str] = None
    citation: Optional[str] = None
    url: Optional[str] = None
    document: Optional[Attachment] = None
    resource: Optional[FHIRReference] = None