#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/ClinicalUseIssue) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .population import Population
from .quantity import Quantity


@dataclass
class ClinicalUseIssueInteractionInteractant(BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueInteractionInteractant"

    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class ClinicalUseIssueContraindicationOtherTherapy(BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueContraindicationOtherTherapy"

    therapyRelationshipType: CodeableConcept = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))


@dataclass
class ClinicalUseIssueContraindication(BackboneElement):
    """ Specifics for when this is a contraindication.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueContraindication"

    diseaseSymptomProcedure: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = None
    indication: Optional[List[FHIRReference]] = None
    otherTherapy: Optional[List[ClinicalUseIssueContraindicationOtherTherapy]] = None


@dataclass
class ClinicalUseIssueIndication(BackboneElement):
    """ Specifics for when this is an indication.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueIndication"

    diseaseSymptomProcedure: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = None
    intendedEffect: Optional[CodeableConcept] = None
    duration: Optional[Quantity] = None
    undesirableEffect: Optional[List[FHIRReference]] = None
    otherTherapy: Optional[List[ClinicalUseIssueContraindicationOtherTherapy]] = None


@dataclass
class ClinicalUseIssueInteraction(BackboneElement):
    """ Specifics for when this is an interaction.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueInteraction"

    interactant: Optional[List[ClinicalUseIssueInteractionInteractant]] = None
    type: Optional[CodeableConcept] = None
    effect: Optional[CodeableConcept] = None
    incidence: Optional[CodeableConcept] = None
    management: Optional[CodeableConcept] = None


@dataclass
class ClinicalUseIssueUndesirableEffect(BackboneElement):
    """ A possible negative outcome from the use of this treatment.

    Describe the undesirable effects of the medicinal product.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueUndesirableEffect"

    symptomConditionEffect: Optional[CodeableConcept] = None
    classification: Optional[CodeableConcept] = None
    frequencyOfOccurrence: Optional[CodeableConcept] = None


@dataclass
class ClinicalUseIssue(DomainResource):
    """ A single item of clinical particulars - an indication, contraindication,
    interaction etc. for a medicinal product.

    A single usage issue - either an indication, contraindication, interaction
    or an undesirable effect for a medicinal product, medication, device or
    procedure.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssue"

    identifier: Optional[List[Identifier]] = None
    type: str = None
    subject: Optional[List[FHIRReference]] = None
    status: Optional[CodeableConcept] = None
    description: Optional[str] = None
    contraindication: Optional[ClinicalUseIssueContraindication] = None
    indication: Optional[ClinicalUseIssueIndication] = None
    interaction: Optional[ClinicalUseIssueInteraction] = None
    population: Optional[List[Population]] = None
    undesirableEffect: Optional[ClinicalUseIssueUndesirableEffect] = None