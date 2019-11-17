#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Evidence) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contributor import Contributor
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .ordereddistribution import OrderedDistribution
from .relatedartifact import RelatedArtifact
from .statistic import Statistic
from .usagecontext import UsageContext


@dataclass
class EvidenceCertaintyCertaintySubcomponent(BackboneElement):
    """ Subcomponent of certainty.
    """
    resource_type: ClassVar[str] = "EvidenceCertaintyCertaintySubcomponent"

    description: Optional[str] = None
    note: Optional[Annotation] = None
    type: Optional[List[CodeableConcept]] = None
    rating: Optional[List[CodeableConcept]] = None


@dataclass
class EvidenceReferentGroup(BackboneElement):
    """ Group being referenced.
    """
    resource_type: ClassVar[str] = "EvidenceReferentGroup"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    evidenceSource: Optional[FHIRReference] = None
    intendedGroup: Optional[FHIRReference] = None
    directnessMatch: Optional[CodeableConcept] = None


@dataclass
class EvidenceVariableDefinition(BackboneElement):
    """ Evidence variable.
    """
    resource_type: ClassVar[str] = "EvidenceVariableDefinition"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    variableRole: Optional[CodeableConcept] = None
    actualDefinition: Optional[FHIRReference] = None
    intendedDefinition: Optional[FHIRReference] = None
    directnessMatch: Optional[CodeableConcept] = None


@dataclass
class EvidenceCertainty(BackboneElement):
    """ Level of certainty.
    """
    resource_type: ClassVar[str] = "EvidenceCertainty"

    description: Optional[str] = None
    note: Optional[Annotation] = None
    rating: Optional[List[CodeableConcept]] = None
    certaintySubcomponent: Optional[List[EvidenceCertaintyCertaintySubcomponent]] = None


@dataclass
class Evidence(DomainResource):
    """ Single evidence bit.

    This represents statistics, certainty, both the intended and actual
    population, and evidence variables.
    """
    resource_type: ClassVar[str] = "Evidence"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    useContext: Optional[List[UsageContext]] = None
    date: Optional[FHIRDate] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    contributor: Optional[List[Contributor]] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    description: Optional[str] = None
    assertion: Optional[str] = None
    note: Optional[List[Annotation]] = None
    referentGroup: EvidenceReferentGroup = None
    variableDefinition: Optional[List[EvidenceVariableDefinition]] = None
    synthesisType: Optional[CodeableConcept] = None
    studyType: Optional[CodeableConcept] = None
    statistic: Optional[List[Statistic]] = None
    distribution: Optional[List[OrderedDistribution]] = None
    certainty: Optional[List[EvidenceCertainty]] = None