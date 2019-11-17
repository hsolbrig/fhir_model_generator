#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Flag) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Flag(DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """
    resource_type: ClassVar[str] = "Flag"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    subject: FHIRReference = None
    period: Optional[Period] = None
    encounter: Optional[FHIRReference] = None
    author: Optional[FHIRReference] = None