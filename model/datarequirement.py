#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .coding import Coding
from .duration import Duration
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class DataRequirementCodeFilter(Element):
    """ What codes are expected.

    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data.
    """
    resource_type: ClassVar[str] = "DataRequirementCodeFilter"

    path: str = None
    valueSetString: Optional[str] = field(default=None, metadata=dict(one_of_many='valueSet',))
    valueSetReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='valueSet',))
    valueCode: Optional[List[str]] = None
    valueCoding: Optional[List[Coding]] = None
    valueCodeableConcept: Optional[List[CodeableConcept]] = None


@dataclass
class DataRequirementDateFilter(Element):
    """ What dates/date ranges are expected.

    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements.
    """
    resource_type: ClassVar[str] = "DataRequirementDateFilter"

    path: str = None
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class DataRequirement(Element):
    """ Describes a required data item.

    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    resource_type: ClassVar[str] = "DataRequirement"

    type: str = None
    profile: Optional[List[str]] = None
    mustSupport: Optional[List[str]] = None
    codeFilter: Optional[List[DataRequirementCodeFilter]] = None
    dateFilter: Optional[List[DataRequirementDateFilter]] = None