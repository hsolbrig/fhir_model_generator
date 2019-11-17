#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Measure) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .contributor import Contributor
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class MeasureGroupPopulation(BackboneElement):
    """ Population criteria.

    A population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroupPopulation"

    identifier: Optional[Identifier] = None
    code: Optional[CodeableConcept] = None
    name: Optional[str] = None
    description: Optional[str] = None
    criteria: str = None


@dataclass
class MeasureGroupStratifier(BackboneElement):
    """ Stratifier criteria for the measure.

    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library, or a
    valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifier"

    identifier: Optional[Identifier] = None
    criteria: Optional[str] = None
    path: Optional[str] = None


@dataclass
class MeasureGroup(BackboneElement):
    """ Population criteria group.

    A group of population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroup"

    identifier: Identifier = None
    name: Optional[str] = None
    description: Optional[str] = None
    population: Optional[List[MeasureGroupPopulation]] = None
    stratifier: Optional[List[MeasureGroupStratifier]] = None


@dataclass
class MeasureSupplementalData(BackboneElement):
    """ What other data should be reported with the measure.

    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureSupplementalData"

    identifier: Optional[Identifier] = None
    usage: Optional[List[CodeableConcept]] = None
    criteria: Optional[str] = None
    path: Optional[str] = None


@dataclass
class Measure(DomainResource):
    """ A quality measure definition.

    The Measure resource provides the definition of a quality measure.
    """
    resource_type: ClassVar[str] = "Measure"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    description: Optional[str] = None
    purpose: Optional[str] = None
    usage: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    topic: Optional[List[CodeableConcept]] = None
    contributor: Optional[List[Contributor]] = None
    contact: Optional[List[ContactDetail]] = None
    copyright: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    library: Optional[List[FHIRReference]] = None
    disclaimer: Optional[str] = None
    scoring: Optional[CodeableConcept] = None
    compositeScoring: Optional[CodeableConcept] = None
    type: Optional[List[CodeableConcept]] = None
    riskAdjustment: Optional[str] = None
    rateAggregation: Optional[str] = None
    rationale: Optional[str] = None
    clinicalRecommendationStatement: Optional[str] = None
    improvementNotation: Optional[str] = None
    definition: Optional[List[str]] = None
    guidance: Optional[str] = None
    set: Optional[str] = None
    group: Optional[List[MeasureGroup]] = None
    supplementalData: Optional[List[MeasureSupplementalData]] = None