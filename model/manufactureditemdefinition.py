#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class ManufacturedItemDefinitionCharacteristic(BackboneElement):
    """ General characteristics of this item.
    """
    resource_type: ClassVar[str] = "ManufacturedItemDefinitionCharacteristic"

    code: CodeableConcept = None
    valueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class ManufacturedItemDefinition(DomainResource):
    """ The definition and characteristics of a medicinal manufactured item, such
    as a tablet or capsule, as contained in a packaged medicinal product.
    """
    resource_type: ClassVar[str] = "ManufacturedItemDefinition"

    identifier: Optional[List[Identifier]] = None
    manufacturedDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    manufacturer: Optional[List[FHIRReference]] = None
    ingredient: Optional[List[FHIRReference]] = None
    characteristic: Optional[List[ManufacturedItemDefinitionCharacteristic]] = None