#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference


@dataclass
class MessageHeaderDestination(BackboneElement):
    """ Message destination application(s).

    The destination application which the message is intended for.
    """
    resource_type: ClassVar[str] = "MessageHeaderDestination"

    name: Optional[str] = None
    target: Optional[FHIRReference] = None
    endpoint: str = None


@dataclass
class MessageHeaderSource(BackboneElement):
    """ Message source application.

    The source application from which this message originated.
    """
    resource_type: ClassVar[str] = "MessageHeaderSource"

    name: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None
    contact: Optional[ContactPoint] = None
    endpoint: str = None


@dataclass
class MessageHeaderResponse(BackboneElement):
    """ If this is a reply to prior message.

    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    resource_type: ClassVar[str] = "MessageHeaderResponse"

    identifier: str = None
    code: str = None
    details: Optional[FHIRReference] = None


@dataclass
class MessageHeader(DomainResource):
    """ A resource that describes a message that is exchanged between systems.

    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    resource_type: ClassVar[str] = "MessageHeader"

    event: Coding = None
    destination: Optional[List[MessageHeaderDestination]] = None
    receiver: Optional[FHIRReference] = None
    sender: Optional[FHIRReference] = None
    timestamp: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    author: Optional[FHIRReference] = None
    source: MessageHeaderSource = None
    responsible: Optional[FHIRReference] = None
    reason: Optional[CodeableConcept] = None
    response: Optional[MessageHeaderResponse] = None
    focus: Optional[List[FHIRReference]] = None