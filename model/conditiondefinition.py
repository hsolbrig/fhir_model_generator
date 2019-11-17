#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/ConditionDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .usagecontext import UsageContext


@dataclass
class ConditionDefinitionObservation(BackboneElement):
    """ Observations particularly relevant to this condition.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionObservation"

    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None


@dataclass
class ConditionDefinitionMedication(BackboneElement):
    """ Medications particularly relevant for this condition.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionMedication"

    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None


@dataclass
class ConditionDefinitionPrecondition(BackboneElement):
    """ Observation that suggets this condition.

    An observation that suggests that this condition applies.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionPrecondition"

    type: str = None
    code: CodeableConcept = None
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class ConditionDefinitionQuestionnaire(BackboneElement):
    """ Questionnaire for this condition.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionQuestionnaire"

    purpose: str = None
    reference: FHIRReference = None


@dataclass
class ConditionDefinitionPlan(BackboneElement):
    """ Plan that is appropriate.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionPlan"

    role: Optional[CodeableConcept] = None
    reference: FHIRReference = None


@dataclass
class ConditionDefinition(DomainResource):
    """ A definition of a condition.

    A definition of a condition and information relevant to managing it.
    """
    resource_type: ClassVar[str] = "ConditionDefinition"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    severity: Optional[CodeableConcept] = None
    bodySite: Optional[CodeableConcept] = None
    stage: Optional[CodeableConcept] = None
    hasSeverity: Optional[bool] = None
    hasBodySite: Optional[bool] = None
    hasStage: Optional[bool] = None
    definition: Optional[List[str]] = None
    observation: Optional[List[ConditionDefinitionObservation]] = None
    medication: Optional[List[ConditionDefinitionMedication]] = None
    precondition: Optional[List[ConditionDefinitionPrecondition]] = None
    team: Optional[List[FHIRReference]] = None
    questionnaire: Optional[List[ConditionDefinitionQuestionnaire]] = None
    plan: Optional[List[ConditionDefinitionPlan]] = None