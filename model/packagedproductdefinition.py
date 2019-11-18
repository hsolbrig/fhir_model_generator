#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition) on 2019-11-18.
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
from .marketingstatus import MarketingStatus
from .productshelflife import ProductShelfLife
from .quantity import Quantity


@dataclass
class PackagedProductDefinitionPackageCharacteristic(BackboneElement):
    """ General characteristics of this item.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinitionPackageCharacteristic"

    code: CodeableConcept = None
    valueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class PackagedProductDefinitionPackageContainedItem(BackboneElement):
    """ The item(s) within the packaging.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinitionPackageContainedItem"

    item: Optional[List[FHIRReference]] = None
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='amount',))


@dataclass
class PackagedProductDefinitionBatchIdentifier(BackboneElement):
    """ Batch numbering.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinitionBatchIdentifier"

    outerPackaging: Identifier = None
    immediatePackaging: Optional[Identifier] = None


@dataclass
class PackagedProductDefinitionPackage(BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinitionPackage"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    material: Optional[List[CodeableConcept]] = None
    alternateMaterial: Optional[List[CodeableConcept]] = None
    shelfLifeStorage: Optional[List[ProductShelfLife]] = None
    manufacturer: Optional[List[FHIRReference]] = None
    characteristic: Optional[List[PackagedProductDefinitionPackageCharacteristic]] = None
    containedItem: Optional[List[PackagedProductDefinitionPackageContainedItem]] = None
    package: Optional[List["PackagedProductDefinitionPackage"]] = None


@dataclass
class PackagedProductDefinition(DomainResource):
    """ A medicinal product in a container or package.
    """
    resource_type: ClassVar[str] = "PackagedProductDefinition"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[List[FHIRReference]] = None
    description: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    marketingStatus: Optional[List[MarketingStatus]] = None
    copackagedIndicator: Optional[bool] = None
    marketingAuthorization: Optional[FHIRReference] = None
    manufacturer: Optional[List[FHIRReference]] = None
    batchIdentifier: Optional[List[PackagedProductDefinitionBatchIdentifier]] = None
    package: Optional[List[PackagedProductDefinitionPackage]] = None