#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus
from .period import Period


@dataclass
class MedicinalProductDefinitionNameNamePart(BackboneElement):
    """ Coding words or phrases of the name.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionNameNamePart"

    part: str = None
    type: Coding = None


@dataclass
class MedicinalProductDefinitionNameCountryLanguage(BackboneElement):
    """ Country where the name applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionNameCountryLanguage"

    country: CodeableConcept = None
    jurisdiction: Optional[CodeableConcept] = None
    language: CodeableConcept = None


@dataclass
class MedicinalProductDefinitionContact(BackboneElement):
    """ A product specific contact, person (in a role), or an organization.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionContact"

    type: Optional[CodeableConcept] = None
    contact: FHIRReference = None


@dataclass
class MedicinalProductDefinitionName(BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionName"

    productName: str = None
    type: Optional[Coding] = None
    namePart: Optional[List[MedicinalProductDefinitionNameNamePart]] = None
    countryLanguage: Optional[List[MedicinalProductDefinitionNameCountryLanguage]] = None


@dataclass
class MedicinalProductDefinitionCrossReference(BackboneElement):
    """ Reference to another product, e.g. for linking authorised to
    investigational product.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionCrossReference"

    productIdentifier: Identifier = field(default=None, metadata=dict(one_of_many='product',))
    productReference: FHIRReference = field(default=None, metadata=dict(one_of_many='product',))
    type: Optional[Coding] = None


@dataclass
class MedicinalProductDefinitionManufacturingBusinessOperation(BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionManufacturingBusinessOperation"

    operationType: Optional[CodeableConcept] = None
    authorisationReferenceNumber: Optional[Identifier] = None
    effectiveDate: Optional[Period] = None
    confidentialityIndicator: Optional[CodeableConcept] = None
    manufacturer: Optional[List[FHIRReference]] = None
    regulator: Optional[FHIRReference] = None


@dataclass
class MedicinalProductDefinition(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinition"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    domain: Optional[Coding] = None
    description: Optional[str] = None
    combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
    indication: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    additionalMonitoringIndicator: Optional[CodeableConcept] = None
    specialMeasures: Optional[List[CodeableConcept]] = None
    paediatricUseIndicator: Optional[CodeableConcept] = None
    productClassification: Optional[List[CodeableConcept]] = None
    marketingStatus: Optional[List[MarketingStatus]] = None
    pharmaceuticalProduct: Optional[List[FHIRReference]] = None
    packagedMedicinalProduct: Optional[List[FHIRReference]] = None
    ingredient: Optional[List[FHIRReference]] = None
    attachedDocument: Optional[List[FHIRReference]] = None
    masterFile: Optional[List[FHIRReference]] = None
    contact: Optional[List[MedicinalProductDefinitionContact]] = None
    clinicalTrial: Optional[List[FHIRReference]] = None
    name: List[MedicinalProductDefinitionName] = field(default_factory=list)
    crossReference: Optional[List[MedicinalProductDefinitionCrossReference]] = None
    manufacturingBusinessOperation: Optional[List[MedicinalProductDefinitionManufacturingBusinessOperation]] = None