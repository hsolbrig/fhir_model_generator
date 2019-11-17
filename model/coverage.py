#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CoverageGrouping(BackboneElement):
    """ Additional coverage classifications.

    A suite of underwrite specific classifiers, for example may be used to
    identify a class of coverage or employer group, Policy, Plan.
    """
    resource_type: ClassVar[str] = "CoverageGrouping"

    group: Optional[str] = None
    groupDisplay: Optional[str] = None
    subGroup: Optional[str] = None
    subGroupDisplay: Optional[str] = None
    plan: Optional[str] = None
    planDisplay: Optional[str] = None
    subPlan: Optional[str] = None
    subPlanDisplay: Optional[str] = None
    class_fhir: Optional[str] = field(default=None, metadata=dict(orig_name='class'))
    classDisplay: Optional[str] = None
    subClass: Optional[str] = None
    subClassDisplay: Optional[str] = None


@dataclass
class Coverage(DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services.
    """
    resource_type: ClassVar[str] = "Coverage"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    policyHolder: Optional[FHIRReference] = None
    subscriber: Optional[FHIRReference] = None
    subscriberId: Optional[str] = None
    beneficiary: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    period: Optional[Period] = None
    payor: Optional[List[FHIRReference]] = None
    grouping: Optional[CoverageGrouping] = None
    dependent: Optional[str] = None
    sequence: Optional[str] = None
    order: Optional[int] = None
    network: Optional[str] = None
    contract: Optional[List[FHIRReference]] = None