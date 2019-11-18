#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/MedicationKnowledge) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationKnowledgeRegulatorySubstitution(BackboneElement):
    """ Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySubstitution"

    type: CodeableConcept = None
    allowed: bool = None


@dataclass
class MedicationKnowledgeRegulatoryMaxDispense(BackboneElement):
    """ The maximum number of units of the medication that can be dispensed in a
    period.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatoryMaxDispense"

    quantity: Quantity = None
    period: Optional[Duration] = None


@dataclass
class MedicationKnowledgeAdministrationGuidelineDosage(BackboneElement):
    """ Dosage for the medication for the specific guidelines.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelineDosage"

    type: CodeableConcept = None
    dosage: List[Dosage] = field(default_factory=list)


@dataclass
class MedicationKnowledgeAdministrationGuidelinePatientCharacteristic(BackboneElement):
    """ Characteristics of the patient that are relevant to the administration
    guidelines.

    Characteristics of the patient that are relevant to the administration
    guidelines (for example, height, weight, gender, etc.).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelinePatientCharacteristic"

    characteristicCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='characteristic',))
    characteristicQuantity: Quantity = field(default=None, metadata=dict(one_of_many='characteristic',))
    value: Optional[List[str]] = None


@dataclass
class MedicationKnowledgeRelatedMedicationKnowledge(BackboneElement):
    """ Associated or related medication information.

    Associated or related knowledge about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRelatedMedicationKnowledge"

    type: CodeableConcept = None
    reference: List[FHIRReference] = field(default_factory=list)


@dataclass
class MedicationKnowledgeMonograph(BackboneElement):
    """ Associated documentation about the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonograph"

    type: Optional[CodeableConcept] = None
    source: Optional[FHIRReference] = None


@dataclass
class MedicationKnowledgeIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeIngredient"

    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    isActive: Optional[bool] = None
    strength: Optional[Ratio] = None


@dataclass
class MedicationKnowledgeCost(BackboneElement):
    """ The pricing of the medication.

    The price of the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeCost"

    type: CodeableConcept = None
    source: Optional[str] = None
    cost: Money = None


@dataclass
class MedicationKnowledgeMonitoringProgram(BackboneElement):
    """ Program under which a medication is reviewed.

    The program under which the medication is reviewed.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonitoringProgram"

    type: Optional[CodeableConcept] = None
    name: Optional[str] = None


@dataclass
class MedicationKnowledgeAdministrationGuideline(BackboneElement):
    """ Guidelines or protocols for administration of the medication.

    Guidelines or protocols that are applicable for the administration of the
    medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuideline"

    dosage: Optional[List[MedicationKnowledgeAdministrationGuidelineDosage]] = None
    indicationCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='indication',))
    indicationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='indication',))
    patientCharacteristic: Optional[List[MedicationKnowledgeAdministrationGuidelinePatientCharacteristic]] = None


@dataclass
class MedicationKnowledgeMedicineClassification(BackboneElement):
    """ Categorization of the medication within a formulary or classification
    system.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMedicineClassification"

    type: CodeableConcept = None
    classification: Optional[List[CodeableConcept]] = None


@dataclass
class MedicationKnowledgePackaging(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgePackaging"

    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    device: Optional[FHIRReference] = None
    material: Optional[CodeableConcept] = None
    packaging: Optional[List["MedicationKnowledgePackaging"]] = None


@dataclass
class MedicationKnowledgeDrugCharacteristic(BackboneElement):
    """ Specifies descriptive properties of the medicine.

    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeDrugCharacteristic"

    type: Optional[CodeableConcept] = None
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueBase64Binary: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class MedicationKnowledgeRegulatory(BackboneElement):
    """ Regulatory information about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatory"

    regulatoryAuthority: FHIRReference = None
    substitution: Optional[List[MedicationKnowledgeRegulatorySubstitution]] = None
    schedule: Optional[List[CodeableConcept]] = None
    maxDispense: Optional[MedicationKnowledgeRegulatoryMaxDispense] = None


@dataclass
class MedicationKnowledgeKineticCharacteristic(BackboneElement):
    """ The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeKineticCharacteristic"

    type: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class MedicationKnowledge(DomainResource):
    """ Definition of Medication Knowledge.

    Information about a medication that is used to support knowledge.
    """
    resource_type: ClassVar[str] = "MedicationKnowledge"

    identifier: Optional[List[Identifier]] = None
    code: Optional[CodeableConcept] = None
    status: Optional[str] = None
    manufacturer: Optional[FHIRReference] = None
    doseForm: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None
    synonym: Optional[List[str]] = None
    relatedMedicationKnowledge: Optional[List[MedicationKnowledgeRelatedMedicationKnowledge]] = None
    associatedMedication: Optional[List[FHIRReference]] = None
    productType: Optional[List[CodeableConcept]] = None
    monograph: Optional[List[MedicationKnowledgeMonograph]] = None
    ingredient: Optional[List[MedicationKnowledgeIngredient]] = None
    device: Optional[List[FHIRReference]] = None
    preparationInstruction: Optional[str] = None
    intendedRoute: Optional[List[CodeableConcept]] = None
    cost: Optional[List[MedicationKnowledgeCost]] = None
    monitoringProgram: Optional[List[MedicationKnowledgeMonitoringProgram]] = None
    administrationGuideline: Optional[List[MedicationKnowledgeAdministrationGuideline]] = None
    medicineClassification: Optional[List[MedicationKnowledgeMedicineClassification]] = None
    packaging: Optional[MedicationKnowledgePackaging] = None
    drugCharacteristic: Optional[List[MedicationKnowledgeDrugCharacteristic]] = None
    clinicalUseIssue: Optional[List[FHIRReference]] = None
    regulatory: Optional[List[MedicationKnowledgeRegulatory]] = None
    kineticCharacteristic: Optional[List[MedicationKnowledgeKineticCharacteristic]] = None