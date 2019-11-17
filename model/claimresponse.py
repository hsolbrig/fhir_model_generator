#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money


@dataclass
class ClaimResponseAddItemDetail(BackboneElement):
    """ Added items details.

    The second tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetail"

    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    fee: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ClaimResponseItemAdjudication"]] = None


@dataclass
class ClaimResponseItemDetailSubDetail(BackboneElement):
    """ Subdetail line items.

    The third tier service adjudications for submitted services.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetailSubDetail"

    sequenceLinkId: int = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ClaimResponseItemAdjudication"]] = None


@dataclass
class ClaimResponseItemAdjudication(BackboneElement):
    """ Adjudication details.

    The adjudication results.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemAdjudication"

    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    value: Optional[float] = None


@dataclass
class ClaimResponseItemDetail(BackboneElement):
    """ Detail line items.

    The second tier service adjudications for submitted services.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetail"

    sequenceLinkId: int = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = None
    subDetail: Optional[List[ClaimResponseItemDetailSubDetail]] = None


@dataclass
class ClaimResponseItem(BackboneElement):
    """ Line items.

    The first tier service adjudications for submitted services.
    """
    resource_type: ClassVar[str] = "ClaimResponseItem"

    sequenceLinkId: int = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = None
    detail: Optional[List[ClaimResponseItemDetail]] = None


@dataclass
class ClaimResponseAddItem(BackboneElement):
    """ Insurer added line items.

    The first tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItem"

    sequenceLinkId: Optional[List[int]] = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    service: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    fee: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = None
    detail: Optional[List[ClaimResponseAddItemDetail]] = None


@dataclass
class ClaimResponseError(BackboneElement):
    """ Processing errors.

    Mutually exclusive with Services Provided (Item).
    """
    resource_type: ClassVar[str] = "ClaimResponseError"

    sequenceLinkId: Optional[int] = None
    detailSequenceLinkId: Optional[int] = None
    subdetailSequenceLinkId: Optional[int] = None
    code: CodeableConcept = None


@dataclass
class ClaimResponsePayment(BackboneElement):
    """ Payment details, if paid.

    Payment details for the claim if the claim has been paid.
    """
    resource_type: ClassVar[str] = "ClaimResponsePayment"

    type: Optional[CodeableConcept] = None
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    amount: Optional[Money] = None
    identifier: Optional[Identifier] = None


@dataclass
class ClaimResponseProcessNote(BackboneElement):
    """ Processing notes.

    Note text.
    """
    resource_type: ClassVar[str] = "ClaimResponseProcessNote"

    number: Optional[int] = None
    type: Optional[CodeableConcept] = None
    text: Optional[str] = None
    language: Optional[CodeableConcept] = None


@dataclass
class ClaimResponseInsurance(BackboneElement):
    """ Insurance or medical plan.

    Financial instrument by which payment information for health care.
    """
    resource_type: ClassVar[str] = "ClaimResponseInsurance"

    sequence: int = None
    focal: bool = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None
    preAuthRef: Optional[List[str]] = None
    claimResponse: Optional[FHIRReference] = None


@dataclass
class ClaimResponse(DomainResource):
    """ Remittance resource.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    resource_type: ClassVar[str] = "ClaimResponse"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    patient: Optional[FHIRReference] = None
    created: Optional[FHIRDate] = None
    insurer: Optional[FHIRReference] = None
    requestProvider: Optional[FHIRReference] = None
    requestOrganization: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    disposition: Optional[str] = None
    payeeType: Optional[CodeableConcept] = None
    item: Optional[List[ClaimResponseItem]] = None
    addItem: Optional[List[ClaimResponseAddItem]] = None
    error: Optional[List[ClaimResponseError]] = None
    totalCost: Optional[Money] = None
    unallocDeductable: Optional[Money] = None
    totalBenefit: Optional[Money] = None
    payment: Optional[ClaimResponsePayment] = None
    reserved: Optional[Coding] = None
    form: Optional[CodeableConcept] = None
    processNote: Optional[List[ClaimResponseProcessNote]] = None
    communicationRequest: Optional[List[FHIRReference]] = None
    insurance: Optional[List[ClaimResponseInsurance]] = None