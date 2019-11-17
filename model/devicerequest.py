#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .timing import Timing


@dataclass
class DeviceRequestRequester(BackboneElement):
    """ Who/what is requesting diagnostics.

    The individual who initiated the request and has responsibility for its
    activation.
    """
    resource_type: ClassVar[str] = "DeviceRequestRequester"

    agent: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class DeviceRequest(DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    resource_type: ClassVar[str] = "DeviceRequest"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[List[FHIRReference]] = None
    basedOn: Optional[List[FHIRReference]] = None
    priorRequest: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: Optional[str] = None
    intent: CodeableConcept = None
    priority: Optional[str] = None
    codeReference: FHIRReference = field(default=None, metadata=dict(one_of_many='code',))
    codeCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='code',))
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[DeviceRequestRequester] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    relevantHistory: Optional[List[FHIRReference]] = None