#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class GuidanceResponse(DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    resource_type: ClassVar[str] = "GuidanceResponse"

    requestId: Optional[str] = None
    identifier: Optional[Identifier] = None
    module: FHIRReference = None
    status: str = None
    subject: Optional[FHIRReference] = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    performer: Optional[FHIRReference] = None
    reasonCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='reason',))
    reasonReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='reason',))
    note: Optional[List[Annotation]] = None
    evaluationMessage: Optional[List[FHIRReference]] = None
    outputParameters: Optional[FHIRReference] = None
    result: Optional[FHIRReference] = None
    dataRequirement: Optional[List[DataRequirement]] = None