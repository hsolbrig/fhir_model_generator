#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Account) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period


@dataclass
class AccountCoverage(BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """
    resource_type: ClassVar[str] = "AccountCoverage"

    coverage: FHIRReference = None
    priority: Optional[int] = None


@dataclass
class AccountGuarantor(BackboneElement):
    """ Responsible for the account.

    Parties financially responsible for the account.
    """
    resource_type: ClassVar[str] = "AccountGuarantor"

    party: FHIRReference = None
    onHold: Optional[bool] = None
    period: Optional[Period] = None


@dataclass
class Account(DomainResource):
    """ Tracks balance, charges, for patient or cost center.

    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """
    resource_type: ClassVar[str] = "Account"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    name: Optional[str] = None
    subject: Optional[FHIRReference] = None
    period: Optional[Period] = None
    active: Optional[Period] = None
    balance: Optional[Money] = None
    coverage: Optional[List[AccountCoverage]] = None
    owner: Optional[FHIRReference] = None
    description: Optional[str] = None
    guarantor: Optional[List[AccountGuarantor]] = None