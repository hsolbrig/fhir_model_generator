#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Claim) on 2019-11-17.
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
class ClaimItemDetailSubDetail(BackboneElement):
    """ Additional items.

    Third tier of goods and services.
    """
    resource_type: ClassVar[str] = "ClaimItemDetailSubDetail"

    sequence: int = None
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


@dataclass
class ClaimItemDetail(BackboneElement):
    """ Additional items.

    Second tier of goods and services.
    """
    resource_type: ClassVar[str] = "ClaimItemDetail"

    sequence: int = None
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
    subDetail: Optional[List[ClaimItemDetailSubDetail]] = None


@dataclass
class ClaimRelated(BackboneElement):
    """ Related Claims which may be revelant to processing this claimn.

    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    resource_type: ClassVar[str] = "ClaimRelated"

    claim: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    reference: Optional[Identifier] = None


@dataclass
class ClaimPayee(BackboneElement):
    """ Party to be paid any benefits payable.

    The party to be reimbursed for the services.
    """
    resource_type: ClassVar[str] = "ClaimPayee"

    type: CodeableConcept = None
    resourceType: Optional[Coding] = None
    party: Optional[FHIRReference] = None


@dataclass
class ClaimCareTeam(BackboneElement):
    """ Members of the care team.

    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """
    resource_type: ClassVar[str] = "ClaimCareTeam"

    sequence: int = None
    provider: FHIRReference = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    qualification: Optional[CodeableConcept] = None


@dataclass
class ClaimInformation(BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """
    resource_type: ClassVar[str] = "ClaimInformation"

    sequence: int = None
    category: CodeableConcept = None
    code: Optional[CodeableConcept] = None
    timingDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='value',))
    reason: Optional[CodeableConcept] = None


@dataclass
class ClaimDiagnosis(BackboneElement):
    """ List of Diagnosis.

    List of patient diagnosis for which care is sought.
    """
    resource_type: ClassVar[str] = "ClaimDiagnosis"

    sequence: int = None
    diagnosisCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='diagnosis',))
    diagnosisReference: FHIRReference = field(default=None, metadata=dict(one_of_many='diagnosis',))
    type: Optional[List[CodeableConcept]] = None
    packageCode: Optional[CodeableConcept] = None


@dataclass
class ClaimProcedure(BackboneElement):
    """ Procedures performed.

    Ordered list of patient procedures performed to support the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimProcedure"

    sequence: int = None
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='procedure',))
    procedureReference: FHIRReference = field(default=None, metadata=dict(one_of_many='procedure',))


@dataclass
class ClaimInsurance(BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """
    resource_type: ClassVar[str] = "ClaimInsurance"

    sequence: int = None
    focal: bool = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None
    preAuthRef: Optional[List[str]] = None
    claimResponse: Optional[FHIRReference] = None


@dataclass
class ClaimAccident(BackboneElement):
    """ Details about an accident.

    An accident which resulted in the need for healthcare services.
    """
    resource_type: ClassVar[str] = "ClaimAccident"

    date: FHIRDate = None
    type: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='location',))
    locationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='location',))


@dataclass
class ClaimItem(BackboneElement):
    """ Goods and Services.

    First tier of goods and services.
    """
    resource_type: ClassVar[str] = "ClaimItem"

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
    detail: Optional[List[ClaimItemDetail]] = None


@dataclass
class Claim(DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    resource_type: ClassVar[str] = "Claim"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subType: Optional[List[CodeableConcept]] = None
    use: Optional[str] = None
    patient: Optional[FHIRReference] = None
    billablePeriod: Optional[Period] = None
    created: Optional[FHIRDate] = None
    enterer: Optional[FHIRReference] = None
    insurer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    priority: Optional[CodeableConcept] = None
    fundsReserve: Optional[CodeableConcept] = None
    related: Optional[List[ClaimRelated]] = None
    prescription: Optional[FHIRReference] = None
    originalPrescription: Optional[FHIRReference] = None
    payee: Optional[ClaimPayee] = None
    referral: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    careTeam: Optional[List[ClaimCareTeam]] = None
    information: Optional[List[ClaimInformation]] = None
    diagnosis: Optional[List[ClaimDiagnosis]] = None
    procedure: Optional[List[ClaimProcedure]] = None
    insurance: Optional[List[ClaimInsurance]] = None
    accident: Optional[ClaimAccident] = None
    employmentImpacted: Optional[Period] = None
    hospitalization: Optional[Period] = None
    item: Optional[List[ClaimItem]] = None
    total: Optional[Money] = None