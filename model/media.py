#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Media) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Media(DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    resource_type: ClassVar[str] = "Media"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    type: str = None
    subtype: Optional[CodeableConcept] = None
    view: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    operator: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    bodySite: Optional[CodeableConcept] = None
    device: Optional[FHIRReference] = None
    height: Optional[int] = None
    width: Optional[int] = None
    frames: Optional[int] = None
    duration: Optional[int] = None
    content: Attachment = None
    note: Optional[List[Annotation]] = None