#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod"

    tissue: CodeableConcept = None
    value: Quantity = None
    supportingInformation: Optional[str] = None


@dataclass
class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies"

    code: CodeableConcept = None
    withdrawalPeriod: Optional[List[AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = None


@dataclass
class AdministrableProductDefinitionCharacteristic(BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionCharacteristic"

    code: CodeableConcept = None
    valueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    status: Optional[CodeableConcept] = None


@dataclass
class AdministrableProductDefinitionRouteOfAdministration(BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionRouteOfAdministration"

    code: CodeableConcept = None
    firstDose: Optional[Quantity] = None
    maxSingleDose: Optional[Quantity] = None
    maxDosePerDay: Optional[Quantity] = None
    maxDosePerTreatmentPeriod: Optional[Ratio] = None
    maxTreatmentPeriod: Optional[Duration] = None
    targetSpecies: Optional[List[AdministrableProductDefinitionRouteOfAdministrationTargetSpecies]] = None


@dataclass
class AdministrableProductDefinition(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinition"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[List[FHIRReference]] = None
    administrableDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    producedFrom: Optional[List[FHIRReference]] = None
    ingredient: Optional[List[FHIRReference]] = None
    device: Optional[List[FHIRReference]] = None
    characteristic: Optional[List[AdministrableProductDefinitionCharacteristic]] = None
    routeOfAdministration: List[AdministrableProductDefinitionRouteOfAdministration] = field(default_factory=list)