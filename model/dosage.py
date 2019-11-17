#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Dosage) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .element import Element
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing


@dataclass
class Dosage(Element):
    """ How the medication is/was taken or should be taken.

    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    resource_type: ClassVar[str] = "Dosage"

    sequence: Optional[int] = None
    text: Optional[str] = None
    additionalInstruction: Optional[List[CodeableConcept]] = None
    patientInstruction: Optional[str] = None
    timing: Optional[Timing] = None
    asNeededBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='asNeeded',))
    asNeededCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='asNeeded',))
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    doseRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='dose',))
    doseQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='dose',))
    maxDosePerPeriod: Optional[Ratio] = None
    maxDosePerAdministration: Optional[Quantity] = None
    maxDosePerLifetime: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='rate',))
    rateRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='rate',))
    rateQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='rate',))