#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2019-11-17.
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
class VisionPrescriptionDispense(BackboneElement):
    """ Vision supply authorization.

    Deals with details of the dispense part of the supply specification.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionDispense"

    product: Optional[CodeableConcept] = None
    eye: Optional[str] = None
    sphere: Optional[float] = None
    cylinder: Optional[float] = None
    axis: Optional[int] = None
    prism: Optional[float] = None
    base: Optional[str] = None
    add: Optional[float] = None
    power: Optional[float] = None
    backCurve: Optional[float] = None
    diameter: Optional[float] = None
    duration: Optional[Quantity] = None
    color: Optional[str] = None
    brand: Optional[str] = None
    note: Optional[List[Annotation]] = None


@dataclass
class VisionPrescription(DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """
    resource_type: ClassVar[str] = "VisionPrescription"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    patient: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    dateWritten: Optional[FHIRDate] = None
    prescriber: Optional[FHIRReference] = None
    reasonCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='reason',))
    reasonReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='reason',))
    dispense: Optional[List[VisionPrescriptionDispense]] = None