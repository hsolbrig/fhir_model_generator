#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Medication) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationPackageContent(BackboneElement):
    """ What is  in the package.

    A set of components that go to make up the described item.
    """
    resource_type: ClassVar[str] = "MedicationPackageContent"

    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    amount: Optional[Quantity] = None


@dataclass
class MedicationPackageBatch(BackboneElement):
    """ Identifies a single production run.

    Information about a group of medication produced or packaged from one
    production run.
    """
    resource_type: ClassVar[str] = "MedicationPackageBatch"

    lotNumber: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None


@dataclass
class MedicationIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationIngredient"

    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    isActive: Optional[bool] = None
    amount: Optional[Ratio] = None


@dataclass
class MedicationPackage(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationPackage"

    container: Optional[CodeableConcept] = None
    content: Optional[List[MedicationPackageContent]] = None
    batch: Optional[List[MedicationPackageBatch]] = None


@dataclass
class Medication(DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """
    resource_type: ClassVar[str] = "Medication"

    code: Optional[CodeableConcept] = None
    status: Optional[str] = None
    isBrand: Optional[bool] = None
    isOverTheCounter: Optional[bool] = None
    manufacturer: Optional[FHIRReference] = None
    form: Optional[CodeableConcept] = None
    ingredient: Optional[List[MedicationIngredient]] = None
    package: Optional[MedicationPackage] = None
    image: Optional[List[Attachment]] = None