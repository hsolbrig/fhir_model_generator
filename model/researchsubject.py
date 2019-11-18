#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ResearchSubjectProgress(BackboneElement):
    """ Subject status.

    The current state (status) of the subject and resons for status change
    where appropriate.
    """
    resource_type: ClassVar[str] = "ResearchSubjectProgress"

    type: Optional[CodeableConcept] = None
    state: Optional[CodeableConcept] = None
    milestone: Optional[CodeableConcept] = None
    reason: Optional[CodeableConcept] = None
    startDate: FHIRDate = None


@dataclass
class ResearchSubject(DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    resource_type: ClassVar[str] = "ResearchSubject"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    progress: Optional[List[ResearchSubjectProgress]] = None
    period: Optional[Period] = None
    study: FHIRReference = None
    individual: FHIRReference = None
    assignedArm: Optional[str] = None
    actualArm: Optional[str] = None
    consent: Optional[FHIRReference] = None