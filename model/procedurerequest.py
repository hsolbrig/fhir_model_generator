#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ProcedureRequest) on 2019-11-17.
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
class ProcedureRequestRequester(BackboneElement):
    """ Who/what is requesting procedure or diagnostic.

    The individual who initiated the request and has responsibility for its
    activation.
    """
    resource_type: ClassVar[str] = "ProcedureRequestRequester"

    agent: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class ProcedureRequest(DomainResource):
    """ A request for a procedure or diagnostic to be performed.

    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """
    resource_type: ClassVar[str] = "ProcedureRequest"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[List[FHIRReference]] = None
    basedOn: Optional[List[FHIRReference]] = None
    replaces: Optional[List[FHIRReference]] = None
    requisition: Optional[Identifier] = None
    status: str = None
    intent: str = None
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    asNeededBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='asNeeded',))
    asNeededCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='asNeeded',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[ProcedureRequestRequester] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    specimen: Optional[List[FHIRReference]] = None
    bodySite: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    relevantHistory: Optional[List[FHIRReference]] = None