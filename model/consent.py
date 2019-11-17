#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Consent) on 2019-11-17.
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
from .period import Period


@dataclass
class ConsentProvisionActor(BackboneElement):
    """ Who|what controlled by this rule (or group, by role).

    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    resource_type: ClassVar[str] = "ConsentProvisionActor"

    role: CodeableConcept = None
    reference: FHIRReference = None


@dataclass
class ConsentProvisionData(BackboneElement):
    """ Data controlled by this rule.

    The resources controlled by this rule if specific resources are referenced.
    """
    resource_type: ClassVar[str] = "ConsentProvisionData"

    meaning: str = None
    reference: FHIRReference = None


@dataclass
class ConsentPolicy(BackboneElement):
    """ Policies covered by this consent.

    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """
    resource_type: ClassVar[str] = "ConsentPolicy"

    authority: Optional[str] = None
    uri: Optional[str] = None


@dataclass
class ConsentVerification(BackboneElement):
    """ Consent Verified by patient or family.

    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """
    resource_type: ClassVar[str] = "ConsentVerification"

    verified: bool = None
    verificationType: Optional[CodeableConcept] = None
    verifiedBy: Optional[FHIRReference] = None
    verifiedWith: Optional[FHIRReference] = None
    verificationDate: Optional[List[FHIRDate]] = None


@dataclass
class ConsentProvision(BackboneElement):
    """ Constraints to the base Consent.policyRule/Consent.policy.

    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    resource_type: ClassVar[str] = "ConsentProvision"

    type: Optional[str] = None
    period: Optional[Period] = None
    actor: Optional[List[ConsentProvisionActor]] = None
    action: Optional[List[CodeableConcept]] = None
    securityLabel: Optional[List[Coding]] = None
    purpose: Optional[List[Coding]] = None
    class_fhir: Optional[List[Coding]] = field(default_factory=list, metadata=dict(orig_name='class'))
    code: Optional[List[CodeableConcept]] = None
    dataPeriod: Optional[Period] = None
    data: Optional[List[ConsentProvisionData]] = None
    provision: Optional[List["ConsentProvision"]] = None


@dataclass
class Consent(DomainResource):
    """ A healthcare consumer's  or third party's choices to permit or deny
    recipients or roles to perform actions for specific purposes and periods of
    time.

    A record of a healthcare consumer’s  choices  or choices made on their
    behalf by a third party, which permits or denies identified recipient(s) or
    recipient role(s) to perform one or more actions within a given policy
    context, for specific purposes and periods of time.
    """
    resource_type: ClassVar[str] = "Consent"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    scope: CodeableConcept = None
    category: List[CodeableConcept] = field(default_factory=list)
    patient: Optional[FHIRReference] = None
    dateTime: Optional[FHIRDate] = None
    performer: Optional[List[FHIRReference]] = None
    organization: Optional[List[FHIRReference]] = None
    sourceAttachment: Optional[List[Attachment]] = None
    sourceReference: Optional[List[FHIRReference]] = None
    policy: Optional[List[ConsentPolicy]] = None
    policyRule: Optional[CodeableConcept] = None
    verification: Optional[List[ConsentVerification]] = None
    provision: Optional[ConsentProvision] = None