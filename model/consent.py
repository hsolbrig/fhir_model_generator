#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Consent) on 2019-11-17.
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
class ConsentExceptActor(BackboneElement):
    """ Who|what controlled by this exception (or group, by role).

    Who or what is controlled by this Exception. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    resource_type: ClassVar[str] = "ConsentExceptActor"

    role: CodeableConcept = None
    reference: FHIRReference = None


@dataclass
class ConsentExceptData(BackboneElement):
    """ Data controlled by this exception.

    The resources controlled by this exception, if specific resources are
    referenced.
    """
    resource_type: ClassVar[str] = "ConsentExceptData"

    meaning: str = None
    reference: FHIRReference = None


@dataclass
class ConsentActor(BackboneElement):
    """ Who|what controlled by this consent (or group, by role).

    Who or what is controlled by this consent. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    resource_type: ClassVar[str] = "ConsentActor"

    role: CodeableConcept = None
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
class ConsentData(BackboneElement):
    """ Data controlled by this consent.

    The resources controlled by this consent, if specific resources are
    referenced.
    """
    resource_type: ClassVar[str] = "ConsentData"

    meaning: str = None
    reference: FHIRReference = None


@dataclass
class ConsentExcept(BackboneElement):
    """ Additional rule -  addition or removal of permissions.

    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    resource_type: ClassVar[str] = "ConsentExcept"

    type: str = None
    period: Optional[Period] = None
    actor: Optional[List[ConsentExceptActor]] = None
    action: Optional[List[CodeableConcept]] = None
    securityLabel: Optional[List[Coding]] = None
    purpose: Optional[List[Coding]] = None
    class_fhir: Optional[List[Coding]] = field(default_factory=list, metadata=dict(orig_name='class'))
    code: Optional[List[Coding]] = None
    dataPeriod: Optional[Period] = None
    data: Optional[List[ConsentExceptData]] = None


@dataclass
class Consent(DomainResource):
    """ A healthcare consumer's policy choices to permits or denies recipients or
    roles to perform actions for specific purposes and periods of time.

    A record of a healthcare consumer’s policy choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """
    resource_type: ClassVar[str] = "Consent"

    identifier: Optional[Identifier] = None
    status: str = None
    category: Optional[List[CodeableConcept]] = None
    patient: FHIRReference = None
    period: Optional[Period] = None
    dateTime: Optional[FHIRDate] = None
    consentingParty: Optional[List[FHIRReference]] = None
    actor: Optional[List[ConsentActor]] = None
    action: Optional[List[CodeableConcept]] = None
    organization: Optional[List[FHIRReference]] = None
    sourceAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='source',))
    sourceIdentifier: Optional[Identifier] = field(default=None, metadata=dict(one_of_many='source',))
    sourceReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='source',))
    policy: Optional[List[ConsentPolicy]] = None
    policyRule: Optional[str] = None
    securityLabel: Optional[List[Coding]] = None
    purpose: Optional[List[Coding]] = None
    dataPeriod: Optional[Period] = None
    data: Optional[List[ConsentData]] = None
    except_fhir: Optional[List[ConsentExcept]] = field(default_factory=list, metadata=dict(orig_name='except'))