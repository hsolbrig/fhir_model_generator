#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ReferralRequest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ReferralRequestRequester(BackboneElement):
    """ Who/what is requesting service.

    The individual who initiated the request and has responsibility for its
    activation.
    """
    resource_type: ClassVar[str] = "ReferralRequestRequester"

    agent: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class ReferralRequest(DomainResource):
    """ A request for referral or transfer of care.

    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """
    resource_type: ClassVar[str] = "ReferralRequest"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[List[FHIRReference]] = None
    basedOn: Optional[List[FHIRReference]] = None
    replaces: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: str = None
    intent: str = None
    type: Optional[CodeableConcept] = None
    priority: Optional[str] = None
    serviceRequested: Optional[List[CodeableConcept]] = None
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[ReferralRequestRequester] = None
    specialty: Optional[CodeableConcept] = None
    recipient: Optional[List[FHIRReference]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    description: Optional[str] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    relevantHistory: Optional[List[FHIRReference]] = None