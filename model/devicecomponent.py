#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DeviceComponent) on 2019-11-17.
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
class DeviceComponentProductionSpecification(BackboneElement):
    """ Specification details such as Component Revisions, or Serial Numbers.

    The production specification such as component revision, serial number,
    etc.
    """
    resource_type: ClassVar[str] = "DeviceComponentProductionSpecification"

    specType: Optional[CodeableConcept] = None
    componentId: Optional[Identifier] = None
    productionSpec: Optional[str] = None


@dataclass
class DeviceComponent(DomainResource):
    """ An instance of a medical-related component of a medical device.

    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    resource_type: ClassVar[str] = "DeviceComponent"

    identifier: Identifier = None
    type: CodeableConcept = None
    lastSystemChange: Optional[FHIRDate] = None
    source: Optional[FHIRReference] = None
    parent: Optional[FHIRReference] = None
    operationalStatus: Optional[List[CodeableConcept]] = None
    parameterGroup: Optional[CodeableConcept] = None
    measurementPrinciple: Optional[str] = None
    productionSpecification: Optional[List[DeviceComponentProductionSpecification]] = None
    languageCode: Optional[CodeableConcept] = None