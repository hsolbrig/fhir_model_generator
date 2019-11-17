#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2019-11-17.
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
class ImmunizationRecommendationRecommendationDateCriterion(BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendationDateCriterion"

    code: CodeableConcept = None
    value: FHIRDate = None


@dataclass
class ImmunizationRecommendationRecommendationProtocol(BackboneElement):
    """ Protocol used by recommendation.

    Contains information about the protocol under which the vaccine was
    administered.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendationProtocol"

    doseSequence: Optional[int] = None
    description: Optional[str] = None
    authority: Optional[FHIRReference] = None
    series: Optional[str] = None


@dataclass
class ImmunizationRecommendationRecommendation(BackboneElement):
    """ Vaccine administration recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendation"

    date: FHIRDate = None
    vaccineCode: Optional[CodeableConcept] = None
    targetDisease: Optional[CodeableConcept] = None
    doseNumber: Optional[int] = None
    forecastStatus: CodeableConcept = None
    dateCriterion: Optional[List[ImmunizationRecommendationRecommendationDateCriterion]] = None
    protocol: Optional[ImmunizationRecommendationRecommendationProtocol] = None
    supportingImmunization: Optional[List[FHIRReference]] = None
    supportingPatientInformation: Optional[List[FHIRReference]] = None


@dataclass
class ImmunizationRecommendation(DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendation"

    identifier: Optional[List[Identifier]] = None
    patient: FHIRReference = None
    recommendation: List[ImmunizationRecommendationRecommendation] = field(default_factory=list)