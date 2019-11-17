#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2019-11-17.
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


@dataclass
class AuditEventEntityDetail(BackboneElement):
    """ Additional Information about the entity.

    Tagged value pairs for conveying additional information about the entity.
    """
    resource_type: ClassVar[str] = "AuditEventEntityDetail"

    type: str = None
    value: str = None


@dataclass
class AuditEventAgentNetwork(BackboneElement):
    """ Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """
    resource_type: ClassVar[str] = "AuditEventAgentNetwork"

    address: Optional[str] = None
    type: Optional[str] = None


@dataclass
class AuditEventAgent(BackboneElement):
    """ Actor involved in the event.

    An actor taking an active role in the event or activity that is logged.
    """
    resource_type: ClassVar[str] = "AuditEventAgent"

    role: Optional[List[CodeableConcept]] = None
    reference: Optional[FHIRReference] = None
    userId: Optional[Identifier] = None
    altId: Optional[str] = None
    name: Optional[str] = None
    requestor: bool = None
    location: Optional[FHIRReference] = None
    policy: Optional[List[str]] = None
    media: Optional[Coding] = None
    network: Optional[AuditEventAgentNetwork] = None
    purposeOfUse: Optional[List[CodeableConcept]] = None


@dataclass
class AuditEventSource(BackboneElement):
    """ Audit Event Reporter.

    The system that is reporting the event.
    """
    resource_type: ClassVar[str] = "AuditEventSource"

    site: Optional[str] = None
    identifier: Identifier = None
    type: Optional[List[Coding]] = None


@dataclass
class AuditEventEntity(BackboneElement):
    """ Data or objects used.

    Specific instances of data or objects that have been accessed.
    """
    resource_type: ClassVar[str] = "AuditEventEntity"

    identifier: Optional[Identifier] = None
    reference: Optional[FHIRReference] = None
    type: Optional[Coding] = None
    role: Optional[Coding] = None
    lifecycle: Optional[Coding] = None
    securityLabel: Optional[List[Coding]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    query: Optional[str] = None
    detail: Optional[List[AuditEventEntityDetail]] = None


@dataclass
class AuditEvent(DomainResource):
    """ Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    resource_type: ClassVar[str] = "AuditEvent"

    type: Coding = None
    subtype: Optional[List[Coding]] = None
    action: Optional[str] = None
    recorded: FHIRDate = None
    outcome: Optional[str] = None
    outcomeDesc: Optional[str] = None
    purposeOfEvent: Optional[List[CodeableConcept]] = None
    agent: List[AuditEventAgent] = field(default_factory=list)
    source: AuditEventSource = None
    entity: Optional[List[AuditEventEntity]] = None