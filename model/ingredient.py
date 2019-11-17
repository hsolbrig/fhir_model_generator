#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Ingredient) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .ratio import Ratio


@dataclass
class IngredientSpecifiedSubstanceStrengthReferenceStrength(BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    resource_type: ClassVar[str] = "IngredientSpecifiedSubstanceStrengthReferenceStrength"

    substanceCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='substance',))
    substanceReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='substance',))
    strength: Ratio = None
    strengthHighLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = None


@dataclass
class IngredientSpecifiedSubstanceStrength(BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "IngredientSpecifiedSubstanceStrength"

    presentation: Optional[Ratio] = None
    presentationHighLimit: Optional[Ratio] = None
    concentration: Optional[Ratio] = None
    concentrationHighLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = None
    referenceStrength: Optional[List[IngredientSpecifiedSubstanceStrengthReferenceStrength]] = None


@dataclass
class IngredientSpecifiedSubstance(BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "IngredientSpecifiedSubstance"

    codeCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='code',))
    codeReference: FHIRReference = field(default=None, metadata=dict(one_of_many='code',))
    group: CodeableConcept = None
    confidentiality: Optional[CodeableConcept] = None
    strength: Optional[List[IngredientSpecifiedSubstanceStrength]] = None


@dataclass
class IngredientSubstance(BackboneElement):
    """ The substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "IngredientSubstance"

    codeCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='code',))
    codeReference: FHIRReference = field(default=None, metadata=dict(one_of_many='code',))
    strength: Optional[List[IngredientSpecifiedSubstanceStrength]] = None


@dataclass
class Ingredient(DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "Ingredient"

    identifier: Optional[Identifier] = None
    role: CodeableConcept = None
    allergenicIndicator: Optional[bool] = None
    manufacturer: Optional[List[FHIRReference]] = None
    specifiedSubstance: Optional[List[IngredientSpecifiedSubstance]] = None
    substance: Optional[IngredientSubstance] = None