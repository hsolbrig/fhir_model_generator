#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2019-11-17.
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
class PaymentNotice(DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    resource_type: ClassVar[str] = "PaymentNotice"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    statusDate: Optional[FHIRDate] = None
    created: Optional[FHIRDate] = None
    target: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    paymentStatus: Optional[CodeableConcept] = None