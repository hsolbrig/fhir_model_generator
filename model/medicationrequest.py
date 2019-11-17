#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/MedicationRequest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity


@dataclass
class MedicationRequestRequester(BackboneElement):
    """ Who/What requested the Request.

    The individual, organization or device that initiated the request and has
    responsibility for its activation.
    """
    resource_type: ClassVar[str] = "MedicationRequestRequester"

    agent: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class MedicationRequestDispenseRequest(BackboneElement):
    """ Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequest"

    validityPeriod: Optional[Period] = None
    numberOfRepeatsAllowed: Optional[int] = None
    quantity: Optional[Quantity] = None
    expectedSupplyDuration: Optional[Duration] = None
    performer: Optional[FHIRReference] = None


@dataclass
class MedicationRequestSubstitution(BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """
    resource_type: ClassVar[str] = "MedicationRequestSubstitution"

    allowed: bool = None
    reason: Optional[CodeableConcept] = None


@dataclass
class MedicationRequest(DomainResource):
    """ Ordering of medication for patient or group.

    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """
    resource_type: ClassVar[str] = "MedicationRequest"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[List[FHIRReference]] = None
    basedOn: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: Optional[str] = None
    intent: str = None
    category: Optional[CodeableConcept] = None
    priority: Optional[str] = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = None
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[MedicationRequestRequester] = None
    recorder: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    dosageInstruction: Optional[List[Dosage]] = None
    dispenseRequest: Optional[MedicationRequestDispenseRequest] = None
    substitution: Optional[MedicationRequestSubstitution] = None
    priorPrescription: Optional[FHIRReference] = None
    detectedIssue: Optional[List[FHIRReference]] = None
    eventHistory: Optional[List[FHIRReference]] = None