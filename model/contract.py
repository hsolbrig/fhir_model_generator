#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Contract) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
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
from .signature import Signature


@dataclass
class ContractTermAgent(BackboneElement):
    """ Contract Term Agent List.

    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ContractTermAgent"

    actor: FHIRReference = None
    role: Optional[List[CodeableConcept]] = None


@dataclass
class ContractTermValuedItem(BackboneElement):
    """ Contract Term Valued Item List.

    Contract Provision Valued Item List.
    """
    resource_type: ClassVar[str] = "ContractTermValuedItem"

    entityCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='entity',))
    entityReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='entity',))
    identifier: Optional[Identifier] = None
    effectiveTime: Optional[FHIRDate] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    points: Optional[float] = None
    net: Optional[Money] = None


@dataclass
class ContractAgent(BackboneElement):
    """ Entity being ascribed responsibility.

    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ContractAgent"

    actor: FHIRReference = None
    role: Optional[List[CodeableConcept]] = None


@dataclass
class ContractSigner(BackboneElement):
    """ Contract Signatory.

    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    resource_type: ClassVar[str] = "ContractSigner"

    type: Coding = None
    party: FHIRReference = None
    signature: List[Signature] = field(default_factory=list)


@dataclass
class ContractValuedItem(BackboneElement):
    """ Contract Valued Item List.
    """
    resource_type: ClassVar[str] = "ContractValuedItem"

    entityCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='entity',))
    entityReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='entity',))
    identifier: Optional[Identifier] = None
    effectiveTime: Optional[FHIRDate] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    points: Optional[float] = None
    net: Optional[Money] = None


@dataclass
class ContractTerm(BackboneElement):
    """ Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    resource_type: ClassVar[str] = "ContractTerm"

    identifier: Optional[Identifier] = None
    issued: Optional[FHIRDate] = None
    applies: Optional[Period] = None
    type: Optional[CodeableConcept] = None
    subType: Optional[CodeableConcept] = None
    topic: Optional[List[FHIRReference]] = None
    action: Optional[List[CodeableConcept]] = None
    actionReason: Optional[List[CodeableConcept]] = None
    securityLabel: Optional[List[Coding]] = None
    agent: Optional[List[ContractTermAgent]] = None
    text: Optional[str] = None
    valuedItem: Optional[List[ContractTermValuedItem]] = None
    group: Optional[List["ContractTerm"]] = None


@dataclass
class ContractFriendly(BackboneElement):
    """ Contract Friendly Language.

    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    resource_type: ClassVar[str] = "ContractFriendly"

    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class ContractLegal(BackboneElement):
    """ Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractLegal"

    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class ContractRule(BackboneElement):
    """ Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractRule"

    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class Contract(DomainResource):
    """ Legal Agreement.

    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """
    resource_type: ClassVar[str] = "Contract"

    identifier: Optional[Identifier] = None
    status: Optional[str] = None
    issued: Optional[FHIRDate] = None
    applies: Optional[Period] = None
    subject: Optional[List[FHIRReference]] = None
    topic: Optional[List[FHIRReference]] = None
    authority: Optional[List[FHIRReference]] = None
    domain: Optional[List[FHIRReference]] = None
    type: Optional[CodeableConcept] = None
    subType: Optional[List[CodeableConcept]] = None
    action: Optional[List[CodeableConcept]] = None
    actionReason: Optional[List[CodeableConcept]] = None
    decisionType: Optional[CodeableConcept] = None
    contentDerivative: Optional[CodeableConcept] = None
    securityLabel: Optional[List[Coding]] = None
    agent: Optional[List[ContractAgent]] = None
    signer: Optional[List[ContractSigner]] = None
    valuedItem: Optional[List[ContractValuedItem]] = None
    term: Optional[List[ContractTerm]] = None
    bindingAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='binding',))
    bindingReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='binding',))
    friendly: Optional[List[ContractFriendly]] = None
    legal: Optional[List[ContractLegal]] = None
    rule: Optional[List[ContractRule]] = None