#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2019-11-17.
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
from .quantity import Quantity


@dataclass
class ImmunizationPractitioner(BackboneElement):
    """ Who performed event.

    Indicates who or what performed the event.
    """
    resource_type: ClassVar[str] = "ImmunizationPractitioner"

    role: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class ImmunizationExplanation(BackboneElement):
    """ Administration/non-administration reasons.

    Reasons why a vaccine was or was not administered.
    """
    resource_type: ClassVar[str] = "ImmunizationExplanation"

    reason: Optional[List[CodeableConcept]] = None
    reasonNotGiven: Optional[List[CodeableConcept]] = None


@dataclass
class ImmunizationReaction(BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    resource_type: ClassVar[str] = "ImmunizationReaction"

    date: Optional[FHIRDate] = None
    detail: Optional[FHIRReference] = None
    reported: Optional[bool] = None


@dataclass
class ImmunizationVaccinationProtocol(BackboneElement):
    """ What protocol was followed.

    Contains information about the protocol(s) under which the vaccine was
    administered.
    """
    resource_type: ClassVar[str] = "ImmunizationVaccinationProtocol"

    doseSequence: Optional[int] = None
    description: Optional[str] = None
    authority: Optional[FHIRReference] = None
    series: Optional[str] = None
    seriesDoses: Optional[int] = None
    targetDisease: List[CodeableConcept] = field(default_factory=list)
    doseStatus: CodeableConcept = None
    doseStatusReason: Optional[CodeableConcept] = None


@dataclass
class Immunization(DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """
    resource_type: ClassVar[str] = "Immunization"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    notGiven: bool = None
    vaccineCode: CodeableConcept = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    primarySource: bool = None
    reportOrigin: Optional[CodeableConcept] = None
    location: Optional[FHIRReference] = None
    manufacturer: Optional[FHIRReference] = None
    lotNumber: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    doseQuantity: Optional[Quantity] = None
    practitioner: Optional[List[ImmunizationPractitioner]] = None
    note: Optional[List[Annotation]] = None
    explanation: Optional[ImmunizationExplanation] = None
    reaction: Optional[List[ImmunizationReaction]] = None
    vaccinationProtocol: Optional[List[ImmunizationVaccinationProtocol]] = None