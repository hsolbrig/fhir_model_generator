#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ResearchSubject(DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.

    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    resource_type: ClassVar[str] = "ResearchSubject"

    identifier: Optional[Identifier] = None
    status: str = None
    period: Optional[Period] = None
    study: FHIRReference = None
    individual: FHIRReference = None
    assignedArm: Optional[str] = None
    actualArm: Optional[str] = None
    consent: Optional[FHIRReference] = None