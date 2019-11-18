#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/SubstanceDefinition) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class SubstanceDefinitionNameOfficial(BackboneElement):
    """ Details of the official nature of this name.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionNameOfficial"

    authority: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None


@dataclass
class SubstanceDefinitionStructureIsotopeMolecularWeight(BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureIsotopeMolecularWeight"

    method: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None


@dataclass
class SubstanceDefinitionStructureIsotope(BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureIsotope"

    identifier: Optional[Identifier] = None
    name: Optional[CodeableConcept] = None
    substitution: Optional[CodeableConcept] = None
    halfLife: Optional[Quantity] = None
    molecularWeight: Optional[SubstanceDefinitionStructureIsotopeMolecularWeight] = None


@dataclass
class SubstanceDefinitionStructureRepresentation(BackboneElement):
    """ Molecular structural representation.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureRepresentation"

    type: Optional[CodeableConcept] = None
    representation: Optional[str] = None
    attachment: Optional[Attachment] = None


@dataclass
class SubstanceDefinitionMoiety(BackboneElement):
    """ Moiety, for structural modifications.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionMoiety"

    role: Optional[CodeableConcept] = None
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    stereochemistry: Optional[CodeableConcept] = None
    opticalActivity: Optional[CodeableConcept] = None
    molecularFormula: Optional[str] = None
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))
    amountType: Optional[CodeableConcept] = None


@dataclass
class SubstanceDefinitionProperty(BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionProperty"

    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    parameters: Optional[str] = None
    definingSubstanceReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='definingSubstance',))
    definingSubstanceCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='definingSubstance',))
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))
    referenceRange: Optional[Range] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceDefinitionStructure(BackboneElement):
    """ Structural information.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructure"

    stereochemistry: Optional[CodeableConcept] = None
    opticalActivity: Optional[CodeableConcept] = None
    molecularFormula: Optional[str] = None
    molecularFormulaByMoiety: Optional[str] = None
    isotope: Optional[List[SubstanceDefinitionStructureIsotope]] = None
    molecularWeight: Optional[SubstanceDefinitionStructureIsotopeMolecularWeight] = None
    sourceCoding: Optional[List[Coding]] = None
    sourceDocument: Optional[List[FHIRReference]] = None
    representation: Optional[List[SubstanceDefinitionStructureRepresentation]] = None


@dataclass
class SubstanceDefinitionstr(BackboneElement):
    """ Codes associated with the substance.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionstr"

    code: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    note: Optional[List[Annotation]] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceDefinitionName(BackboneElement):
    """ Names applicable to this substance.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionName"

    name: str = None
    type: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    preferred: Optional[bool] = None
    language: Optional[List[CodeableConcept]] = None
    domain: Optional[List[CodeableConcept]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    synonym: Optional[List["SubstanceDefinitionName"]] = None
    translation: Optional[List["SubstanceDefinitionName"]] = None
    official: Optional[List[SubstanceDefinitionNameOfficial]] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceDefinitionRelationship(BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionRelationship"

    substanceDefinitionReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='substanceDefinition',))
    substanceDefinitionCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='substanceDefinition',))
    type: Optional[CodeableConcept] = None
    isDefining: Optional[bool] = None
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRatioHighLimit: Optional[Ratio] = None
    amountType: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceDefinition(DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    resource_type: ClassVar[str] = "SubstanceDefinition"

    identifier: Optional[Identifier] = None
    status: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    domain: Optional[CodeableConcept] = None
    description: Optional[str] = None
    source: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    manufacturer: Optional[List[FHIRReference]] = None
    supplier: Optional[List[FHIRReference]] = None
    moiety: Optional[List[SubstanceDefinitionMoiety]] = None
    property: Optional[List[SubstanceDefinitionProperty]] = None
    referenceInformation: Optional[FHIRReference] = None
    structure: Optional[SubstanceDefinitionStructure] = None
    code: Optional[List[SubstanceDefinitionstr]] = None
    name: Optional[List[SubstanceDefinitionName]] = None
    molecularWeight: Optional[List[SubstanceDefinitionStructureIsotopeMolecularWeight]] = None
    relationship: Optional[List[SubstanceDefinitionRelationship]] = None
    nucleicAcid: Optional[FHIRReference] = None
    polymer: Optional[FHIRReference] = None
    protein: Optional[FHIRReference] = None
    sourceMaterial: Optional[FHIRReference] = None