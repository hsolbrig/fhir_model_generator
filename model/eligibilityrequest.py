#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/EligibilityRequest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class EligibilityRequest(DomainResource):
    """ Determine insurance validity and scope of coverage.

    The EligibilityRequest provides patient and insurance coverage information
    to an insurer for them to respond, in the form of an EligibilityResponse,
    with information regarding whether the stated coverage is valid and in-
    force and optionally to provide the insurance details of the policy.
    """
    resource_type: ClassVar[str] = "EligibilityRequest"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    priority: Optional[CodeableConcept] = None
    patient: Optional[FHIRReference] = None
    servicedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='serviced',))
    servicedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='serviced',))
    created: Optional[FHIRDate] = None
    enterer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    insurer: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    coverage: Optional[FHIRReference] = None
    businessArrangement: Optional[str] = None
    benefitCategory: Optional[CodeableConcept] = None
    benefitSubCategory: Optional[CodeableConcept] = None