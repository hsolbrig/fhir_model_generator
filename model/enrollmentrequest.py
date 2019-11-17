#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class EnrollmentRequest(DomainResource):
    """ Enrollment request.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    resource_type: ClassVar[str] = "EnrollmentRequest"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    created: Optional[FHIRDate] = None
    insurer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    subject: Optional[FHIRReference] = None
    coverage: Optional[FHIRReference] = None