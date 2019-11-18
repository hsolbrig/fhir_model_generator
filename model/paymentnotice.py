#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money


@dataclass
class PaymentNotice(DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    resource_type: ClassVar[str] = "PaymentNotice"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    created: FHIRDate = None
    provider: Optional[FHIRReference] = None
    payment: FHIRReference = None
    paymentDate: Optional[FHIRDate] = None
    payee: Optional[FHIRReference] = None
    recipient: FHIRReference = None
    amount: Money = None
    paymentStatus: Optional[CodeableConcept] = None