#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .contributor import Contributor
from .domainresource import DomainResource
from .dosage import Dosage
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .usagecontext import UsageContext


@dataclass
class ActivityDefinitionParticipant(BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionParticipant"

    type: str = None
    role: Optional[CodeableConcept] = None


@dataclass
class ActivityDefinitionDynamicValue(BackboneElement):
    """ Dynamic aspects of the definition.

    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    intent resource that would contain the result.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionDynamicValue"

    description: Optional[str] = None
    path: Optional[str] = None
    language: Optional[str] = None
    expression: Optional[str] = None


@dataclass
class ActivityDefinition(DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.

    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    resource_type: ClassVar[str] = "ActivityDefinition"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    description: Optional[str] = None
    purpose: Optional[str] = None
    usage: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    topic: Optional[List[CodeableConcept]] = None
    contributor: Optional[List[Contributor]] = None
    contact: Optional[List[ContactDetail]] = None
    copyright: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    library: Optional[List[FHIRReference]] = None
    kind: Optional[str] = None
    code: Optional[CodeableConcept] = None
    timingTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='timing',))
    timingDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    timingRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='timing',))
    location: Optional[FHIRReference] = None
    participant: Optional[List[ActivityDefinitionParticipant]] = None
    productReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='product',))
    productCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='product',))
    quantity: Optional[Quantity] = None
    dosage: Optional[List[Dosage]] = None
    bodySite: Optional[List[CodeableConcept]] = None
    transform: Optional[FHIRReference] = None
    dynamicValue: Optional[List[ActivityDefinitionDynamicValue]] = None