#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Observation) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .sampleddata import SampledData


@dataclass
class ObservationReferenceRange(BackboneElement):
    """ Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """
    resource_type: ClassVar[str] = "ObservationReferenceRange"

    low: Optional[Quantity] = None
    high: Optional[Quantity] = None
    type: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = None
    age: Optional[Range] = None
    text: Optional[str] = None


@dataclass
class ObservationRelated(BackboneElement):
    """ Resource related to this observation.

    A  reference to another resource (usually another Observation) whose
    relationship is defined by the relationship type code.
    """
    resource_type: ClassVar[str] = "ObservationRelated"

    type: Optional[str] = None
    target: FHIRReference = None


@dataclass
class ObservationComponent(BackboneElement):
    """ Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """
    resource_type: ClassVar[str] = "ObservationComponent"

    code: CodeableConcept = None
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='value',))
    valueRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='value',))
    valueSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='value',))
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[CodeableConcept] = None
    referenceRange: Optional[List[ObservationReferenceRange]] = None


@dataclass
class Observation(DomainResource):
    """ Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    resource_type: ClassVar[str] = "Observation"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    status: str = None
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    subject: Optional[FHIRReference] = None
    context: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='effective',))
    effectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='effective',))
    issued: Optional[FHIRDate] = None
    performer: Optional[List[FHIRReference]] = None
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='value',))
    valueRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='value',))
    valueSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='value',))
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[CodeableConcept] = None
    comment: Optional[str] = None
    bodySite: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    referenceRange: Optional[List[ObservationReferenceRange]] = None
    related: Optional[List[ObservationRelated]] = None
    component: Optional[List[ObservationComponent]] = None