#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Statistic) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .element import Element
from .quantity import Quantity
from .range import Range


@dataclass
class StatisticAttributeEstimateEstimateQualifier(Element):
    """ An estimate of the precision of the estimate.
    """
    resource_type: ClassVar[str] = "StatisticAttributeEstimateEstimateQualifier"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    level: Optional[float] = None
    range: Optional[Range] = None


@dataclass
class StatisticSampleSize(Element):
    """ Number of samples in the statistic.
    """
    resource_type: ClassVar[str] = "StatisticSampleSize"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    numberOfStudies: Optional[int] = None
    numberOfParticipants: Optional[int] = None
    knownDataCount: Optional[int] = None
    numeratorCount: Optional[int] = None


@dataclass
class StatisticAttributeEstimate(Element):
    """ An estimate of the precision of the statistic.
    """
    resource_type: ClassVar[str] = "StatisticAttributeEstimate"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    level: Optional[float] = None
    range: Optional[Range] = None
    estimateQualifier: Optional[List[StatisticAttributeEstimateEstimateQualifier]] = None


@dataclass
class Statistic(BackboneElement):
    """ Single statistic.

    A fact or piece of data from a  study of a large quantity of numerical
    data.  A mathematical or quantified characteristic of a group of
    observations.
    """
    resource_type: ClassVar[str] = "Statistic"

    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    statisticType: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    sampleSize: Optional[StatisticSampleSize] = None
    attributeEstimate: Optional[List[StatisticAttributeEstimate]] = None