#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class EnrollmentResponse(DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an Enrollment resource.
    """
    resource_type: ClassVar[str] = "EnrollmentResponse"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    disposition: Optional[str] = None
    created: Optional[FHIRDate] = None
    organization: Optional[FHIRReference] = None
    requestProvider: Optional[FHIRReference] = None
    requestOrganization: Optional[FHIRReference] = None