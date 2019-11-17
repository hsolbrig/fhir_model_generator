#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .timing import Timing


@dataclass
class DeviceUseStatement(DomainResource):
    """ Record of use of a device.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    resource_type: ClassVar[str] = "DeviceUseStatement"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    subject: FHIRReference = None
    whenUsed: Optional[Period] = None
    timingTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    timingDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    recordedOn: Optional[FHIRDate] = None
    source: Optional[FHIRReference] = None
    device: FHIRReference = None
    indication: Optional[List[CodeableConcept]] = None
    bodySite: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = None