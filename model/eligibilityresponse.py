#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse) on 2019-11-17.
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


@dataclass
class EligibilityResponseInsuranceBenefitBalanceFinancial(BackboneElement):
    """ Benefit Summary.

    Benefits Used to date.
    """
    resource_type: ClassVar[str] = "EligibilityResponseInsuranceBenefitBalanceFinancial"

    type: CodeableConcept = None
    allowedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedString: Optional[str] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='allowed',))
    usedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='used',))
    usedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='used',))


@dataclass
class EligibilityResponseInsuranceBenefitBalance(BackboneElement):
    """ Benefits by Category.

    Benefits and optionally current balances by Category.
    """
    resource_type: ClassVar[str] = "EligibilityResponseInsuranceBenefitBalance"

    category: CodeableConcept = None
    subCategory: Optional[CodeableConcept] = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    financial: Optional[List[EligibilityResponseInsuranceBenefitBalanceFinancial]] = None


@dataclass
class EligibilityResponseInsurance(BackboneElement):
    """ Details by insurance coverage.

    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """
    resource_type: ClassVar[str] = "EligibilityResponseInsurance"

    coverage: Optional[FHIRReference] = None
    contract: Optional[FHIRReference] = None
    benefitBalance: Optional[List[EligibilityResponseInsuranceBenefitBalance]] = None


@dataclass
class EligibilityResponseError(BackboneElement):
    """ Processing errors.

    Mutually exclusive with Services Provided (Item).
    """
    resource_type: ClassVar[str] = "EligibilityResponseError"

    code: CodeableConcept = None


@dataclass
class EligibilityResponse(DomainResource):
    """ EligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """
    resource_type: ClassVar[str] = "EligibilityResponse"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    created: Optional[FHIRDate] = None
    requestProvider: Optional[FHIRReference] = None
    requestOrganization: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    disposition: Optional[str] = None
    insurer: Optional[FHIRReference] = None
    inforce: Optional[bool] = None
    insurance: Optional[List[EligibilityResponseInsurance]] = None
    form: Optional[CodeableConcept] = None
    error: Optional[List[EligibilityResponseError]] = None