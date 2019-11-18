#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Subscription) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class SubscriptionChannelPayload(BackboneElement):
    """ Payload definition.

    The payload mimetype and content.  If the payload is not present, then
    there is no payload in the notification, just a notification.
    """
    resource_type: ClassVar[str] = "SubscriptionChannelPayload"

    contentType: Optional[str] = None
    content: Optional[str] = None


@dataclass
class SubscriptionFilterBy(BackboneElement):
    """ Criteria for narrowing the topic stream.

    The filter properties to be applied to narrow the topic stream.  When
    multiple filters are applied, evaluates to true if all the conditions are
    met; otherwise it returns false.   (i.e., logical AND).
    """
    resource_type: ClassVar[str] = "SubscriptionFilterBy"

    name: str = None
    matchType: Optional[str] = None
    value: str = None


@dataclass
class SubscriptionChannel(BackboneElement):
    """ The channel on which to report matches to the criteria.

    Details where to send notifications when resources are received that meet
    the criteria.
    """
    resource_type: ClassVar[str] = "SubscriptionChannel"

    type: CodeableConcept = None
    endpoint: Optional[str] = None
    header: Optional[List[str]] = None
    heartbeatPeriod: Optional[int] = None
    payload: Optional[SubscriptionChannelPayload] = None


@dataclass
class Subscription(DomainResource):
    """ Notification about a Topic.

    The subscription resource describes a particular client's request to be
    notified about a Topic.
    """
    resource_type: ClassVar[str] = "Subscription"

    identifier: Optional[List[Identifier]] = None
    name: Optional[str] = None
    status: str = None
    topic: FHIRReference = None
    contact: Optional[List[ContactPoint]] = None
    end: Optional[FHIRDate] = None
    reason: str = None
    filterBy: Optional[List[SubscriptionFilterBy]] = None
    error: Optional[List[CodeableConcept]] = None
    eventCount: Optional[int] = None
    channel: SubscriptionChannel = None