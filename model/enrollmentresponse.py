#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class EnrollmentResponse(DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    resource_type: ClassVar[str] = "EnrollmentResponse"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[str] = None
    disposition: Optional[str] = None
    created: Optional[FHIRDate] = None
    organization: Optional[FHIRReference] = None
    requestProvider: Optional[FHIRReference] = None