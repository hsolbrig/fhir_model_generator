#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2019-11-17.
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
class MeasureReportGroupStratifierStratumPopulation(BackboneElement):
    """ Population results in this stratum.

    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumPopulation"

    identifier: Optional[Identifier] = None
    code: Optional[CodeableConcept] = None
    count: Optional[int] = None
    patients: Optional[FHIRReference] = None


@dataclass
class MeasureReportGroupStratifierStratum(BackboneElement):
    """ Stratum results, one for each unique value in the stratifier.

    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratum"

    value: str = None
    population: Optional[List[MeasureReportGroupStratifierStratumPopulation]] = None
    measureScore: Optional[float] = None


@dataclass
class MeasureReportGroupPopulation(BackboneElement):
    """ The populations in the group.

    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupPopulation"

    identifier: Optional[Identifier] = None
    code: Optional[CodeableConcept] = None
    count: Optional[int] = None
    patients: Optional[FHIRReference] = None


@dataclass
class MeasureReportGroupStratifier(BackboneElement):
    """ Stratification results.

    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifier"

    identifier: Optional[Identifier] = None
    stratum: Optional[List[MeasureReportGroupStratifierStratum]] = None


@dataclass
class MeasureReportGroup(BackboneElement):
    """ Measure results for each group.

    The results of the calculation, one for each population group in the
    measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroup"

    identifier: Identifier = None
    population: Optional[List[MeasureReportGroupPopulation]] = None
    measureScore: Optional[float] = None
    stratifier: Optional[List[MeasureReportGroupStratifier]] = None


@dataclass
class MeasureReport(DomainResource):
    """ Results of a measure evaluation.

    The MeasureReport resource contains the results of evaluating a measure.
    """
    resource_type: ClassVar[str] = "MeasureReport"

    identifier: Optional[Identifier] = None
    status: str = None
    type: str = None
    measure: FHIRReference = None
    patient: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    reportingOrganization: Optional[FHIRReference] = None
    period: Period = None
    group: Optional[List[MeasureReportGroup]] = None
    evaluatedResources: Optional[FHIRReference] = None