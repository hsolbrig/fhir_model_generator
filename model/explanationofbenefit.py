#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class ExplanationOfBenefitBenefitBalanceFinancial(BackboneElement):
    """ Benefit Summary.

    Benefits Used to date.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalanceFinancial"

    type: CodeableConcept = None
    allowedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedString: Optional[str] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='allowed',))
    usedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='used',))
    usedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='used',))


@dataclass
class ExplanationOfBenefitAddItemDetail(BackboneElement):
    """ Added items details.

    The second tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetail"

    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    fee: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = None


@dataclass
class ExplanationOfBenefitItemDetailSubDetail(BackboneElement):
    """ Additional items.

    Third tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetailSubDetail"

    sequence: int = None
    type: CodeableConcept = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    programCode: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = None


@dataclass
class ExplanationOfBenefitItemAdjudication(BackboneElement):
    """ Adjudication details.

    The adjudications results.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemAdjudication"

    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    value: Optional[float] = None


@dataclass
class ExplanationOfBenefitItemDetail(BackboneElement):
    """ Additional items.

    Second tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetail"

    sequence: int = None
    type: CodeableConcept = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    programCode: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    subDetail: Optional[List[ExplanationOfBenefitItemDetailSubDetail]] = None


@dataclass
class ExplanationOfBenefitRelated(BackboneElement):
    """ Related Claims which may be revelant to processing this claim.

    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitRelated"

    claim: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    reference: Optional[Identifier] = None


@dataclass
class ExplanationOfBenefitPayee(BackboneElement):
    """ Party to be paid any benefits payable.

    The party to be reimbursed for the services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayee"

    type: Optional[CodeableConcept] = None
    resourceType: Optional[CodeableConcept] = None
    party: Optional[FHIRReference] = None


@dataclass
class ExplanationOfBenefitInformation(BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitInformation"

    sequence: int = None
    category: CodeableConcept = None
    code: Optional[CodeableConcept] = None
    timingDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='value',))
    reason: Optional[Coding] = None


@dataclass
class ExplanationOfBenefitCareTeam(BackboneElement):
    """ Care Team members.

    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitCareTeam"

    sequence: int = None
    provider: FHIRReference = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    qualification: Optional[CodeableConcept] = None


@dataclass
class ExplanationOfBenefitDiagnosis(BackboneElement):
    """ List of Diagnosis.

    Ordered list of patient diagnosis for which care is sought.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitDiagnosis"

    sequence: int = None
    diagnosisCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='diagnosis',))
    diagnosisReference: FHIRReference = field(default=None, metadata=dict(one_of_many='diagnosis',))
    type: Optional[List[CodeableConcept]] = None
    packageCode: Optional[CodeableConcept] = None


@dataclass
class ExplanationOfBenefitProcedure(BackboneElement):
    """ Procedures performed.

    Ordered list of patient procedures performed to support the adjudication.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcedure"

    sequence: int = None
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='procedure',))
    procedureReference: FHIRReference = field(default=None, metadata=dict(one_of_many='procedure',))


@dataclass
class ExplanationOfBenefitInsurance(BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitInsurance"

    coverage: Optional[FHIRReference] = None
    preAuthRef: Optional[List[str]] = None


@dataclass
class ExplanationOfBenefitAccident(BackboneElement):
    """ Details of an accident.

    An accident which resulted in the need for healthcare services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAccident"

    date: Optional[FHIRDate] = None
    type: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='location',))
    locationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='location',))


@dataclass
class ExplanationOfBenefitItem(BackboneElement):
    """ Goods and Services.

    First tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItem"

    sequence: int = None
    careTeamLinkId: Optional[List[int]] = None
    diagnosisLinkId: Optional[List[int]] = None
    procedureLinkId: Optional[List[int]] = None
    informationLinkId: Optional[List[int]] = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    programCode: Optional[List[CodeableConcept]] = None
    servicedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='serviced',))
    servicedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='serviced',))
    locationCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='location',))
    locationAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='location',))
    locationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='location',))
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = None
    bodySite: Optional[CodeableConcept] = None
    subSite: Optional[List[CodeableConcept]] = None
    encounter: Optional[List[FHIRReference]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    detail: Optional[List[ExplanationOfBenefitItemDetail]] = None


@dataclass
class ExplanationOfBenefitAddItem(BackboneElement):
    """ Insurer added line items.

    The first tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItem"

    sequenceLinkId: Optional[List[int]] = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    fee: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    detail: Optional[List[ExplanationOfBenefitAddItemDetail]] = None


@dataclass
class ExplanationOfBenefitPayment(BackboneElement):
    """ Payment (if paid).

    Payment details for the claim if the claim has been paid.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayment"

    type: Optional[CodeableConcept] = None
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    amount: Optional[Money] = None
    identifier: Optional[Identifier] = None


@dataclass
class ExplanationOfBenefitProcessNote(BackboneElement):
    """ Processing notes.

    Note text.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcessNote"

    number: Optional[int] = None
    type: Optional[CodeableConcept] = None
    text: Optional[str] = None
    language: Optional[CodeableConcept] = None


@dataclass
class ExplanationOfBenefitBenefitBalance(BackboneElement):
    """ Balance by Benefit Category.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalance"

    category: CodeableConcept = None
    subCategory: Optional[CodeableConcept] = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    financial: Optional[List[ExplanationOfBenefitBenefitBalanceFinancial]] = None


@dataclass
class ExplanationOfBenefit(DomainResource):
    """ Explanation of Benefit resource.

    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefit"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subType: Optional[List[CodeableConcept]] = None
    patient: Optional[FHIRReference] = None
    billablePeriod: Optional[Period] = None
    created: Optional[FHIRDate] = None
    enterer: Optional[FHIRReference] = None
    insurer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    referral: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    claim: Optional[FHIRReference] = None
    claimResponse: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    disposition: Optional[str] = None
    related: Optional[List[ExplanationOfBenefitRelated]] = None
    prescription: Optional[FHIRReference] = None
    originalPrescription: Optional[FHIRReference] = None
    payee: Optional[ExplanationOfBenefitPayee] = None
    information: Optional[List[ExplanationOfBenefitInformation]] = None
    careTeam: Optional[List[ExplanationOfBenefitCareTeam]] = None
    diagnosis: Optional[List[ExplanationOfBenefitDiagnosis]] = None
    procedure: Optional[List[ExplanationOfBenefitProcedure]] = None
    precedence: Optional[int] = None
    insurance: Optional[ExplanationOfBenefitInsurance] = None
    accident: Optional[ExplanationOfBenefitAccident] = None
    employmentImpacted: Optional[Period] = None
    hospitalization: Optional[Period] = None
    item: Optional[List[ExplanationOfBenefitItem]] = None
    addItem: Optional[List[ExplanationOfBenefitAddItem]] = None
    totalCost: Optional[Money] = None
    unallocDeductable: Optional[Money] = None
    totalBenefit: Optional[Money] = None
    payment: Optional[ExplanationOfBenefitPayment] = None
    form: Optional[CodeableConcept] = None
    processNote: Optional[List[ExplanationOfBenefitProcessNote]] = None
    benefitBalance: Optional[List[ExplanationOfBenefitBenefitBalance]] = None