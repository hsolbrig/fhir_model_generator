#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period


@dataclass
class PaymentReconciliationDetail(BackboneElement):
    """ List of settlements.

    List of individual settlement amounts and the corresponding transaction.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationDetail"

    type: CodeableConcept = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    submitter: Optional[FHIRReference] = None
    payee: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    amount: Optional[Money] = None


@dataclass
class PaymentReconciliationProcessNote(BackboneElement):
    """ Processing comments.

    Suite of notes.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationProcessNote"

    type: Optional[CodeableConcept] = None
    text: Optional[str] = None


@dataclass
class PaymentReconciliation(DomainResource):
    """ PaymentReconciliation resource.

    This resource provides payment details and claim references supporting a
    bulk payment.
    """
    resource_type: ClassVar[str] = "PaymentReconciliation"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    period: Optional[Period] = None
    created: Optional[FHIRDate] = None
    organization: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    disposition: Optional[str] = None
    requestProvider: Optional[FHIRReference] = None
    requestOrganization: Optional[FHIRReference] = None
    detail: Optional[List[PaymentReconciliationDetail]] = None
    form: Optional[CodeableConcept] = None
    total: Optional[Money] = None
    processNote: Optional[List[PaymentReconciliationProcessNote]] = None