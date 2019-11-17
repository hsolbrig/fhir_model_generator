#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CareTeamParticipant(BackboneElement):
    """ Members of the team.

    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    resource_type: ClassVar[str] = "CareTeamParticipant"

    role: Optional[CodeableConcept] = None
    member: Optional[FHIRReference] = None
    onBehalfOf: Optional[FHIRReference] = None
    period: Optional[Period] = None


@dataclass
class CareTeam(DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.

    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """
    resource_type: ClassVar[str] = "CareTeam"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    category: Optional[List[CodeableConcept]] = None
    name: Optional[str] = None
    subject: Optional[FHIRReference] = None
    context: Optional[FHIRReference] = None
    period: Optional[Period] = None
    participant: Optional[List[CareTeamParticipant]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    managingOrganization: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None