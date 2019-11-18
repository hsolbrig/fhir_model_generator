#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/NutritionIntake) on 2019-11-18.
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
from .period import Period
from .quantity import Quantity
from .timing import Timing


@dataclass
class NutritionIntakeConsumedItem(BackboneElement):
    """ What food or fluid product or item was consumed.
    """
    resource_type: ClassVar[str] = "NutritionIntakeConsumedItem"

    type: CodeableConcept = None
    nutritionProduct: CodeableConcept = None
    schedule: Optional[Timing] = None
    amount: Optional[Quantity] = None
    rate: Optional[Quantity] = None
    notConsumed: Optional[bool] = None
    notConsumedReason: Optional[CodeableConcept] = None


@dataclass
class NutritionIntakeIngredientLabel(BackboneElement):
    """ Total nutrient for the whole meal, product, serving.

    Total nutrient amounts for the whole meal, product, serving, etc.
    """
    resource_type: ClassVar[str] = "NutritionIntakeIngredientLabel"

    nutrient: CodeableConcept = None
    amount: Quantity = None


@dataclass
class NutritionIntake(DomainResource):
    """ Record of food or fluid being taken by a patient.

    A record of food or fluid that is being consumed by a patient.   A
    NutritionIntake may indicate that the patient may be consuming the food or
    fluid now or has consumed the food or fluid in the past.  The source of
    this information can be the patient, significant other (such as a family
    member or spouse), or a clinician.  A common scenario where this
    information is captured is during the history taking process during a
    patient visit or stay or through an app that tracks food or fluids
    consumed.   The consumption information may come from sources such as the
    patient's memory, from a nutrition label,  or from a clinician documenting
    observed intake.
    """
    resource_type: ClassVar[str] = "NutritionIntake"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    statusReason: Optional[List[CodeableConcept]] = None
    category: Optional[List[CodeableConcept]] = None
    consumedItem: List[NutritionIntakeConsumedItem] = field(default_factory=list)
    ingredientLabel: Optional[List[NutritionIntakeIngredientLabel]] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='effective',))
    effectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='effective',))
    dateAsserted: Optional[FHIRDate] = None
    informationSource: Optional[FHIRReference] = None
    derivedFrom: Optional[List[FHIRReference]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None