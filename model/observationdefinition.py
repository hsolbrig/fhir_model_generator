#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range
from .usagecontext import UsageContext


@dataclass
class ObservationDefinitionQuantitativeDetails(BackboneElement):
    """ Characteristics of quantitative results.

    Characteristics for quantitative results of this observation.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQuantitativeDetails"

    customaryUnit: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    conversionFactor: Optional[float] = None
    decimalPrecision: Optional[int] = None


@dataclass
class ObservationDefinitionQualifiedInterval(BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQualifiedInterval"

    category: Optional[str] = None
    range: Optional[Range] = None
    context: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = None
    gender: Optional[str] = None
    age: Optional[Range] = None
    gestationalAge: Optional[Range] = None
    condition: Optional[str] = None


@dataclass
class ObservationDefinitionComponent(BackboneElement):
    """ Component results.

    Some observations have multiple component observations, expressed as
    separate code value pairs.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionComponent"

    code: CodeableConcept = None
    permittedDataType: Optional[List[str]] = None
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = None


@dataclass
class ObservationDefinition(DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    resource_type: ClassVar[str] = "ObservationDefinition"

    url: Optional[str] = None
    identifier: Optional[Identifier] = None
    version: Optional[str] = None
    title: Optional[str] = None
    derivedFromCanonical: Optional[List[str]] = None
    derivedFromUri: Optional[List[str]] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='subject',))
    subjectReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='subject',))
    date: Optional[FHIRDate] = None
    publisher: Optional[FHIRReference] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    performerType: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    permittedDataType: Optional[List[str]] = None
    multipleResultsAllowed: Optional[bool] = None
    bodySite: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    preferredReportName: Optional[str] = None
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = None
    validCodedValueSet: Optional[FHIRReference] = None
    normalCodedValueSet: Optional[FHIRReference] = None
    abnormalCodedValueSet: Optional[FHIRReference] = None
    criticalCodedValueSet: Optional[FHIRReference] = None
    hasMember: Optional[List[FHIRReference]] = None
    component: Optional[List[ObservationDefinitionComponent]] = None