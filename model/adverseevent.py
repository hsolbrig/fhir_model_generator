#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-11-17.
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


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"

    instance: FHIRReference = None
    causality: Optional[str] = None
    causalityAssessment: Optional[CodeableConcept] = None
    causalityProductRelatedness: Optional[str] = None
    causalityMethod: Optional[CodeableConcept] = None
    causalityAuthor: Optional[FHIRReference] = None
    causalityResult: Optional[CodeableConcept] = None


@dataclass
class AdverseEvent(DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    resource_type: ClassVar[str] = "AdverseEvent"

    identifier: Optional[Identifier] = None
    category: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    reaction: Optional[List[FHIRReference]] = None
    location: Optional[FHIRReference] = None
    seriousness: Optional[CodeableConcept] = None
    outcome: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    eventParticipant: Optional[FHIRReference] = None
    description: Optional[str] = None
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = None
    subjectMedicalHistory: Optional[List[FHIRReference]] = None
    referenceDocument: Optional[List[FHIRReference]] = None
    study: Optional[List[FHIRReference]] = None